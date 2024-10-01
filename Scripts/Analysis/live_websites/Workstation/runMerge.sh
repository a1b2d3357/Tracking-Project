#!/bin/bash

# Check if requirements.txt exists
if [ ! -f "requirements.txt" ]; then
  echo "Error: requirements.txt not found!"
  exit 1
fi

# Create a virtual environment in a folder named 'venv'
echo "Creating virtual environment..."
python3 -m venv venv

# Activate the virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install the required libraries
echo "Installing dependencies from requirements.txt..."
pip install -r requirements.txt

# Confirm installation
echo "All dependencies installed successfully."

# run Python script
python merge.py

deactivate