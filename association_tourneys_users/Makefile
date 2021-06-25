


PYTHON := python3
SHELL := /bin/bash


init: venv/init
	@echo '3. runs last. Initiliazes rules and their dependencies.'

venv/init: venv
	@echo '2. runs second. Activates and installs requirements.'
	source .venv/bin/activate; \
	pip install -r ./requirements.txt; \

venv:
	@echo '1. runs first. Creates .venv'
	$(PYTHON) -m venv .venv

clean:
	rm -rf .venv
	@#find -iname "*.pyc" -delete
