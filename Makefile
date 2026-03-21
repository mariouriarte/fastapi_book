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
	docker-compose exec -e CRYPTID_UNIT_TEST=1 api pytest

test-schema: ## Ejecuta pruebas de Schemathesis localmente
	schemathesis run http://localhost:8000/openapi.json --checks all

test-schema-docker: ## Ejecuta pruebas de Schemathesis vía Docker
	docker run --rm --network host schemathesis/schemathesis:stable run http://localhost:8000/openapi.json --checks all

 
