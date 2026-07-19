from datetime import datetime
import utils

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
        utils.clean_terminal()
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
        utils.clean_terminal()
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
        utils.clean_terminal()
        print(f"{self.name} é reconhecido como um valioso ARQUEIRO.")

