help:
	@echo "Makefile commands:"
	@echo "  install        — Установить зависимости"
	@echo "  run_test       — Запустить автотесты"
	@echo "  test_only      — Запустить автотесты только один автотест с меткой only"
	@echo "  linter         — Запустить проверку кода"

install:
	pip install -r requirements.txt

run_test:
	python3 -m pytest -v

test_only:
	python3 -m pytest -m only

linter:
	black .
	isort .
	flake8
