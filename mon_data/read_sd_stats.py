import os
import json

def float_sort(mv):
    return mv[1]


def list_top_50():

    top50 = []

    curPath = os.getcwd()
    jsonPath = curPath + "/jsons/may2024/gen9vgc2024reggbo3-1760.json"

    f = open(jsonPath)

    data = json.load(f)

    for pokemon, info in data['data'].items():
        for category, stats in info.items():
            if (category == "Happiness"):
                for k, val in stats.items():
                    top50.append((pokemon, val))

    top50.sort(reverse=True, key=float_sort)


    f.close()
    del top50[50:]

    return top50



def make_mon_file(name, date, elo, total_usage):
    moves = []
    items = []
    abilities = []
    spreads = []
    
    path = os.getcwd() + "/sd_stats/"
    name = name.replace(" ", "_")

    with open(path + f"{name}_{date}_{elo}.txt", "w") as pkmn_file:

        result = find_pokemon_stats(name, moves, items, abilities, spreads)
        if (result == False):
            return result


        moves.sort(reverse=True, key=float_sort)
        items.sort(reverse=True, key=float_sort)
        abilities.sort(reverse=True, key=float_sort)
        spreads.sort(reverse=True, key=float_sort)


        for elem, usage in moves[:14]:
            pkmn_file.write(f"{elem}, {(usage / total_usage) * 100}%\n")

        pkmn_file.write("\n")

        for elem, usage in items[:5]:
            pkmn_file.write(f"{elem}, {(usage / total_usage) * 100}%\n")

        pkmn_file.write("\n")

        for elem, usage in abilities[:3]:
            pkmn_file.write(f"{elem}, {(usage / total_usage) * 100}%\n")

        pkmn_file.write("\n")

        for elem, usage in spreads[:9]:
            pkmn_file.write(f"{elem}, {(usage / total_usage) * 100}%\n")

        pkmn_file.write("\n")

        #pkmn_file.write([x[0] for x in moves[:14]])
        #pkmn_file.write([x[0] for x in items[:5]])
        #pkmn_file.write([x[0] for x in abilities[:3]])
        #pkmn_file.write([x[0] for x in spreads[:9]])

    pkmn_file.close()

    return result


def find_pokemon_stats(mon_name, moves, items, abilities, spreads):

    curPath = os.getcwd()
    jsonPath = curPath + "/jsons/may2024/gen9vgc2024reggbo3-1760.json"

    f = open(jsonPath)

    data = json.load(f)

    found = False
    flag = ""

    for pokemon, info in data['data'].items():
        if (pokemon == mon_name):
            found = True

            for category, stats in info.items():
                flag = category
                if (type(stats)) is dict:
                    for name, vals in stats.items():
                        if (flag == "Items"):
                            items.append((name, vals))
                        elif (flag == "Moves"):
                            moves.append((name, vals))

                        elif (flag == "Abilities"):
                            abilities.append((name, vals))

                        elif (flag == "Spreads"):
                            spreads.append((name, vals))

                elif (type(stats) is list):
                    for val in stats:
                        pass
                else:
                    pass

        if (found):
            return found
    
    f.close()
    return found


#input_mon = input("What pokemon's stats would you like to find?: ")

#moves = []
#items = []
#abilities = []
#spreads = []


#found = find_pokemon_stats(input_mon)

#if (found == False):
#    print("Pokemon not found")
#    exit(0)
    
#moves.sort(reverse=True, key=float_sort)
#items.sort(reverse=True, key=float_sort)
#abilities.sort(reverse=True, key=float_sort)
#spreads.sort(reverse=True, key=float_sort)
#
#print([x[0] for x in moves[:6]])
#print([x[0] for x in items[:6]])
#print([x[0] for x in abilities[:6]])
#print([x[0] for x in spreads[:6]])
#


top50 = list_top_50()

for pokemon, usage in top50:
    make_mon_file(pokemon, "05_24", "1760", usage)
    

#print([x[0] for x in top50])

