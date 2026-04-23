.PHONY: install lab kernel run clean

install:
	uv sync

lab:
	uv run jupyter lab

kernel:
	uv run python -m ipykernel install --user --name spark-plug --display-name "PySpark (spark-plug)"

run:
	@if [ -z "$(nb)" ]; then echo "Usage: make run nb=<notebook>.ipynb"; exit 1; fi
	uv run jupyter nbconvert --to notebook --execute --inplace $(nb)

clean:
	rm -rf .venv __pycache__ .ipynb_checkpoints data/output
