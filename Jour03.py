# liste = open('Puzzles/Schematic_test').read()
liste = open('Puzzles/Schematic').read()
liste = liste.split()
print(liste)


def find_nb():
    liste_digits = []
    current_digit = []
    for id_line in range(len(liste)):
        for id_column in range(len(liste[id_line])):
            if liste[id_line][id_column].isdigit():
                current_digit.append(liste[id_line][id_column])
            else:
                liste_digits.append(current_digit)
                current_digit = []
        liste_digits.append(current_digit)
        current_digit = []
    return liste_digits


def lisser(list):
    new_list = []
    for i in range(len(list)):
        if list[i]:
            new_list.append("".join(list[i]))
    return new_list


liste_digits = lisser(find_nb())
print(liste_digits)


####################################################################################################################
# 1ème Partie ######################################################################################################
####################################################################################################################


def check_left_right(id_line, start_id_column, end_id_column):
    if start_id_column != 0 and liste[id_line][start_id_column - 1] != '.':
        return False
    elif end_id_column != len(liste[id_line]) - 1 and liste[id_line][end_id_column + 1] != '.':
        return False
    else:
        return True


# check les diagonales aussi
def check_head_bottom(id_line, start_id_column, end_id_column):
    if start_id_column != 0:
        current_id_column = start_id_column - 1
    else:
        current_id_column = start_id_column
    while current_id_column < min(end_id_column + 2, len(liste[id_line])):
        if id_line != 0 and liste[id_line - 1][current_id_column] != '.':
            return False
        elif id_line != len(liste) - 1 and liste[id_line + 1][current_id_column] != '.':
            return False
        current_id_column += 1
    return True


def check_symbols():
    liste_digits_without_symbols = []
    for id_line in range(len(liste)):
        id_column = 0
        while id_column < len(liste[id_line]):
            if liste[id_line][id_column].isdigit():
                start_id_column = id_column
                end_id_column = id_column + len(liste_digits[0]) - 1
                if check_head_bottom(id_line, start_id_column, end_id_column) and check_left_right(id_line, start_id_column, end_id_column):
                    liste_digits_without_symbols.append(int(liste_digits[0]))
                id_column = end_id_column
                liste_digits.pop(0)
            id_column += 1
    return liste_digits_without_symbols


def sum_total():
    sum = 0
    for i in range(len(liste_digits)):
        sum += int(liste_digits[i])
    return sum


print('The sum of all the part numbers in the engine schematic is', sum_total() - sum(check_symbols()))


####################################################################################################################
# 2ème Partie ######################################################################################################
####################################################################################################################


liste_digits = lisser(find_nb())
print(liste_digits)


dico_stars_nb_digits_around = dict()
dico_stars_sum = dict()
for id_line in range(len(liste)):
    for id_column in range(len(liste[id_line])):
        if liste[id_line][id_column] == '*':
            dico_stars_nb_digits_around[str(id_line) + '_' + str(id_column)] = 0
            dico_stars_sum[str(id_line) + '_' + str(id_column)] = 1

print(dico_stars_nb_digits_around)


def check_left(id_line, start_id_column, current_nb):
    if start_id_column != 0 and liste[id_line][start_id_column - 1] == '*':
        dico_stars_nb_digits_around[str(id_line) + '_' + str(start_id_column - 1)] += 1
        dico_stars_sum[str(id_line) + '_' + str(start_id_column - 1)] *= int(current_nb)


def check_right(id_line, end_id_column, current_nb):
    if end_id_column != len(liste[id_line]) - 1 and liste[id_line][end_id_column + 1] == '*':
        dico_stars_nb_digits_around[str(id_line) + '_' + str(end_id_column + 1)] += 1
        dico_stars_sum[str(id_line) + '_' + str(end_id_column + 1)] *= int(current_nb)


# check les diagonales aussi
def check_head(id_line, start_id_column, end_id_column, current_nb):
    if start_id_column != 0:
        current_id_column = start_id_column - 1
    else:
        current_id_column = start_id_column
    while current_id_column < min(end_id_column + 2, len(liste[id_line])):
        if id_line != 0 and liste[id_line - 1][current_id_column] == '*':
            dico_stars_nb_digits_around[str(id_line - 1) + '_' + str(current_id_column)] += 1
            dico_stars_sum[str(id_line - 1) + '_' + str(current_id_column)] *= int(current_nb)
        current_id_column += 1


# check les diagonales aussi
def check_bottom(id_line, start_id_column, end_id_column, current_nb):
    if start_id_column != 0:
        current_id_column = start_id_column - 1
    else:
        current_id_column = start_id_column
    while current_id_column < min(end_id_column + 2, len(liste[id_line])):
        if id_line != len(liste) - 1 and liste[id_line + 1][current_id_column] == '*':
            dico_stars_nb_digits_around[str(id_line + 1) + '_' + str(current_id_column)] += 1
            dico_stars_sum[str(id_line + 1) + '_' + str(current_id_column)] *= int(current_nb)
        current_id_column += 1


def check_symbols_bis():
    for id_line in range(len(liste)):
        id_column = 0
        while id_column < len(liste[id_line]):
            if liste[id_line][id_column].isdigit():
                start_id_column = id_column
                current_nb = liste_digits[0]
                end_id_column = id_column + len(current_nb) - 1
                check_bottom(id_line, start_id_column, end_id_column, current_nb)
                check_head(id_line, start_id_column, end_id_column, current_nb)
                check_right(id_line, end_id_column, current_nb)
                check_left(id_line, start_id_column, current_nb)
                id_column = end_id_column
                liste_digits.pop(0)
            id_column += 1


def find_right_stars():
    liste_right_stars = []
    for item in dico_stars_nb_digits_around:
        if dico_stars_nb_digits_around[item] == 2:
            liste_right_stars.append(dico_stars_sum[item])
    return liste_right_stars


check_symbols_bis()
print('the sum of all of the gear ratios in your engine schematic', sum(find_right_stars()))