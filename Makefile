NAME=textese
SYSTEM_DEPS=poppler

.PHONY: all install-deps uninstall-deps clean format build patch install uninstall reinstall initial-install

all: clean format build reinstall

install-deps:
	brew install ${SYSTEM_DEPS}
	poetry install

uninstall-deps:
	brew uninstall ${SYSTEM_DEPS}
	poetry env remove python

clean:
	rm -rf ./dist

format:
	poetry run python -m black ./${NAME}/*.py

build:
	poetry build

patch:
	poetry version patch

initial-install: install-deps install

install: build
	pip install --user dist/*.whl

uninstall:
	pip uninstall $(NAME)

reinstall: uninstall install

