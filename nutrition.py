
def fda_table_dict(): #dictionary that holds the fruits and calories
    return {
        "apple":130,
        "avocado california":50,
        "banana":110,
        "canteloupe":50,
        "grapefruit":60,
        "grapes":90,
        "honeydew melon":50,
        "kiwi fruit":90,
        "lemon":15,
        "lime":20,
        "nectarine":60,
        "orange":80, 
        "peach":60,
        "pear":100,
        "pineapple":50,
        "plums":70,
        "strawberries":50,
        "sweet cherries":100,
        "tangerine":50,
        "watermelon":80 
    }


    #this function asks user for a fruit name then checks if it is in the dict
    #if so it prints out the calories and if not it stays quiet
def check_calories(fda_table_dict): 
    fruit_name = input("item: ").lower().strip()
    if fruit_name in fda_table_dict:
        print(f"calories: {fda_table_dict[fruit_name]}")
    else:
        print("")



def main():
    fruit_dict = fda_table_dict()
    check_calories(fruit_dict)

if __name__=="__main__":
    main()