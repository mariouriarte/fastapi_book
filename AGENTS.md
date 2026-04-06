# Agent Guidelines for FastAPI Book Project

This document outlines the conventions, commands, and best practices for developing within this codebase. Adhering to these guidelines ensures consistency, maintainability, and efficient collaboration.

---

## 1. Build, Lint, and Test Commands

All development and testing activities primarily leverage `docker-compose`. Ensure Docker and Docker Compose are running.

### General Commands

*   **Start Development Environment (with fakes):**
    ```bash
    make up
    ```
    This command builds (if necessary) and starts the API service in the background. The API will use fake data for development and unit testing.

*   **Stop Development Environment:**
    ```bash
    make down
    ```
    Stops and removes the Docker containers.

*   **Build Docker Images:**
    ```bash
    make build
    ```
    Builds the Docker images for the services defined in `docker-compose.yml`.

*   **View Logs:**
    ```bash
    make logs
    ```
    Follows the logs of the running Docker containers.

### Testing

Tests are executed within the Dockerized environment.

*   **Run All Unit Tests:**
    ```bash
    make test-unit
    ```
    Executes all unit tests using `pytest` within the `api` container. The `CRYPTID_UNIT_TEST=1` environment variable ensures fake data is used.

*   **Run a Single Unit Test File:**
    To run tests from a specific file, append the file path to the `pytest` command:
    ```bash
    docker-compose exec -T -e CRYPTID_UNIT_TEST=1 api pytest app/test/unit/service/test_creature.py
    ```

*   **Run a Specific Unit Test:**
    To run a single test function within a file, use the `::` separator:
    ```bash
    docker-compose exec -T -e CRYPTID_UNIT_TEST=1 api pytest app/test/unit/service/test_creature.py::test_create
    ```

*   **Run Schema Tests (against Fakes):**
    ```bash
    make test-schema         # Local schemathesis CLI
    make test-schema-docker  # Schemathesis via Docker
    ```
    These commands run contract tests against the API using fake data.

*   **Run Schema Tests (against Real Database):**
    ```bash
    make test-schema-real
    ```
    This command spins up a temporary test database and the API connected to it, then runs schema tests.

### Linting and Type Checking

*   **Run MyPy (Type Checker):**
    ```bash
    docker-compose exec api mypy app/
    ```
    This project uses `mypy` for static type checking. Ensure all new and modified code passes `mypy` checks.

---

## 2. Code Style Guidelines

This section outlines the preferred code style, formatting, and structural conventions.

### Python Specifics

*   **PEP 8 Adherence:**
    All Python code must generally adhere to [PEP 8](https://www.python.org/dev/peps/pep-0008/).

*   **Imports:**
    *   Group imports in the following order:
        1.  Standard library imports (e.g., `os`, `sys`).
        2.  Third-party library imports (e.g., `fastapi`, `pydantic`, `pytest`).
        3.  Local application-specific imports (e.g., `from model.creature import Creature`).
    *   Alphabetize imports within each group.
    *   Avoid wildcard imports (`from module import *`).

*   **Formatting:**
    *   Use 4 spaces for indentation.
    *   Line length should ideally not exceed 79 characters, but can extend to 120 for readability in specific cases (e.g., long import statements, Pydantic Field definitions).
    *   Follow existing patterns for whitespace around operators and in function definitions.

*   **Typing:**
    *   **Strict Type Hinting:** All new Python code must use type hints for function arguments, return values, and class attributes where applicable.
    *   Use `typing` module types for complex scenarios (e.g., `List[str]`, `Optional[int]`, `Union[str, int]`). For Python 3.9+, prefer built-in generics (e.g., `list[str]`, `dict[str, int]`).

*   **Naming Conventions:**
    *   **Modules:** `snake_case` (e.g., `creature.py`, `explorer.py`).
    *   **Packages:** `snake_case` (e.g., `model`, `service`, `web`).
    *   **Classes:** `PascalCase` (e.g., `Creature`, `Missing`, `Duplicate`).
    *   **Functions/Methods:** `snake_case` (e.g., `get_all`, `create`).
    *   **Variables:** `snake_case`.
    *   **Constants:** `UPPER_SNAKE_CASE` (e.g., `DB_TEST_NAME`).

*   **Error Handling:**
    *   **Custom Exceptions:** Define custom exceptions in `app/errors.py` for application-specific error conditions (e.g., `Missing`, `Duplicate`).
    *   **FastAPI `HTTPException`:** For API endpoints, raise `fastapi.HTTPException` with appropriate `status_code` and `detail` for client-facing errors.
    *   Use `try...except` blocks for handling expected errors and ensuring graceful degradation.
    *   Avoid broad `except Exception:` clauses; catch specific exceptions.

*   **FastAPI Specific Patterns:**
    *   **Pydantic Models:** Use `pydantic.BaseModel` for defining request and response data structures. Leverage `pydantic.Field` for validation and `model_config` for schema examples.
    *   **APIRouter:** Organize API endpoints using `fastapi.APIRouter` for modularity.
    *   **Dependency Injection:** Utilize FastAPI's dependency injection system for managing database connections, authentication, and other shared resources.

---

## 3. Cursor/Copilot Rules

No specific Cursor or Copilot configuration files were found in this repository. Agents should adhere to the general code style guidelines and project conventions outlined above.

---

## 4. General Agent Behavior

*   **Context Awareness:** Always analyze surrounding code, existing tests, and configuration files before proposing or implementing changes.
*   **Idiomatic Code:** Strive to write code that is idiomatic to Python and the FastAPI framework, mimicking established patterns in the codebase.
*   **Incremental Changes:** Prefer smaller, focused changes that are easier to review and verify.
*   **Self-Correction:** Before marking a task as complete, run relevant tests, linting, and type checks to ensure the changes are correct and adhere to standards.

