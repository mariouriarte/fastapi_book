.PHONY: help up down build logs test-unit test-schema test-schema-docker

help: ## Muestra este mensaje de ayuda
	@echo "Uso: make [comando]"
	@echo ""
	@echo "Comandos:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2}'

up: ## Inicia los contenedores en segundo plano
	docker-compose up -d

down: ## Detiene y elimina los contenedores
	docker-compose down

build: ## Construye las imágenes de Docker
	docker-compose build

logs: ## Muestra los logs de los contenedores
	docker-compose logs -f

test-unit: ## Ejecuta las pruebas unitarias usando fakes dentro del contenedor
	docker-compose exec -T -e CRYPTID_UNIT_TEST=1 api pytest

test-schema: ## Ejecuta pruebas de Schemathesis localmente contra fakes (puerto 8001)
	@echo "Levantando instancia temporal de la API con Fakes..."
	docker-compose run -d --name api-test -e CRYPTID_UNIT_TEST=1 -p 8001:80 api
	@sleep 5
	-schemathesis run http://localhost:8001/openapi.json --checks all
	@echo "Limpiando instancia temporal..."
	docker rm -f api-test

test-schema-docker: ## Ejecuta pruebas de Schemathesis vía Docker contra fakes
	@echo "Levantando instancia temporal de la API con Fakes..."
	docker-compose run -d --name api-test -e CRYPTID_UNIT_TEST=1 -p 8001:80 api
	@sleep 5
	-docker run --rm --network host schemathesis/schemathesis:stable run http://localhost:8001/openapi.json --checks all
	@echo "Limpiando instancia temporal..."
	docker rm -f api-test


 

# --- Configuración para pruebas de integración con Base de Datos Real ---

DB_TEST_NAME=test_db
DB_TEST_USER=test_user
DB_TEST_PASS=test_pass
DB_TEST_PORT=5433
NETWORK_NAME=fastapi_book_test_net

test-net: ## Crea la red de pruebas si no existe
	@docker network inspect $(NETWORK_NAME) >/dev/null 2>&1 || docker network create $(NETWORK_NAME)

test-db-up: test-net ## Inicia una base de datos de pruebas aislada
	docker run -d --name $(DB_TEST_NAME) \
		--network $(NETWORK_NAME) \
		-e POSTGRES_DB=cryptid \
		-e POSTGRES_USER=$(DB_TEST_USER) \
		-e POSTGRES_PASSWORD=$(DB_TEST_PASS) \
		-p $(DB_TEST_PORT):5432 \
		postgres:15-alpine
	@sleep 3

test-db-down: ## Elimina la base de datos de pruebas y la red
	docker rm -f $(DB_TEST_NAME) || true
	docker network rm $(NETWORK_NAME) || true

test-schema-real: test-db-up ## Ejecuta Schemathesis contra DB real (puerto 8002)
	@echo "Levantando API conectada a DB de pruebas..."
	-docker-compose run -d --name api-real-test \
		--network $(NETWORK_NAME) \
		-e DATABASE_URL=postgresql://$(DB_TEST_USER):$(DB_TEST_PASS)@$(DB_TEST_NAME):5432/cryptid \
		-e CRYPTID_UNIT_TEST=0 \
		-p 8002:8000 api
	@echo "Esperando a que la API y la DB estén listas..."
	@sleep 5
	@echo "Ejecutando Schemathesis..."
	-schemathesis run http://localhost:8002/openapi.json --checks all
	@echo "Limpiando entorno de pruebas real..."
	-docker rm -f api-real-test
	-$(MAKE) test-db-down



