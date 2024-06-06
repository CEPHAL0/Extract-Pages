@echo off

rem Create virtual environment
python -m venv venv

rem Activate virtual environment
call venv\Scripts\activate.bat

rem Install PyPDF2 package
pip install PyPDF2

rem Run main.py
python main.py

rem Deactivate virtual environment
deactivate
