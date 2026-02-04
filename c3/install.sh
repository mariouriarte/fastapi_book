#!/bin/bash

if [ ! -d "venv" ]; then
    # Aquí pones lo que quieres hacer si NO existe
    echo '> No exixte venv, se creara...'
    python -m venv venv
fi

source venv/bin/activate

pip install fastapi uvicorn httpie requests httpx pytest
