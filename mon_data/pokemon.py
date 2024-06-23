from poketypes import Poketype
import nature
#import abilities
#import moves
#import items

class Stats:
    total: int
    hp: int
    atk: int
    dfn: int
    spa: int
    spd: int
    spe: int

    def __init__(self, total, hp, atk, dfn, spa, spd, spe):
        self.total = total
        self.hp = hp
        self.atk = atk
        self.dfn = dfn
        self.spa = spa
        self.spd = spd
        self.spe = spe

    def __str__(self):
        return f"{self.total}, {self.hp}, {self.atk}, {self.dfn}, {self.spa}, {self.spd}, {self.spe}"



class Pokemon:
    dexid: int
    name: str
    form: str #enum of str? blank for now, str sounds good tho 
    type1: Poketype
    type2: Poketype 
    base_stats: Stats
    # from here on out these are distinguished features

    def __init__(self, dexid, name, form, type1, type2, base_stats):
        self.dexid = dexid
        self.name = name

        if (form == ' '):
            self.form = 'None'
        else:
            self.form = form

        self.type1 = Poketype[type1.upper()]

        #print(type2)
        
        if (type2 == " " or type2 == ""):
            self.type2 = Poketype['NONE']
        else:
            self.type2 = Poketype[type2.upper()]

        self.base_stats = base_stats

"""
class Set:
    pokemon: Pokemon
    level: int
    evs: Stats
    ivs: Stats
    item: Item # could be string
    moves: Move # could be string, but needs to be one to four
    nature: Nature
    tera_type: Poketype
    ability: Ability # could be string

"""
