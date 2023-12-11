# liste = open('Puzzles/Oasis_test').read()
liste = open('Puzzles/Oasis').read()
liste = liste.split('\n')


for i in range(len(liste)):
    liste[i] = liste[i].split(' ')
print(liste)


####################################################################################################################
# 1ème Partie ######################################################################################################
####################################################################################################################


def find_the_differences(list, index_where_add):
    liste_differences = []
    for i in range(len(list) - 1):
        liste_differences.append(int(list[i + 1]) - int(list[i]))
    if all(x == liste_differences[0] for x in liste_differences):
        return int(list[index_where_add]) - pow(-1, index_where_add) * liste_differences[0]
    else:
        return int(list[index_where_add]) - pow(-1, index_where_add) * find_the_differences(liste_differences, index_where_add)


def find_last_nb_of_sequences(index_where_add):
    sum_of_last_nb_of_sequences = 0
    for i in range(len(liste)):
        sum_of_last_nb_of_sequences += find_the_differences(liste[i], index_where_add)
    return sum_of_last_nb_of_sequences


print('The sum of the extrapolated values in last position is', find_last_nb_of_sequences(-1))


####################################################################################################################
# 2ème Partie ######################################################################################################
####################################################################################################################


print('The sum of the extrapolated values in the first position is', find_last_nb_of_sequences(0))
