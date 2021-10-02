# Run tests using pytest
.PHONY: test
test:
	python -m pytest --version
	python -m pytest tests
## Format your code using black
.PHONY: black
black:
	python -m black --version
	python -m black .
## Run ci part
.PHONY: ci
ci:
	pre-commit run
## Run locally
.PHONY: run
run:
	uvicorn app.main:app --reload --port 8080
