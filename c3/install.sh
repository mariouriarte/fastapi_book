#!/bin/bash

python -m venv venv
source venv/bin/activate

pip install fastapi uvicorn httpie requests httpx pytest
