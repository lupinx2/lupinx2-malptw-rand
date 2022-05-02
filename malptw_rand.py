from argparse import ArgumentParser
from cmd import PROMPT
import xml.etree.ElementTree as ET
import random
import glob

#TODO
#link to MAL page(?)
#handle missing xml file

if __name__ == '__main__':
    # returns a List with every .xml file in the working directory.
    ListOfXML = (glob.glob('*.xml'))
    print('Select an xml file:')
    i = int(0)
    for each in ListOfXML:
        print(i, ':', ListOfXML[i])
        i = (i+1)

    # prompts user to pick an xml file.
    choice = input()
    try:
        choice = int(choice)
    except ValueError:
        print("Invalid input!\n")
    selectedMALfile = ListOfXML[choice]
    print(selectedMALfile, ' selected.\n')
    list_tree = ET.parse(selectedMALfile)
    tree_root = list_tree.getroot()

    # prompts user to excludde movies or series.
    opts = ["y", "n"]
    while True:
        no_movies = input("Exclude movies? [Y/N]: ").lower().rstrip()
        if no_movies not in opts:
            print("Invalid input!\n")
            continue
        else:
            if no_movies == "n":
                only_movies = input("Only movies? [Y/N]: ").lower().rstrip()
                if only_movies not in opts:
                    print("Invalid input!\n")
                    continue
                else:
                    break
            else:  # if no_movies = Y
                only_movies = "n"
                break

    ptw_list = list()
    ptw_list_id = list()
    for anime in tree_root.findall("anime"):  # from each <anime> in the xml (cont.)
        if anime.find("my_status").text == "Plan to Watch":  # with my_status = PTW (cont.)
            # append to ptw_list list as a string equal to the series_title value.
            ptw_list.append(anime.find("series_title").text +
                            " [" + anime.find("series_type").text + "]")# also include its series_type
            ptw_list_id.append(anime.find("series_animedb_id").text)# and append its series_animedb_id value to ptw_list_id 
            if (anime.find("series_type").text == "Movie") and (no_movies == "y"):
                ptw_list.pop()
                ptw_list_id.pop()
            if (anime.find("series_type").text != "Movie") and (only_movies == "y"):
                ptw_list.pop()
                ptw_list_id.pop()

    # prompt user to pick a random anime from ptw_list.
    while True:
        user_in = input("Get random anime? [Y/n]: ").lower().rstrip()
        if user_in not in opts:
            print("Invalid input!\n")
            continue
        elif user_in == "n":
            break                
        rand_index = random.randint(0, len(ptw_list)-1)        
        print("Your random anime is: {}".format(ptw_list[rand_index]))
        print('https://myanimelist.net/anime/' + (ptw_list_id[rand_index]) + "/\n")        