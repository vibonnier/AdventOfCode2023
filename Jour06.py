# liste = open('Puzzles/Race_test').read()
liste = open('Puzzles/Race').read()
liste = liste.split()
print(liste)


def create_liste_time():
    liste_time = []
    i = 1
    while liste[i] != 'Distance:':
        liste_time.append(int(liste[i]))
        i += 1
    return liste_time


def create_liste_distance():
    liste_distance = []
    i = liste.index('Distance:') + 1
    while i < len(liste):
        liste_distance.append(int(liste[i]))
        i += 1
    return liste_distance


liste_time = create_liste_time()
liste_distance = create_liste_distance()


print('Time', liste_time)
print('Distance', liste_distance)


####################################################################################################################
# 1ème Partie ######################################################################################################
####################################################################################################################


def way_to_win(time, record_distance):
    for time_holding_button in range(time):
        time_moving = time - time_holding_button
        distance_reached = time_moving * time_holding_button
        if distance_reached > record_distance:
            return time + 1 - 2 * time_holding_button


product = 1
for id_race in range(len(liste_time)):
    product *= way_to_win(liste_time[id_race], liste_distance[id_race])
print('The answer is', product)


####################################################################################################################
# 2ème Partie ######################################################################################################
####################################################################################################################


Time = "".join(map(str, liste_time))
Distance = "".join(map(str, liste_distance))


print('New Time:', Time)
print('New Distance:', Distance)


print('The numbers of ways which can beat the record is', way_to_win(int(Time), int(Distance)))





