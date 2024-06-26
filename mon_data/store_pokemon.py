import csv
import os
from pokemon import Pokemon
from pokemon import Stats
from poketypes import Poketype

curPath = os.getcwd()
csvPath =  "/csvs/pokemon.csv"


with open(curPath + csvPath, newline='') as csvfile:
    pokereader = csv.reader(csvfile, delimiter=',')
    header = next(pokereader)
    
    for row in pokereader: 

        if (row[0] == "1024"):
            print(row[1] + " " + row[2])

        mon_data = Pokemon(row[0], row[1], row[2], row[3], row[4],
                    Stats(row[5], row[6], row[7], row[8], 
                          row[9], row[10], row[11]))


#        print(mon_data.dexid, mon_data.name, mon_data.form, mon_data.type1.name, mon_data.type2.name, mon_data.base_stats)

csvfile.close()
