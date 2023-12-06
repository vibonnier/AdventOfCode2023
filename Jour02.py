# liste = open('Puzzles/Games_test').read()
liste = open('Puzzles/Games').read()
liste = liste.split('\n')


def lisser():
    new_liste = [[] for _ in range(len(liste))]
    for i in range(len(liste)):
        liste[i] = liste[i][7:]
        liste[i] = liste[i].split(';')
        for j in range(0, len(liste[i])):
            new_liste[i].append(liste[i][j])
    return new_liste


print(lisser())


####################################################################################################################
# 1ème Partie ######################################################################################################
####################################################################################################################


def reveal_possible(color, max_cube_possible, id_game, id_reveal):
    try:
        if int(liste[id_game][id_reveal][liste[id_game][id_reveal].index(color) - 3: liste[id_game][id_reveal].index(color) - 1]) > max_cube_possible:
            print('False')
            return False
        else:
            print('True')
            return True
    except (ValueError, IndexError):
        print('True')
        return True


list_id_game_possible = []
for id_game in range(len(liste)):
    compteur_each_reveal = 0
    for id_reveal in range(len(liste[id_game])):
        print('Game', id_game + 1, 'reveal', id_reveal, liste[id_game][id_reveal])
        if reveal_possible('red', 12, id_game, id_reveal) and reveal_possible('blue', 14, id_game, id_reveal) and reveal_possible('green', 13, id_game, id_reveal):
            compteur_each_reveal += 1
    if compteur_each_reveal == len(liste[id_game]):
        list_id_game_possible.append(id_game + 1)

print('The sum of id of games possibles is', sum(list_id_game_possible))


####################################################################################################################
# 2ème Partie ######################################################################################################
####################################################################################################################

def min_cubes(current_min, color, id_game, id_reveal):
    try:
        if current_min < int(liste[id_game][id_reveal][liste[id_game][id_reveal].index(color) - 3: liste[id_game][id_reveal].index(color) - 1]):
            return int(liste[id_game][id_reveal][liste[id_game][id_reveal].index(color) - 3: liste[id_game][id_reveal].index(color) - 1])
        else:
            return current_min
    except (ValueError, IndexError):
        return current_min


all_power = []
for id_game in range(len(liste)):
    current_min_red = 0
    current_min_blue = 0
    current_min_green = 0
    current_power = 1
    for id_reveal in range(len(liste[id_game])):
        current_min_red = min_cubes(current_min_red, 'red', id_game, id_reveal)
        current_min_blue = min_cubes(current_min_blue, 'blue', id_game, id_reveal)
        current_min_green = min_cubes(current_min_green, 'green', id_game, id_reveal)
    current_power = current_min_red * current_min_blue * current_min_green
    print('Game', id_game + 1, current_power)
    all_power.append(current_power)


print('The sum of id of games possibles is', sum(all_power))
