#!/bin/bash


# Create virtual environment
python -m venv venv

# Activate virtual environment
source venv/Scripts/activate

# Install PyPDF2 package
pip install PyPDF2


# Run main.py script
python main.py

# Deactivate virtual environment
deactivate
