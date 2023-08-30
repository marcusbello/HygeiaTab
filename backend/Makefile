APP := hygeiatab-api
PORT := 8081
PYTHON3_10 := $(shell command -v python3 2> /dev/null)

ifndef PYTHON3_10
    $(error "Python 3.v is not installed! See README.md")
endif


ifeq (${IS_CI}, true)
	FLAGS := "--ci"
else
	FLAGS := "-s"
endif


PHONY: env

all: env test

env: env/bin/activate

env/bin/activate: requirements.txt
	test -d env || python3 -m venv env
	. env/bin/activate; pip install --upgrade pip; pip install pip-tools wheel -e .; pip install -r requirements.txt
	touch env/bin/activate

test: env
	. env/bin/activate; pytest $(FLAGS)	

dev: env
	. env/bin/activate; FASTAPI_APP=$(APP) uvicorn main:app --reload --port=$(PORT) --host=0.0.0.0

run:
	uvicorn main:app --reload

requirements.txt:
	pip freeze > requirements.txt


