import os
import re

def removeNumbers(list):
    pattern = '[0-9]'
    list = [re.sub(pattern, '', i) for i in list]
    return list

# os.mkdir("Index-1")
# os.mkdir("Index-2")
# os.mkdir("Index-3")
# os.mkdir("Index-4")

wordsList = list()

for filename in os.listdir("CACM"):
    with open("CACM/" + filename, mode="r", encoding="utf-8") as myFile:
        words = myFile.read().split()
        words = removeNumbers(words)
        words = list(filter(None, words))
        wordsList += words

# print(wordsList)
print(len(wordsList))

