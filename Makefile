venv/bin/activate:
	$(MAKE) virtualenv
	virtualenv -p ~/.pyenv/shims/python3  venv

.PHONY: virtualenv
virtualenv:
	@command -v virtualenv > /dev/null || pip3 install virtualenv

.PHONY: python-deps
python-deps: venv/bin/activate requirements.txt
	( \
		source venv/bin/activate; \
		LDFLAGS="-L/usr/local/opt/openssl/lib" \
		DYLD_LIBRARY_PATH=$DYLD_LIBRARY_PATH:$(brew --prefix openssl)/lib \
		pip3 install -r requirements.txt; \
	)

.PHONY: test
test: python-deps
	pytest

# Install Git hooks (including local Python dependencies)
.PHONY: git-hooks
git-hooks: venv/bin/pre-commit
	@( \
		source venv/bin/activate; \
		pre-commit install; \
	)

venv/bin/pre-commit:
	$(MAKE) python-deps