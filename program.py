from datetime import datetime
import os, sys, random, time, json
from collections import Counter

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
# Class Heritage
# --------------------------------------------------------------

class Character:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.level = 1
        self.hp = 0
        self.classe = None
        self.created_in = datetime.now().isoformat()
    
    def level_up(self):
        self.level += 1
        self.hp += self.hp_per_nivel
        print(f"{self.name} subiu para o nível {self.level}! HP: {self.hp}")

    def para_dict(self):
        return {
            "id":         self.id,
            "name":       self.name,
            "class":      self.classe,
            "hp":         self.hp,
            "level":      self.level,
            "created_in": self.created_in
        }

class Mage(Character):
    hp_per_nivel = 5
    initial_hp = 60
    _classe = "Mago"

    def __init__(self, id, nome):
        super().__init__(id, nome)
        self.hp = self.initial_hp
        self.classe = self._classe

    def initial_text(self):
        clean_terminal()
        print(f"{self.name} é reconhecido como um grande MAGO.")

class Warrior(Character):
    hp_per_nivel = 10
    initial_hp = 100
    _classe = "Guerreiro"

    def __init__(self, id, nome):
        super().__init__(id, nome)
        self.hp = self.initial_hp
        self.classe = self._classe

    def initial_text(self):
        clean_terminal()
        print(f"{self.name} é reconhecido como um honrado GUERREIRO.")

class Archer(Character):
    hp_per_nivel = 8
    initial_hp = 80
    _classe = "Arqueiro"

    def __init__(self, id, nome):
        super().__init__(id, nome)
        self.hp = self.initial_hp
        self.classe = self._classe
    
    def initial_text(self):
        clean_terminal()
        print(f"{self.name} é reconhecido como um valioso ARQUEIRO.")

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
            character = Mage(new_id, name)
        case "Guerreiro":
            character = Warrior(new_id, name)
        case "Arqueiro":
            character = Archer(new_id, name)

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

classes = [Mage, Warrior, Archer]

def filter_characters_per_class(data):
    clean_terminal()
    choice = input("Você quer ver os personagens de qual classe?" \
                "\n1 - Mago" \
                "\n2 - Guerreiro" \
                "\n3 - Arqueiro" \
                "\n\nEscolha: ").upper()
    
    match choice:
        case "1" | "MAGO":
            choice = "Mago"
        case "2" | "GUERREIRO":
            choice = "Guerreiro"
        case "3" | "ARQUEIRO":
            choice = "Arqueiro"
        case _:
            print("Nenhuma classe foi escolhida.")
    
    clean_terminal()

    for c in filter(lambda c: c['class'] == choice, data):
        print(f"{c['name']} na classe {c['class']} está no level {c['level']} com {c['hp']} de HP"
                f"\nFoi criado em {date_from_json(c['created_in'])}")

    user_go_by()

def character_level_up(data):
    clean_terminal()
    characters = []
    
    for d in data:
        match d['class']:
            case "Guerreiro":
                p = Warrior(d['id'], d['name'])
            case "Mago":
                p = Mage(d['id'], d['name'])
            case "Arqueiro":
                p = Archer(d['id'], d['name'])
            case _:
                print(f"Classe desconhecida: {d['class']}, pulando.")
                continue

        p.level = d['level']
        p.hp = d['hp']
        p.created_in = d['created_in']

        characters.append(p)

    for c in characters:
        print("\n")
        print(f"{c.id} - {c.name} | Nível {c.level} | HP {c.hp}")
        
    choice = input("\nDigite o ID do personagem que quer upar: ")

    try:
        choice = int(choice)
    except ValueError:
        print("ID inválido.")
        return
    for p in filter(lambda p: p.id == choice, characters):
        p.level_up()
        datas = [p.para_dict() for p in characters]
        character_info_save(datas)
        clean_terminal()
        input("\nLEVEL UP !!!!\n\nAperte enter para voltar.\n\n")
        return

    print("Personagem não encontrado.")
    user_go_by()

def create_character(data):
    name_player = input("Crie um nome para seu personagem: ")
    clean_terminal()
    class_player = input("Agora escolha sua classe: " \
                        "\n1 - Mago" \
                        "\n2 - Guerreiro" \
                        "\n3 - Arqueiro" \
                        "\n\nEscolha: ").upper()

    player = class_choice(data, class_player, name_player)
    data = load_characters()

    add_new_character(data, player.name, player.classe)

def random_class():
    random_choice = random.choice(classes)
    return random_choice

def class_choice(data, info, name_player):
    new_id = len(data) + 1
    match info:
        case "1" | "MAGO":
            _class = Mage(new_id, name_player)
            _class.initial_text()
            time.sleep(2)
            return _class
        case "2" | "GUERREIRO":
            _class = Warrior(new_id, name_player)
            _class.initial_text()
            time.sleep(2)
            return _class
        case "3" | "ARQUEIRO":
            _class = Archer(new_id, name_player)
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
            create_character(data)
            return True
        case "3" | "SUBIR":
            character_level_up(data)
            return True
        case "4" | "FILTRAR":
            filter_characters_per_class(data)
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
    create_character(data)

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