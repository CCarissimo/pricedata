#!/bin/bash

# Path to your virtual environment's activate script
VENV_ACTIVATE="/media/data/pricedata_cesare/pricedata/.venv/bin/activate"

# Path to your Python script
PYTHON_SCRIPT="/media/data/pricedata_cesare/pricedata/scrape_price_data.py"

# Activate the virtual environment
source $VENV_ACTIVATE

# Run the Python script
python $PYTHON_SCRIPT

# Deactivate the virtual environment (optional)
deactivate