

# Damage = ((((2 * level)/5 + 2) * base_power * atk_of_atk_mon/def_of_def_mon)/50 + 2) * targets * weather * crit * random * stab * burn * other 


# level is base 50
# weather, typ1, typ2, mv_typ are enums
# atk_typ and def_typ are pairs of enums
# rest are bools or ints

def calc_damage(base_power: int, atk: int, df: int, is_spread: bool, weather,
                is_crit: bool, is_burn: bool, mv_typ, atk_typ, def_typ, 
                atk_mult: int, def_mult: int):

    # make sure to remember random roll 0.85 to 1
    # if this weather amplify move type, else if other move type reduce
    # wthr_mult = 
    # if (burn): burn_mult = 0.5 else burn_mult = 1
    # crit is a bit complicated, but basically take stat differences away
    # atk_mult and def_mult here for now, might just import who base stats for both later

    dmg = ((22 * base_power * (atk/df))/50 + 2) * is_spread * wthr_mult * crit_mult * burn_mult

    return dmg



def main():
    #print("Hello")
    # pull the rest of the data from csv file?
    # make weather 
    



if __name__ == "__main__":
    main()
