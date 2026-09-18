# 常用开发命令
# Windows 上没有 make 时，可用 mingw32-make 代替
.PHONY: install dev run test lint fmt check hooks

install:
	pip install -r requirements.txt

dev:
	pip install -r requirements-dev.txt

run:
	python demo.py

test:
	python -m pytest

lint:
	ruff check .

fmt:
	ruff format .

check: lint test

hooks:
	pre-commit install
