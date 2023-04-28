.PHONY: install-dev
install-dev:
	@. ./venv/bin/activate &&\
	pip install --upgrade pip setuptools wheel &&\
	pip install --upgrade --requirement requirements.txt &&\
	pre-commit install &&\
	echo "Done."



# [pre_commit]-[BEGIN]
.PHONY: pre-commit-run
# Run tools for files from commit.
pre-commit-run:
	@pre-commit run

.PHONY: pre-commit-run-all
# Run tools for all files.
pre-commit-run-all:
	@pre-commit run --all-files
# [pre_commit]-[END]