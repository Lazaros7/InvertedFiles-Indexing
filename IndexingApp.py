import createIndex
from searchIndexFiles import searchTermFreaquency, termAppearanceInfo

# Be sure to uncomment the nltk.download('punkt') line in createIndex.py
# for the first time you run this script.

print("Creating indexes, please wait.\nAnytime you want to exit, type exit.\n")


while True:
    word = input('Please insert the word you want to search for: \n')
    if word == 'exit':
        break

    index = input('Please choose an index(1-4): \n')
    if index == 'exit':
        break

    try:
        if int(index) not in range(1,5):
            print("Index does not exist. Try again.\n")
            continue
        else:
            termFrequency = searchTermFreaquency(index, word)
            print("The word's term frequency is: " + str(termFrequency))

            elements = termAppearanceInfo(index, word)
            print("Filename       Appearances TextTermLength")
            for i in range(len(elements)):
                print(elements[i][0] + " " + elements[i][1], (10 - len(elements[i][1])) * " ", elements[i][2])

            print()
    except ValueError:
        print("Error. You need to insert a digit as an index.\n")

