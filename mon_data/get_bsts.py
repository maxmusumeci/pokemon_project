import csv

print("Pokemon BSTs")

mon_effective_stat= []
global atk
global spa
i = 0

# newmons = [
#             [1011, "Dipplin"," ", "Grass", "Dragon", 485, 80, 80, 110, 95, 80, 40, 9],
#             [1012, "Poltchageist"," ", "Grass", "Ghost", 308, 40, 45, 45, 74, 54, 50, 9],
#             [1013, "Sinistcha"," ", "Grass", "Ghost", 508, 71, 60, 106, 121, 80, 70, 9],
#             [1014, "Okidogi"," ", "Poison", "Fighting", 555, 88, 128, 115, 58, 86, 80, 9],
#             [1015, "Munkidori"," ", "Poision", "Psychic", 555, 88, 75, 66, 130, 90, 106, 9],
#             [1016, "Fezandipiti"," ", "Poison", "Fairy", 555, 88, 91, 82, 70, 125, 99, 9],
#             [1017, "Ogerpon", "Teal Mask", "Grass"," ", 550, 80, 120, 84, 60, 96, 110, 9],
#             [1017, "Ogerpon", "Wellspring Mask", "Grass", "Water", 550, 80, 120, 84, 60, 96, 110, 9],
#             [1017, "Ogerpon", "Hearthflame Mask", "Grass", "Fire", 550, 80, 120, 84, 60, 96, 110, 9],
#             [1017, "Ogerpon", "Cornerstone Mask", "Grass", "Rock", 550, 80, 120, 84, 60, 96, 110, 9],
#             [1018, "Archaludon"," ", "Steel", "Dragon", 600, 90, 105, 130, 125, 65, 85, 9],
#             [1019, "Hydrapple"," ", "Grass", "Dragon", 540, 106, 80, 110, 120, 80, 44, 9],
#             [1020, "Gouging Fire"," ", "Fire", "Dragon", 590, 105, 115, 121, 65, 93, 91, 9],
#             [1021, "Raging Bolt"," ", "Electric", "Dragon", 590, 125, 73, 91, 137, 89, 75, 9],
#             [1022, "Iron Boulder"," ", "Rock", "Psychic", 590, 90, 120, 80, 68, 108, 124, 9],
#             [1023, "Iron Crown"," ", "Steel", "Psychic", 590, 90, 72, 100, 122, 108, 98, 9],
#             [1024, "Terapagos", "Normal Form", "Normal"," ", 450, 90, 65, 85, 65, 85, 60, 9],
#             [1024, "Terapagos", "Terastal Form", "Normal"," ", 600, 95, 95, 110, 105, 110, 85, 9],
#             [1024, "Terapagos", "Stellar Form", "Stellar"," ", 700, 160, 105, 110, 130, 110, 85, 9],
#             [1025, "Pecharunt"," ", "Poison", "Ghost", 600, 88, 88, 160, 88, 88, 88, 9]
#             ]

# with open('pokemon.csv', 'w', newline='') as csvfile:
#     csvwriter = csv.writer(csvfile)
#     csvwriter.writerows(newmons)
    
with open('pokemon.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        try:
            atk = int(row[7])
            spa = int(row[9])
            lower_stat = min(atk, spa)
            bst = (int)(row[5])
            mon_effective_stat.append((row[1] + " " + row[2], bst - lower_stat))
            #print(row[1], row[2], effective_stat[i])
            i += 1
        except:
            print("start")

sorted_stats = sorted(mon_effective_stat, key=lambda x: x[1])


for name, stats in sorted_stats:
    print(f"{name}, {stats}")
