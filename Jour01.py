# liste_part_1 = open('Puzzles/Calibration_test').read()
liste_part_1 = open('Puzzles/Calibration').read()
liste_part_1 = liste_part_1.split()
print(liste_part_1)

# liste_part_2 = open('Puzzles/Calibration_test_bis').read()
liste_part_2 = open('Puzzles/Calibration').read()
liste_part_2 = liste_part_2.split()
print(liste_part_2)


####################################################################################################################
# 1ème Partie ######################################################################################################
####################################################################################################################


def find_all_digits(list):
    list_of_digits = []
    for i in range(len(list)):
        if list[i].isdigit():
            list_of_digits.append(int(list[i]))
    return "".join(map(str, list_of_digits))


def find_two_digits(list):
    all_digits = find_all_digits(list)
    return "".join([all_digits[0], all_digits[-1]])


def add_calibration_values(list):
    compteur = 0
    for i in range(len(list)):
        compteur += int(find_two_digits(list[i]))
    return compteur


print('The sum of all of the calibration values is', add_calibration_values(liste_part_1))


####################################################################################################################
# 2ème Partie ######################################################################################################
####################################################################################################################


words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']


def words_into_nb(list):
    for i in range(len(list)):
        for word in words:
            if word in list[i]:
                list[i] = str(list[i]).replace(word, word[0] + str(words.index(word) + 1) + word[-1])
    return list


print('The new sum of all of the calibration values is', add_calibration_values(words_into_nb(liste_part_2)))
