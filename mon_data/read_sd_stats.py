import os
import json



curPath = os.getcwd()
jsonPath = curPath + "/jsons/may2024/gen9vgc2024reggbo3-1760.json"


f = open(jsonPath)

data = json.load(f)

#print(data)

for pokemon, info in data['data'].items():
    #print(pokemon, info)
    print(pokemon)
    for category, stats in info.items():
        print(category)
        if (type(stats)) is dict:
            for name, vals in stats.items():
                print(name, vals)

        elif (type(stats) is list):
            for val in stats:
                print(val)
        else:
            print(stats)
    

f.close()

