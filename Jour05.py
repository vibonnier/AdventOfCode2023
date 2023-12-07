# liste = open('Puzzles/Almanac_test').read()
liste = open('Puzzles/Almanac').read()
liste = liste.split()
print(liste)


liste_seeds = []
i = 1
while liste[i].isdigit():
    liste_seeds.append(int(liste[i]))
    i += 1


def fill_liste(list, name_in_liste):
    i = liste.index(name_in_liste) + 2
    while i < len(liste) and liste[i].isdigit():
        list.append(int(liste[i]))
        i += 1
    return list


liste_seed_to_soil = []
liste_soil_to_fertilizer = []
liste_fertilizer_to_water = []
liste_water_to_light = []
liste_light_to_temperature = []
liste_temperature_to_humidity = []
liste_humidity_to_location = []


fill_liste(liste_seed_to_soil, 'seed-to-soil')
fill_liste(liste_soil_to_fertilizer, 'soil-to-fertilizer')
fill_liste(liste_fertilizer_to_water, 'fertilizer-to-water')
fill_liste(liste_water_to_light, 'water-to-light')
fill_liste(liste_light_to_temperature, 'light-to-temperature')
fill_liste(liste_temperature_to_humidity, 'temperature-to-humidity')
fill_liste(liste_humidity_to_location, 'humidity-to-location')


print('seeds', liste_seeds)


####################################################################################################################
# 1ème Partie ######################################################################################################
####################################################################################################################


def is_in_length(start_nb, associated_start_nb, length, nb_to_check):
    if start_nb <= nb_to_check < start_nb + length:
        return associated_start_nb + nb_to_check - start_nb


def check_all_length(list, nb_to_check):
    for id_length in range(2, len(list), 3):
        current_length = int(list[id_length])
        start_nb = int(list[id_length - 1])
        associated_start_nb = int(list[id_length - 2])
        new_nb_to_check = is_in_length(start_nb, associated_start_nb, current_length, nb_to_check)
        if new_nb_to_check is not None:
            return new_nb_to_check
    return nb_to_check


def transforme_seed_into_location(seed):
    soil = check_all_length(liste_seed_to_soil, seed)
    fertilizer = check_all_length(liste_soil_to_fertilizer, soil)
    water = check_all_length(liste_fertilizer_to_water, fertilizer)
    light = check_all_length(liste_water_to_light, water)
    temperature = check_all_length(liste_light_to_temperature, light)
    humidity = check_all_length(liste_temperature_to_humidity, temperature)
    location = check_all_length(liste_humidity_to_location, humidity)
    return location


liste_location = []
for seed in liste_seeds:
    location = transforme_seed_into_location(seed)
    liste_location.append(location)


print('The lowest location number is', min(liste_location))


####################################################################################################################
# 2ème Partie ######################################################################################################
####################################################################################################################


# In order to gain speed, check not all the seeds but every 10'000.
# This gives an approximation min location and the associated seed.
step = 10000
liste_min_location_seed = [float('inf'), float('inf')]
for id_start_seed in range(0, len(liste_seeds), 2):
    for current_length in range(0, liste_seeds[id_start_seed + 1], step):
        current_seed = liste_seeds[id_start_seed] + current_length
        current_location = transforme_seed_into_location(current_seed)
        if current_location < liste_min_location_seed[0]:
            liste_min_location_seed = [current_location, current_seed]
print('Step', step, ', approximation min location', liste_min_location_seed[0], ', approximation associated seed', liste_min_location_seed[1])


# The associated seed of the true answer is near the approximation associated seed (around 10'000).
start_seed = liste_min_location_seed[1]
for i in range(-step, step):
    current_seed = start_seed + i
    current_location = transforme_seed_into_location(current_seed)
    if current_location < liste_min_location_seed[0]:
        liste_min_location_seed = [current_location, current_seed]
print('True min location', liste_min_location_seed[0], ', true associated seed', liste_min_location_seed[1])

print('The new lowest location number is', liste_min_location_seed[0])
