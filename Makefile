.PHONY: $(MAKECMDGOALS)
SHELL := /bin/bash

VERSION ?= $(shell git describe --tags --abbrev=0 | sed 's/v//' | awk -F. '{$$NF = $$NF + 1;} 1' | sed 's/ /./g')

generate:
	python3 -m venv --clear .venv
	.venv/bin/pip install -q -e .
	.venv/bin/python -m bron_sdk_python.codegen.generator bron-open-api-public.json src/bron_sdk_python/types src/bron_sdk_python/api

lint:
	python -m pyflakes src || true

test:
	python -m pytest -q tests

generate-keys:
	python -m bron_sdk_python.utils.key_generator

update-version:
	VERSION=${VERSION} python scripts/update_version.py
	git tag v${VERSION} -m "Release ${VERSION}"
	git commit -am "Update version to ${VERSION}"
	git push origin master
	git push --tags
