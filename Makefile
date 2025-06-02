install:
	pip install -r requirements.txt

run:
	dvc repro

metrics:
	dvc metrics show

push:
	dvc push
