import datetime, time
import os, sys
import random

# --------------------------------------------------------------
# Auxiliar functions
# --------------------------------------------------------------

def clean_terminal():
    os.system('cls')

# --------------------------------------------------------------
# Class Heritage
# --------------------------------------------------------------


class Character:
    def __init__(self, nome):
        self.nome = nome
        self.nivel = 1
        self.hp = 0
    
    def level_up(self):
        self.nivel += 1
        self.hp += self.hp_per_nivel
        print(f"{self.nome} subiu para o nível {self.nivel}! HP: {self.hp}")

class Mage(Character):
    hp_per_nivel = 5
    initial_hp = 60

    def __init__(self, nome):
        super().__init__(nome)
        self.hp = self.initial_hp

    def initial_text(self):
        print(f"{self.nome} é reconhecido como um grande MAGO.")

class Warrior(Character):
    hp_per_nivel = 10
    initial_hp = 100

    def __init__(self, nome):
        super().__init__(nome)
        self.hp = self.initial_hp

    def initial_text(self):
        print(f"{self.nome} é reconhecido como um honrado GUERREIRO.")

class Archer(Character):
    hp_per_nivel = 8
    initial_hp = 80

    def __init__(self, nome):
        super().__init__(nome)
        self.hp = self.initial_hp
    
    def initial_text(self):
        print(f"{self.nome} é reconhecido como um valioso ARQUEIRO.")

# --------------------------------------------------------------
# User Interaction
# --------------------------------------------------------------

classes = {Mage, Warrior, Archer}

def random_class():
    random_choice = random.choice(classes)
    return random_choice

def class_choice(info):
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

clean_terminal()

name_player = input("Bem vindo ao RPG!\n\nCrie um nome para começar: ")
class_player = input("Agora escolha sua classe: " \
                    "\n1 - Mago" \
                    "\n2 - Guerreiro" \
                    "\n3 - Arqueiro" \
                    "\n\nEscolha: ").upper()

player = class_choice(class_player)

clean_terminal()

while True:
    choice = input("1. Listar personagens" \
                "\n2. Criar personagem" \
                "\n3. Subir de nível" \
                "\n4. Filtrar por classe" \
                "\n5. Sair").upper()
