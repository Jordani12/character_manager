from datetime import datetime
import os, sys, random, time, json

FOLDER = os.path.dirname(os.path.abspath(__file__))
CHARACTER_DATA = os.path.join(FOLDER, "characters.json")

# --------------------------------------------------------------
# Auxiliar functions
# --------------------------------------------------------------

def clean_terminal():
    os.system('cls')

# --------------------------------------------------------------
# Class Heritage
# --------------------------------------------------------------


class Character:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.hp = 0
        self.classe = None
    
    def level_up(self):
        self.level += 1
        self.hp += self.hp_per_nivel
        print(f"{self.name} subiu para o nível {self.level}! HP: {self.hp}")

class Mage(Character):
    hp_per_nivel = 5
    initial_hp = 60
    _classe = "Mago"

    def __init__(self, nome):
        super().__init__(nome)
        self.hp = self.initial_hp
        self.classe = self._classe

    def initial_text(self):
        print(f"{self.name} é reconhecido como um grande MAGO.")


class Warrior(Character):
    hp_per_level = 10
    initial_hp = 100
    _classe = "Guerreiro"

    def __init__(self, nome):
        super().__init__(nome)
        self.hp = self.initial_hp
        self.classe = self._classe

    def initial_text(self):
        print(f"{self.name} é reconhecido como um honrado GUERREIRO.")

class Archer(Character):
    hp_per_nivel = 8
    initial_hp = 80
    _classe = "Arqueiro"

    def __init__(self, nome):
        super().__init__(nome)
        self.hp = self.initial_hp
        self.classe = self._classe
    
    def initial_text(self):
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

def add_new_character(data, name, classe, hp, level, date):
    novo_ranking ={"id": len(data) + 1, 
                   "nome": name, 
                   "class": classe, 
                   "hp": hp,
                    "level": level,
                    "created_in": date
                   }
    data.append(novo_ranking)
    character_info_save(data)

def show_characters(data):
    for c in data:
        date_from_json = datetime.fromisoformat(c['created_in'])
        exibition_date = date_from_json.strftime("%d/%m/%Y %H:%M")
        print("\n")
        print(f"{c['nome']} na classe {c['class']} está no level {c['level']} com {c['hp']} de HP"
              f"\nFoi criado em {exibition_date}")

def show_characters_alive(data):
    vivos = [c for c in data if c['hp'] > 0]
    for c in vivos:
        print(c['nome'])
    
# --------------------------------------------------------------
# User Interaction
# --------------------------------------------------------------

classes = {Mage, Warrior, Archer}


def create_character():
    name_player = input("Bem vindo ao RPG!\n\nCrie um nome para começar: ")
    class_player = input("Agora escolha sua classe: " \
                        "\n1 - Mago" \
                        "\n2 - Guerreiro" \
                        "\n3 - Arqueiro" \
                        "\n\nEscolha: ").upper()

    player = class_choice(class_player, name_player)
    time_of_creation = datetime.now().isoformat # Salvar a data hora que criou o personagem
    data = load_characters()

    add_new_character(data, player.name, player.classe, player.hp, player.level, time_of_creation)


def random_class():
    random_choice = random.choice(classes)
    return random_choice

def class_choice(info, name_player):
    match info:
        case "1" | "MAGO":
            _class = Mage(name_player)
            _class.initial_text()
            time.sleep(2)
            return _class
        case "2" | "GUERREIRO":
            _class = Warrior(name_player)
            _class.initial_text()
            time.sleep(2)
            return _class
        case "3" | "ARQUEIRO":
            _class = Archer(name_player)
            _class.initial_text()
            time.sleep(2)
            return _class
        case _:
            print("Nenhuma classe foi escolhida." \
            "\nSerá escolhida uma classe aleatória entre as 3.")
            _class = random_class()(name_player)
            _class.initial_text()
            time.sleep(2)
            return _class

def user_choice(info, data):
    match info:
        case "1" | "LISTAR":
            show_characters(data)
        case "2" | "CRIAR":
            create_character()
        #case "3" | "SUBIR":
        #case "4" | "FILTRAR":
        case "5" | "SAIR":
            return False    

clean_terminal()

while True:
    choice = input("1. Listar personagens" \
                "\n2. Criar personagem" \
                "\n3. Subir de nível" \
                "\n4. Filtrar por classe" \
                "\n5. Sair").upper()
    
    data = load_characters()

    user_choice(choice, data)