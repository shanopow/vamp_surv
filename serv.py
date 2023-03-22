# file
from obs import *
# module
import json
import copy

# json reader
def file_reader(file_name):
    f = open(file_name)
    raw_data = json.load(f)
    f.close()
    return raw_data

# for converting name of class in str to actual class, used in normal object builder, DO NOT USE ALONE
def get_class(kls):
    parts = kls.split('.')
    module = ".".join(parts[:-1])
    m = __import__(module)
    for comp in parts[1:]:
        m = getattr(m, comp)          
    return m

# makes big list of all objects of same class
def object_builder(data, class_type, keyword):
    D = get_class(class_type)
    big = []
    for each in data:
        if each == keyword:
            big = [D(data[keyword][each]) for each in data[keyword]]
    return big

def final_object_builder(mashed_list, count):
    final_dict = {}
    for item in mashed_list:
        final_dict[count] = item
        count += 1
    return final_dict



# work done inside the  main while loop
def input_taker():
    stuck = True
    while stuck:
        print("Enter a map:")
        chose = input()
        stuck = False
    print("You selected:", chose)
    return chose



json_blob = file_reader("items.json")
weapons = object_builder(json_blob, "__main__.Weapon", "Weapon") 
items = object_builder(json_blob, "__main__.Item", "Item")
unions = object_builder(json_blob, "__main__.Union", "Union")
evolves = object_builder(json_blob, "__main__.Evolve", "Evolve")

count = 1;
final_dict = final_object_builder(weapons + items + unions + evolves, count)
banned = ["Crimson Shroud", "Infinite Corridor", "Silver Ring", "Gold Ring", "Metaglio Left", "Metaglio Right"]
# main loop
while True:
    final = Loadout()
    chose = input_taker()
    final.extra_weapon =  [item for item in weapons if chose in item.locations and item.name not in banned]
    final.extra_item = [item for item in items if chose in item.locations and item.name not in banned]

    # always get the corrosponding items for these weapons on the map
    for finder in final.extra_weapon + final.extra_item:
        # find any evolutions that use this weapon / armour
        for each in evolves + unions:
            if (finder.name in each.weapon) or (finder.name in each.item) and (each not in final.base_evolves):
                final.base_evolves.append(each)
                # get all the other items associated with this evolve / union and add to the their weapon and item lists
                final.loadout_filler(finder, each)
    
    
    
    print("ITEMS:")
    for item in final.base_item:
        print(item)
    print("\nWEAPONS:")
    for item in final.base_weapon:
        print(item)
    quit()