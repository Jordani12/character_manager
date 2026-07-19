import os 
from datetime import datetime

# --------------------------------------------------------------
# Auxiliar functions
# --------------------------------------------------------------

def clean_terminal():
    os.system('cls')

def user_go_by():
    input("\nAperte enter para voltar.\n\n")

def date_from_json(date):
    _date_from_json = datetime.fromisoformat(date)
    return _date_from_json.strftime("%d/%m/%Y %H:%M")