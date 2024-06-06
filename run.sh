#!/bin/bash


# Create virtual environment
python -m venv myenv

# Activate virtual environment
source myenv/bin/activate

# Install PyPDF2 package
pip install PyPDF2


# Run main.py script
python main.py

# Deactivate virtual environment
deactivate
