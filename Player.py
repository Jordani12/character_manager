from datetime import datetime
import program

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
        program.clean_terminal()
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
        program.clean_terminal()
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
        program.clean_terminal()
        print(f"{self.name} é reconhecido como um valioso ARQUEIRO.")

# --------------------------------------------------------------
# Choice System
# --------------------------------------------------------------

def filter_characters_per_class(data):
    program.clean_terminal()
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
    
    program.clean_terminal()

    for c in filter(lambda c: c['class'] == choice, data):
        print(f"{c['name']} na classe {c['class']} está no level {c['level']} com {c['hp']} de HP"
                f"\nFoi criado em {program.date_from_json(c['created_in'])}")

    program.user_go_by()

def character_level_up(data):
    program.clean_terminal()
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
        program.character_info_save(datas)
        program.clean_terminal()
        input("\nLEVEL UP !!!!\n\nAperte enter para voltar.\n\n")
        return

    print("Personagem não encontrado.")
    program.user_go_by()

def create_character(data):
    name_player = input("Crie um nome para seu personagem: ")
    program.clean_terminal()
    class_player = input("Agora escolha sua classe: " \
                        "\n1 - Mago" \
                        "\n2 - Guerreiro" \
                        "\n3 - Arqueiro" \
                        "\n\nEscolha: ").upper()

    player = program.class_choice(data, class_player, name_player)
    data = program.load_characters()

    program.add_new_character(data, player.name, player.classe)