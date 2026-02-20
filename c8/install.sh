#!/bin/bash
set -e

VENV_DIR="venv"

# Check if python3 is installed
if ! command -v python3 &>/dev/null; then
    echo "Error: python3 could not be found. Please install it."
    exit 1
fi

# Create virtual environment if it doesn't exist
if [ ! -d "$VENV_DIR" ]; then
    echo "> Creating virtual environment in $VENV_DIR..."
    python3 -m venv "$VENV_DIR"
fi

# Activate virtual environment
echo "> Activating virtual environment..."
source "$VENV_DIR/bin/activate"

# Upgrade pip and install dependencies
echo "> Upgrading pip and installing dependencies..."
pip install --upgrade pip
pip install fastapi uvicorn httpie requests httpx pytest mypy

echo "> Setup complete!"
