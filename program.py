import datetime, time
import os, sys

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

class Warrior(Character):
    hp_per_nivel = 10
    initial_hp = 100

    def __init__(self, nome):
        super().__init__(nome)
        self.hp = self.initial_hp

class Archer(Character):
    hp_per_nivel = 8
    initial_hp = 80

    def __init__(self, nome):
        super().__init__(nome)
        self.hp = self.initial_hp

nome_player = input("Bem vindo ao RPG!\n\nCrie um nome para começar: ")
classe_player = input("Agora escolha sua classe: " \
                    "\n1 - Mago" \
                    "\n2 - Guerreiro" \
                    "\n3 - Arqueiro").upper()

def class_choose(info):
    match info:
        case "1" | "MAGO":
            return Mage(nome_player)
        case "2" | "GUERREIRO":
            return Warrior(nome_player)
        case "3" | "ARQUEIRO":
            return Archer(nome_player)
        case _:
            print("Nenhuma classe foi escolhida")
            return 0

player = class_choose(classe_player)