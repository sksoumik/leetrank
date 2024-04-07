format-isort: ## Fixes .py files with isort
	@echo "⚙️ Fixing isort formatting issues"
	isort .

format-black: ## Fixes .py files with black
	@echo "⚙️ Fixing black formatting issues"
	black . --line-length 100

format-unused-imports: ## Fixes unused imports and unused variables
	@echo "⚙️ Removing unused imports"
	autoflake -i --remove-all-unused-imports --recursive .

format: format-unused-imports format-isort format-black

lint-flake8: ## Checks if .py files follow flake8
	@echo "⚙️ Checking flake8 errors"
	flake8 --max-line-length=100 .

lint-pylint: ## Checks if .py files follow pylint
	@echo "⚙️ Checking pylint errors"
	pylint --max-line-length=100 --recursive=y .

check-lint: lint-flake8 lint-pylint

clean: ## Cleans up the local-development environment except .env
	rm -rf .mypy_cache
	rm -rf .pytest_cache
	rm -f .coverage
	find . -name __pycache__ -type d -prune -exec rm -rf {} \;
	find . -name '.DS_Store' -delete
