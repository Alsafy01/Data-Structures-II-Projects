from FileReader import Dictionary

dictionary = Dictionary()
dictionary.loadDictionary()
while (True):
    switch = input("What do you want to do?\n"
                   "1)print the Dictionary\n"
                   "2)Insert a word to the Dictionary\n"
                   "3)LookUp a word\n"
                   "4)Quit\n")

    match switch:
        case '1':
            dictionary.printDictionary()
        case '2':
            dictionary.insertWord()
        case '3':
            dictionary.lookUp()
        case '4':
            break
