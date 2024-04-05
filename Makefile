format:
    black .
    isort .
    autoflake --remove-all-unused-imports --recursive --in-place .

test:
    mypy .

.PHONY: format test