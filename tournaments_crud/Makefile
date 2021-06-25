ABS_PATH := ${PWD}
ROOT_DIR := .
SRC_DIR := ${ROOT_DIR}/src
DB_SETUP_DIR := ${SRC_DIR}/setup.py
PYTHON := python3
VENV_BIN_DIR := ".venv/bin"
VENV_PIP := ${VENV_BIN_DIR}/pip
VENV_PY := ${VENV_BIN_DIR}/${PYTHON}

run: venv/bin/activate db/perm 
	@echo 'Running setup...'

venv/bin/activate: requirements.txt
	$(PYTHON) -m venv .venv
	$(VENV_PIP) install -r requirements.txt

db/setup:
	cd ${SRC_DIR} && ../$(VENV_PY) setup.py

db/perm: db/setup
	find . -name '*.db' -type f -exec sudo chmod -c 777 {} \;

clean:
	rm -rf .venv
