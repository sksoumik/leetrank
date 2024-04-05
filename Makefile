format-isort: ## Fixes .py files with isort
	@echo "Fixing isort formatting issues"
	isort .

format-black: ## Fixes .py files with black
	@echo "Fixing black formatting issues"
	black .

format-unused-imports: ## Fixes unused imports and unused variables
	@echo "Removing unused imports"
	autoflake -i --remove-all-unused-imports --recursive .

format: format-unused-imports format-isort format-black