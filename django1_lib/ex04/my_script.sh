#!/bin/bash

if [[ "$SHELL" = "/usr/bin/fish" ]]; then
	/usr/bin/fish -c "python -m venv django_venv && source $PWD/django_venv/bin/activate.fish && pip install -r requirements.txt && fish"
else
	/bin/bash -c "python -m venv django_venv && source $PWD/django_venv/bin/activate && pip install -r requirements.txt && bash"
fi
