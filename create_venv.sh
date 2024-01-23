#!/bin/zsh

# Create a Python virtual environment
python3 -m venv .venv

# Activate the virtual environment
source .venv/bin/activate

pip install --upgrade pip
pip install pip-tools

