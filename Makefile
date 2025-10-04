# Compute next patch version from latest git tag (e.g., v0.1.5 -> 0.1.6)
VERSION ?= $(shell git describe --tags --abbrev=0 2>/dev/null | sed 's/^v//' | awk -F. '{ $$NF = $$NF + 1; OFS="."; print $$0 }')

generate:
	python -m bron_sdk_python.codegen.generator bron-open-api-public.json src/bron_sdk_python/types src/bron_sdk_python/api

lint:
	python -m pyflakes src || true

test:
	python -m pytest -q tests

generate-keys:
	python -m bron_sdk_python.utils.key_generator

update-version:
	python scripts/update_version.py
