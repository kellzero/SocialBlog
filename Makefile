# Versão do Python (ajuste conforme necessário)
PYTHON_VERSION ?= 3.13.1
# Diretórios de código
LIBRARY_DIRS = mylibrary
# Diretório de build
BUILD_DIR ?= build

# PyTest options
PYTEST_HTML_OPTIONS = --html=$(BUILD_DIR)/report.html --self-contained-html
PYTEST_TAP_OPTIONS = --tap-combined --tap-outdir $(BUILD_DIR)
PYTEST_COVERAGE_OPTIONS = --cov=$(LIBRARY_DIRS)
PYTEST_OPTIONS ?= $(PYTEST_HTML_OPTIONS) $(PYTEST_TAP_OPTIONS) $(PYTEST_COVERAGE_OPTIONS)

# MyPy typechecking options
MYPY_OPTS ?= --python-version $(basename $(PYTHON_VERSION)) --show-column-numbers --pretty --html-report $(BUILD_DIR)/mypy

# Poetry (ajustado para Windows)
POETRY ?= poetry
RUN_PYPKG_BIN = $(POETRY) run

# Cores no Windows PowerShell
COLOR_ORANGE = [33m
COLOR_RESET = [0m

##@ Utility

.PHONY: help
help:  ## Display this help
	@echo "Comandos disponíveis:"
	@echo "  make version-python     - Mostra versao do Python"
	@echo "  make test               - Roda testes"
	@echo "  make build              - Build do projeto"
	@echo "  make publish            - Publica pacote"
	@echo "  make deps                - Instala todas dependencias"
	@echo "  make deps-py             - Instala dependencias Python"
	@echo "  make check               - Roda linters"
	@echo "  make format-py           - Formata codigo com black"
	@echo "  make migrate             - Roda migrations Django"
	@echo "  make seed                - Popula banco com dados iniciais"

.PHONY: version-python
version-python: ## Echos the version of Python in use
	@echo $(PYTHON_VERSION)

##@ Testing

.PHONY: test
test: ## Runs tests
	$(RUN_PYPKG_BIN) pytest $(PYTEST_OPTIONS) tests/*.py

##@ Building and Publishing

.PHONY: build
build: ## Runs a build
	$(POETRY) build

.PHONY: publish
publish: ## Publish a build to the configured repo
	$(POETRY) publish

.PHONY: deps-py-update
deps-py-update: pyproject.toml ## Update Poetry deps
	$(POETRY) update

##@ Setup

.PHONY: deps
deps: deps-py ## Installs all dependencies

.PHONY: deps-py
deps-py: ## Installs Python development and runtime dependencies
	pip install --upgrade pip
	pip install --upgrade poetry
	$(POETRY) install

##@ Code Quality

.PHONY: check
check: check-py ## Runs linters

.PHONY: check-py
check-py: check-py-flake8 check-py-black check-py-mypy ## Checks only Python files

.PHONY: check-py-flake8
check-py-flake8: ## Runs flake8 linter
	$(RUN_PYPKG_BIN) flake8 .

.PHONY: check-py-black
check-py-black: ## Runs black in check mode
	$(RUN_PYPKG_BIN) black --check --line-length 118 --fast .

.PHONY: check-py-mypy
check-py-mypy: ## Runs mypy
	$(RUN_PYPKG_BIN) mypy $(MYPY_OPTS) $(LIBRARY_DIRS)

.PHONY: format-py
format-py: ## Runs black, makes changes where necessary
	$(RUN_PYPKG_BIN) black .

##@ Django Commands

.PHONY: migrate
migrate: ## Roda migrations do Django
	docker-compose exec web python manage.py migrate --noinput

.PHONY: seed
seed: ## Popula banco com dados iniciais
	docker-compose exec web python manage.py seed

.PHONY: shell
shell: ## Abre shell do Django
	docker-compose exec web python manage.py shell

.PHONY: createsuperuser
createsuperuser: ## Cria superusuário
	docker-compose exec web python manage.py createsuperuser