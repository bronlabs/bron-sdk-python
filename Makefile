PY := python

# Compute next patch version from latest git tag (e.g., v0.1.5 -> 0.1.6)
VERSION ?= $(shell git describe --tags --abbrev=0 2>/dev/null | sed 's/^v//' | awk -F. '{ $$NF = $$NF + 1; OFS="."; print $$0 }')

generate:
	$(PY) -m bron_sdk_py.codegen.generator bron-open-api-public.json src/bron_sdk_py/types src/bron_sdk_py/api

lint:
	$(PY) -m pyflakes src || true

test:
	$(PY) -m pytest -q tests

generate-keys:
	$(PY) -m bron_sdk_py.utils.key_generator

update-version:
	$(PY) scripts/update_version.py

build:
	$(PY) scripts/update_version.py
	@echo "Build steps here (e.g., python -m build)"

publish:
	$(PY) scripts/update_version.py
	@echo "Use your packaging flow (build wheel/sdist, bump version)"


