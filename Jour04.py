# liste = open('Puzzles/').read()
liste = open('Puzzles/Cards').read()
liste = liste.split('\n')
print(liste)


def find_winner_nb():
    liste_winner_digits = [[] for _ in range(len(liste))]
    current_digit = []
    for id_card in range(len(liste)):
        i = liste[id_card].index(':') + 2
        while liste[id_card][i] != '|':
            if liste[id_card][i].isdigit():
                current_digit.append(liste[id_card][i])
            else:
                liste_winner_digits[id_card].append(current_digit)
                current_digit = []
            i += 1
        liste_winner_digits[id_card].append(current_digit)
        current_digit = []
    return liste_winner_digits


def find_possible_nb():
    liste_possible_digits = [[] for _ in range(len(liste))]
    current_digit = []
    for id_card in range(len(liste)):
        i = liste[id_card].index('|') + 2
        while i < len(liste[id_card]):
            if liste[id_card][i].isdigit():
                current_digit.append(liste[id_card][i])
            else:
                liste_possible_digits[id_card].append(current_digit)
                current_digit = []
            i += 1
        liste_possible_digits[id_card].append(current_digit)
        current_digit = []
    return liste_possible_digits


def lisser(list):
    new_list = [[] for _ in range(len(liste))]
    for id_card in range(len(list)):
        for i in range(len(list[id_card])):
            if list[id_card][i]:
                new_list[id_card].append(int("".join(list[id_card][i])))
    return new_list


liste_winner_nb = lisser(find_winner_nb())
liste_possible_nb = lisser(find_possible_nb())
print(liste_winner_nb)
print(liste_possible_nb)


####################################################################################################################
# 1ème Partie ######################################################################################################
####################################################################################################################


def is_winner():
    liste_nb_of_winners = []
    for id_card in range(len(liste_possible_nb)):
        nb_of_winners = 0
        for id_nb in range(len(liste_possible_nb[id_card])):
            if liste_possible_nb[id_card][id_nb] in liste_winner_nb[id_card]:
                nb_of_winners += 1
        liste_nb_of_winners.append(nb_of_winners)
    return liste_nb_of_winners


def power(list):
    liste_score_per_card = []
    for id_card in range(len(list)):
        if list[id_card] != 0:
            liste_score_per_card.append(pow(2, list[id_card] - 1))
        else:
            liste_score_per_card.append(0)
    return liste_score_per_card


print('The total points is', sum(power(is_winner())))


####################################################################################################################
# 2ème Partie ######################################################################################################
####################################################################################################################

def count_copies():
    liste_nb_of_winners = is_winner()
    liste_nb_of_copies = [1 for _ in range(len(liste))]
    for id_card in range(len(liste)):
        for i in range(liste_nb_of_winners[id_card]):
            multiple = 0
            while multiple < liste_nb_of_copies[id_card]:
                liste_nb_of_copies[id_card + 1 + i] += 1
                multiple += 1
    return liste_nb_of_copies


print('The total scratchcards at the end is', sum(count_copies()))
