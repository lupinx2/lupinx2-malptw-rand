from argparse import ArgumentParser
import xml.etree.ElementTree as ET
import random

#TODO:
#* one-click launch
#   Double click .bat file to run
#
#* No arguments at runtime
#   Make it find a .xml file on its own somehow.
#   Currently uses only lupinx2_MAL.xml specifically
#   Ask user to name file a specific way?
#   IDEALLY: the script should offer the coice of every .xml file in the directory
#
#* figure out WTF argumentparser is and what it does and to whom it does it
#
#* Choice between series and movie?
#


if __name__ == '__main__': #huh?
    parser = ArgumentParser(description="Pick a random show from your PTW list")
    #ArgumentParser declared
    parser.add_argument("mal_list",#with the xml file as a parameter, parser 
                        metavar="LIST",#saves it as mal_list
                        type=str,
                        help="The exported XML from your MAL page.")

    args = parser.parse_args()#I guess args.mal_list is the xml file?
    list_tree = ET.parse(args.mal_list)
    tree_root = list_tree.getroot()

    ptw_list = list()
    for anime in tree_root.findall("anime"):#from each <anime> in the xml
        if anime.find("my_status").text == "Plan to Watch":#if my_status = PTW
            ptw_list.append(anime.find("series_title").text)#add it to ptw_list as its series_title

    opts = ["y", "n"]
    while True:#Prompt user
        user_in = input("Get random anime? [Y/N]: ").lower().rstrip()
        if user_in not in opts:
            print("Invalid input!\n")
            continue
        elif user_in == "n":
            break

        rand_index = random.randint(0, len(ptw_list))#pick a random anime from ptw_list
        print("Your random anime is: {}\n".format(ptw_list[rand_index]))