import os
import re
import string
import nltk
from nltk.stem.porter import PorterStemmer
# nltk.download('punkt') # Uncomment  this the first time you run the program

def removeNumbers(words):
    pattern = '[0-9]'
    words = [re.sub(pattern, '', i) for i in words]
    return words

def punctuationAndLower(words):
    words = words.translate(str.maketrans('', '', string.punctuation))
    words = words.lower()
    return words

def stemming(words):
     porter_stemmer = PorterStemmer()

     for i in range(len(words)):
         words[i] = porter_stemmer.stem(words[i])

     return  words

def stopwordRemoval(words):
    with open("files/stoplist.txt", mode="r", encoding="utf-8") as file:
        stopwordList = set()
        for line in file:
            stopwordList.add(line.strip())

        for word in reversed(words):
            if (word in stopwordList):
                words.remove(word)
                
        return words

def createIndex(indexNum):
    try:
        os.mkdir(indexNum)
    except FileExistsError:
        pass
        
    wordsList = list()
    word2ID_Dict = {}  # 1
    text2ID_Dict = {}  # 2
    revertedFile_Dict = {}  # 3

    fileID = 0
    a = 0  # Testing purposes

    for filename in os.listdir("CACM"):
        fileID += 1
        a += 1  # Testing purposes

        with open("CACM/" + filename, mode="r", encoding="utf-8") as file:
            words = file.read()
            words = punctuationAndLower(words)
            words = words.split()
            words = removeNumbers(words)
            words = list(filter(None, words))

            words.remove('html')
            words.remove('pre')
            words.remove('pre')
            words.remove('html')

            if(indexNum == "Index-1"):
                pass
            elif(indexNum == "Index-2"):
                words = stemming(words)
            elif(indexNum == "Index-3"):
                words = stopwordRemoval(words)
            elif(indexNum == "Index-4"):
                words = stopwordRemoval(words)
                words = stemming(words)

            '''creating the text2ID dictionary'''
            text2ID_Dict[filename] = [fileID, len(words)]

            '''creating the revertedFile dictionary'''
            for word in words:
                if (word in revertedFile_Dict) and (revertedFile_Dict[word][0][0] != fileID):
                    revertedFile_Dict[word].append([fileID, 1])
                elif (word in revertedFile_Dict) and (revertedFile_Dict[word][0][0] == fileID):
                    revertedFile_Dict[word][0][1] += 1
                else:
                    revertedFile_Dict[word] = [[fileID, 1]]

            # Testing purposes
            # print(sorted(words))
            # if a == 2:
            #     print(sorted(words))
            #     break

            wordsList += words

    wordsList = list(sorted(set(wordsList)))

    index = 0
    line = 0

    '''creating the word2ID dictionary'''
    for word in wordsList:
        index += 1
        frequency = 0

        word2ID_Dict[word] = [index, 0, []]

        for i in revertedFile_Dict[word]:
            line += 1
            frequency += i[1]

            word2ID_Dict[word][2].append(line)

        word2ID_Dict[word][1] = frequency

    # Testing purposes
    # print(wordsList)
    # print(word2ID_Dict['a.'])
    # print(wordsList)
    # print(text2ID_Dict)
    # print(len(wordsList))

    with open(indexNum + "/text2ID.txt", mode="w", encoding="utf-8") as file:
        file.write("textName textID textLength\n")

        textNamesList = sorted(list(text2ID_Dict.keys()))

        for textName in textNamesList:
            file.write(textName + " " + str(text2ID_Dict[textName][0]) + " " + str(text2ID_Dict[textName][1]) + "\n")

    with open(indexNum + "/word2ID.txt", mode="w", encoding="utf-8") as file:
        file.write("word wordID frequency line_appearences\n")

        # wordsList = sorted(list(text2ID_Dict.keys()))

        for word in wordsList:
            file.write(word + " " + str(word2ID_Dict[word][0]) + " " + str(word2ID_Dict[word][1]) + " ")
            for line in word2ID_Dict[word][2]:
                file.write(str(line) + " ")
            file.write("\n")

    with open(indexNum + "/revertedFile.txt", mode="w", encoding="utf-8") as file:
        file.write("wordID textID appearances\n")

        # wordsList = sorted(list(revertedFile_Dict.keys()))

        for word in wordsList:
            for value in revertedFile_Dict[word]:
                file.write(str(word2ID_Dict[word][0]) + " " + str(value[0]) + " " + str(value[1]) + "\n")


createIndex("Index-1")
createIndex("Index-2")
createIndex("Index-3")
createIndex("Index-4")