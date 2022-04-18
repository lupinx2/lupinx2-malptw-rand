import os
import glob
# directory = os.getcwd()
# print(directory)
ListOfXML = (glob.glob('*.xml'))
print ('Select an xml file:\n')
i = int(0)
for each in ListOfXML:
    print(i,':',ListOfXML[i],'\n')
    i=(i+1)
choice = int(input())
selectedMALfile = ListOfXML[choice]
print (selectedMALfile,' selected.\n')
#print ('Exclude movies? [Y/N]\n')
