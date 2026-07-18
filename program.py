from datetime import datetime
import os, sys, random, time, json
from collections import Counter

import Player

FOLDER = os.path.dirname(os.path.abspath(__file__))
CHARACTER_DATA = os.path.join(FOLDER, "characters.json") 

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



# --------------------------------------------------------------
# Data Functions
# --------------------------------------------------------------


def load_characters():
    try:
        with open(CHARACTER_DATA, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
        return dados
    except (FileNotFoundError, json.JSONDecodeError, KeyError):
        return []
    
def character_info_save(data):
    try:
        with open(CHARACTER_DATA, "w", encoding="utf-8") as arquivo:
            json.dump(data, arquivo, indent=4, ensure_ascii=False)
    except (FileNotFoundError, json.JSONDecodeError, KeyError):
        return []

def add_new_character(data, name, classe):
    new_id = len(data) + 1

    match classe:
        case "Mago":
            character = Player.Mage(new_id, name)
        case "Guerreiro":
            character = Player.Warrior(new_id, name)
        case "Arqueiro":
            character = Player.Archer(new_id, name)

    data.append(character.para_dict())
    character_info_save(data)

def show_all_characters(data):
    clean_terminal()
    for c in data:
        print("\n")
        print(f"{c['name']} na classe {c['class']} está no level {c['level']} com {c['hp']} de HP"
              f"\nFoi criado em {date_from_json(c['created_in'])}")
    user_go_by()

def show_characters_alive(data):
    clean_terminal()
    vivos = [c for c in data if c['hp'] > 0]
    for c in vivos:
        print("\n")
        print(f"{c['name']} na classe {c['class']} está no level {c['level']} com {c['hp']} de HP"
              f"\nFoi criado em {date_from_json(c['created_in'])}")
    user_go_by()
    
# --------------------------------------------------------------
# User Interaction
# --------------------------------------------------------------

classes = [Player.Mage, Player.Warrior, Player.Archer]



def random_class():
    random_choice = random.choice(classes)
    return random_choice

def class_choice(data, info, name_player):
    new_id = len(data) + 1
    match info:
        case "1" | "MAGO":
            _class = Player.Mage(new_id, name_player)
            _class.initial_text()
            time.sleep(2)
            return _class
        case "2" | "GUERREIRO":
            _class = Player.Warrior(new_id, name_player)
            _class.initial_text()
            time.sleep(2)
            return _class
        case "3" | "ARQUEIRO":
            _class = Player.Archer(new_id, name_player)
            _class.initial_text()
            time.sleep(2)
            return _class
        case _:
            print("Nenhuma classe foi escolhida." \
            "\nSerá escolhida uma classe aleatória entre as 3.")
            _class = random_class()(new_id, name_player)
            _class.initial_text()
            time.sleep(2)
            return _class

def user_choice(info, data):
    match info:
        case "1" | "LISTAR":
            choice_filter = input("Quer ver somente os vivos?" \
                            "\n1 - Sim" \
                            "\n2 - Não" \
                            "\n\nEscolha: ").upper()
            if choice_filter == "1" or choice_filter == "SIM":
                show_characters_alive(data)
            else:
                show_all_characters(data)
            return True
        case "2" | "CRIAR":
            Player.create_character(data)
            return True
        case "3" | "SUBIR":
            Player.character_level_up(data)
            return True
        case "4" | "FILTRAR":
            Player.filter_characters_per_class(data)
            return True
        case "5" | "SAIR":
            return False    
        case _:
            clean_terminal()
            print("Digite algo válido!")
            user_go_by()
            return True

clean_terminal()

data = load_characters()

print("Bem vindo ao RPG!\n")
time.sleep(1)
create_choice = input("Você deseja criar um personagem?" \
                "\n1 - Sim" \
                "\n2 - Não"
                "\n\nEscolha: ")

if create_choice == "1" or create_choice == "SIM":
    Player.create_character(data)

while True:
    clean_terminal()
    choice = input("1. Listar personagens" \
                "\n2. Criar personagem" \
                "\n3. Subir de nível" \
                "\n4. Filtrar por classe" \
                "\n5. Sair" \
                "\n\nEscolha: ").upper()
    
    data = load_characters()

    if not user_choice(choice, data):
        break