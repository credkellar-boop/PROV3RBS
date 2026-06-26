run:
	uvicorn app:app --reload

test:
	python tests/validate.py

install:
	pip install -r requirements.txt
