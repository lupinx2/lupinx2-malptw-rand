from argparse import ArgumentParser
import xml.etree.ElementTree as ET
import random
import glob

# TODO:
#
# * Choice between series and movie?
#
# DONE:
# * launch by clicking bat file
# * no parameters needed
# * finds all xml files and asks
#

if __name__ == '__main__':  # huh?

    ListOfXML = (glob.glob('*.xml'))
    print('Select an xml file:')
    i = int(0)
    for each in ListOfXML:
        print(i, ':', ListOfXML[i])
        i = (i+1)
    choice = int(input())
    selectedMALfile = ListOfXML[choice]
    print(selectedMALfile, ' selected.\n')
    #print ('Exclude movies? [Y/N]\n')

    list_tree = ET.parse(selectedMALfile) 
    tree_root = list_tree.getroot()

    ptw_list = list()
    for anime in tree_root.findall("anime"):  # from each <anime> in the xml
        if anime.find("my_status").text == "Plan to Watch":  # if my_status = PTW
            # add it to ptw_list as its series_title
            ptw_list.append(anime.find("series_title").text)
    opts = ["y", "n"]
    while True:  # Prompt user
        user_in = input("Get random anime? [Y/N]: ").lower().rstrip()
        if user_in not in opts:
            print("Invalid input!\n")
            continue
        elif user_in == "n":
            break

        # pick a random anime from ptw_list
        rand_index = random.randint(0, len(ptw_list))
        print("Your random anime is: {}\n".format(ptw_list[rand_index]))
