# 248133033  and 248052388 too low

# liste = open('Puzzles/CamelGame_test').read()
liste = open('Puzzles/CamelGame').read()
liste = liste.split()
print(liste)

liste_hand = []
dictionary_nb_associated = dict()
for i in range(0, len(liste), 2):
    liste_hand.append(liste[i])
    dictionary_nb_associated[liste[i]] = int(liste[i + 1])

print('Liste of hands', liste_hand)
print('Dictionary of nb associated', dictionary_nb_associated)


####################################################################################################################
# 1ème Partie ######################################################################################################
####################################################################################################################


dictionary_strength = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}


def order_by_nb_cards_different(hand):
    dictionary_per_hand = dict()
    for card in hand:
        if card in dictionary_per_hand:
            dictionary_per_hand[card] += 1
        else:
            dictionary_per_hand[card] = 1
    return dictionary_per_hand


def order_hand_by_type():
    dictionary_by_type = dict()
    for hand in liste_hand:
        dictionary_by_type[hand] = 10 * (5 - len(order_by_nb_cards_different(hand).values())) + max(order_by_nb_cards_different(hand).values())
    return dictionary_by_type


def order_hand_by_strength():
    dictionary_by_strength = dict()
    for hand in liste_hand:
        dictionary_by_strength[hand] = 100000000 * dictionary_strength[hand[0]] + 1000000 * dictionary_strength[hand[1]] \
                                       + 10000 * dictionary_strength[hand[2]] + 100 * dictionary_strength[hand[3]] + dictionary_strength[hand[4]]
    return dictionary_by_strength


def order_hand_total():
    dictionary_by_strength = order_hand_by_strength()
    dictionary_by_type = order_hand_by_type()
    dictionary_total = dict()
    new_dictionary_total = dict()
    for hand in liste_hand:
        dictionary_total[hand] = 10000000000 * dictionary_by_type[hand] + dictionary_by_strength[hand]
    rank = 1
    while dictionary_total:
        min_key = min(dictionary_total, key=dictionary_total.get)
        new_dictionary_total[min_key] = rank
        rank += 1
        del dictionary_total[min_key]
    return new_dictionary_total


def count():
    dictionary_ordered = order_hand_total()
    sum = 0
    for hand in liste_hand:
        sum += dictionary_ordered[hand] * dictionary_nb_associated[hand]
    return sum


print(order_hand_total())
print('The total of winnings is', count())


####################################################################################################################
# 2ème Partie ######################################################################################################
####################################################################################################################


dictionary_strength_bis = {'J': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'Q': 11, 'K': 12, 'A': 13}


def order_by_nb_cards_different_bis(hand):
    dictionary_per_hand = dict()
    nb_of_J = 0
    for card in hand:
        if card in dictionary_per_hand and card != 'J':
            dictionary_per_hand[card] += 1
        elif card not in dictionary_per_hand and card != 'J':
            dictionary_per_hand[card] = 1
        else:
            nb_of_J += 1
    if hand == 'JJJJJ':
        dictionary_per_hand['A'] = 5
    else:
        max_key = max(dictionary_per_hand, key=dictionary_per_hand.get)
        dictionary_per_hand[max_key] += nb_of_J
    return dictionary_per_hand


def order_hand_by_type_bis():
    dictionary_by_type = dict()
    for hand in liste_hand:
        dictionary_by_type[hand] = 10 * (5 - len(order_by_nb_cards_different_bis(hand).values())) + max(order_by_nb_cards_different_bis(hand).values())
    return dictionary_by_type


def order_hand_by_strength_bis():
    dictionary_by_strength = dict()
    for hand in liste_hand:
        dictionary_by_strength[hand] = 100000000 * dictionary_strength_bis[hand[0]] + 1000000 * dictionary_strength_bis[hand[1]] \
                                       + 10000 * dictionary_strength_bis[hand[2]] + 100 * dictionary_strength_bis[hand[3]] + dictionary_strength_bis[hand[4]]
    return dictionary_by_strength


def order_hand_total_bis():
    dictionary_by_strength = order_hand_by_strength_bis()
    dictionary_by_type = order_hand_by_type_bis()
    dictionary_total = dict()
    new_dictionary_total = dict()
    for hand in liste_hand:
        dictionary_total[hand] = 10000000000 * dictionary_by_type[hand] + dictionary_by_strength[hand]
    rank = 1
    while dictionary_total:
        min_key = min(dictionary_total, key=dictionary_total.get)
        new_dictionary_total[min_key] = rank
        rank += 1
        del dictionary_total[min_key]
    return new_dictionary_total


def count_bis():
    dictionary_ordered = order_hand_total_bis()
    sum = 0
    for hand in liste_hand:
        sum += dictionary_ordered[hand] * dictionary_nb_associated[hand]
    return sum


print(order_hand_total_bis())
print('The new total of winnings is', count_bis())




"""
import sys
import re
from collections import defaultdict, Counter
D = open("Puzzles/CamelGame").read().strip()
L = D.split('\n')

def strength(hand, part2):
  hand = hand.replace('T',chr(ord('9')+1))
  hand = hand.replace('J',chr(ord('2')-1) if part2 else chr(ord('9')+2))
  hand = hand.replace('Q',chr(ord('9')+3))
  hand = hand.replace('K',chr(ord('9')+4))
  hand = hand.replace('A',chr(ord('9')+5))

  C = Counter(hand)
  if part2:
    target = list(C.keys())[0]
    for k in C:
      if k!='1':
        if C[k] > C[target] or target=='1':
          target = k
    assert target != '1' or list(C.keys()) == ['1']
    if '1' in C and target != '1':
      C[target] += C['1']
      del C['1']
    assert '1' not in C or list(C.keys()) == ['1'], f'{C} {hand}'

  if sorted(C.values()) == [5]:
    return (10, hand)
  elif sorted(C.values()) == [1,4]:
    return (9, hand)
  elif sorted(C.values()) == [2,3]:
    return (8, hand)
  elif sorted(C.values()) == [1,1,3]:
    return (7, hand)
  elif sorted(C.values()) == [1,2,2]:
    return (6, hand)
  elif sorted(C.values()) == [1,1,1,2]:
    return (5, hand)
  elif sorted(C.values()) == [1,1,1,1,1]:
    return (4, hand)
  else:
    assert False, f'{C} {hand} {sorted(C.values())}'

for part2 in [False, True]:
  H = []
  for line in L:
    hand,bid = line.split()
    H.append((hand,bid))
  H = sorted(H, key=lambda hb:strength(hb[0], part2))
  ans = 0
  for i,(h,b) in enumerate(H):
    if i+1 != order_hand_total_bis()[h]:
        print(i,h,b,'mine', order_hand_total_bis()[h])
    ans += (i+1)*int(b)
  print(ans)

"""