install:
	pip install -r requirements.txt

generate_venv:
	python -m venv ./venv

attach_venv:
	source ./venv/Scripts/activate

detach_venv:
	deactivate

venv: generate_venv attach_venv
