from random import randint
import utils, Player

def start_match(data, p1id, p2id):
    rounds(data, p1id, p2id)

def damage(classe):

    match classe:
        case "Mago":
            return 30
        case "Arqueiro":
            return 20
        case "Guerreiro":
            dice = randint(0,10)
            if dice >= 5:
                return 50
            return 0

def rounds(data, player1id, player2id):
    import program

    characters = []

    for d in data:
        match d['class']:
            case "Guerreiro":
                p = Player.Warrior(d['id'], d['name'])
            case "Mago":
                p = Player.Mage(d['id'], d['name'])
            case "Arqueiro":
                p = Player.Archer(d['id'], d['name'])
            case _:
                print(f"Classe desconhecida: {d['class']}, pulando.")
                continue

        p.level = d['level']
        p.hp = d['hp']
        p.created_in = d['created_in']

        characters.append(p)

    

    while True:
        print("Deseja prosseguir?")
        try:
            player1id = int(player1id)
        except ValueError:
            print("ID inválido.")
            return
        for p in filter(lambda p: p.id == choice, characters):
            p.level_up()
            datas = [p.para_dict() for p in characters]
            program.character_info_save(datas)
            utils.clean_terminal()
            input(f"\n{p.name} deu {damage} de dano!!!!\n\nAperte enter para avançar.\n\n")
            return

def random_p_start():
    if randint(0, 10) >= 5:
        return 1
    else:
        return 2