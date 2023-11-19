

.venv:
	python3 -m venv .venv

install: .venv
	. .venv/bin/activate && pip install -r requirements.txt

run-example: .venv
	. .venv/bin/activate && python3 example.py

run-redis-server:
	redis-server
