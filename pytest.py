import os
import glob
# directory = os.getcwd()
# print(directory)
ListOfXML = (glob.glob('*.xml'))
print ('Select an xml file:')
i = int(0)
for each in ListOfXML:
    print(i,':',ListOfXML[i])
    i=(i+1)
choice = int(input())
selectedMALfile = ListOfXML[choice]
print (selectedMALfile,' selected.\n')


    #parser = ArgumentParser(
    #    description="Pick a random show from your PTW list")
    # ArgumentParser declared
    #parser.add_argument("mal_list",  # with the xml file as a parameter, parser
    #                    metavar="LIST",  #named LIST?
    #                    type=str,
    #                    help="The exported XML from your MAL page.")
    #args = parser.parse_args()  # I guess args.mal_list is the xml file?    
    #list_tree = ET.parse(selectedMALfile)
    ##= ET.parse(args.mal_list)
    #tree_root = list_tree.getroot()