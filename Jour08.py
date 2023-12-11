import math

# liste = open('Puzzles/Network_test').read()
# liste = open('Puzzles/Network_test_bis').read()
liste = open('Puzzles/Network').read()
liste = liste.split('\n')


liste_left_right = list(liste[0])
print(liste_left_right)


dictionary_network = dict()
for i in range(2, len(liste)):
    current_network = liste[i].split('=')
    dictionary_network[current_network[0][0:3]] = [current_network[1][2:5], current_network[1][7:10]]


print(dictionary_network)


####################################################################################################################
# 1ème Partie ######################################################################################################
####################################################################################################################


def read_network(current_left_right, nb_of_steps, current_item, end_item, nb_of_letters_not_same):
    if current_left_right == 'L':
        current_item = dictionary_network[current_item][0]
        nb_of_steps += 1
        if current_item[nb_of_letters_not_same:] == end_item:
            return [nb_of_steps, current_item]
    else:
        current_item = dictionary_network[current_item][1]
        nb_of_steps += 1
        if current_item[nb_of_letters_not_same:] == end_item:
            return [nb_of_steps, current_item]
    return [nb_of_steps, current_item]


def read_all(start_item, end_item, nb_of_letters_not_same):
    current_item = start_item
    nb_of_steps = 0
    while current_item[nb_of_letters_not_same:] != end_item:
        for current_left_right in liste_left_right:
            [nb_of_steps, current_item] = read_network(current_left_right, nb_of_steps, current_item, end_item, nb_of_letters_not_same)
    return nb_of_steps


print('The number of steps is', read_all('AAA', 'ZZZ', 0))


####################################################################################################################
# 2ème Partie ######################################################################################################
####################################################################################################################


# liste = open('Puzzles/Network_part2_test').read()
liste = open('Puzzles/Network').read()
liste = liste.split('\n')


liste_left_right = list(liste[0])
print(liste_left_right)


dictionary_network = dict()
for i in range(2, len(liste)):
    current_network = liste[i].split('=')
    dictionary_network[current_network[0][0:3]] = [current_network[1][2:5], current_network[1][7:10]]


print(dictionary_network)


def find_start():
    liste_start_item = []
    for item in dictionary_network.keys():
        if item[-1] == 'A':
            liste_start_item.append(item)
    return liste_start_item


def read_simultaneously():
    liste_start_item = find_start()
    liste_nb_of_steps = []
    for start_item in liste_start_item:
        current_nb_of_step = read_all(start_item, 'Z', 2)
        print(start_item, current_nb_of_step)
        liste_nb_of_steps.append(current_nb_of_step)
    return math.lcm(*liste_nb_of_steps)


print(read_simultaneously())
