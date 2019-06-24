
def searchTermFreaquency(index, word):
    with open("Index-" + index + "/word2ID.txt", mode="r", encoding="utf-8") as file:
        for line in file:
            elements = list(str(line).split())

            if(elements[0] == word):
                return elements[2]

def termAppearanceInfo(index, word):
    lineAppearances = set()

    with open("Index-" + index + "/word2ID.txt", mode="r", encoding="utf-8") as file:
        for line in file:
            elements = list(str(line).split())

            if(elements[0] == word):
                for i in range(3,len(elements)):
                    lineAppearances.add(elements[i])

    wordID2TermAppearances = {}

    with open("Index-" + index + "/revertedFile.txt", mode="r", encoding="utf-8") as file:
        lineCounter = 0
        for line in file:
            if str(lineCounter) in lineAppearances:
                wordID2TermAppearances[line.split()[1]] = line.split()[2]

            lineCounter += 1

    termAppearanceInfo = []

    with open("Index-" + index + "/text2ID.txt", mode="r", encoding="utf-8") as file:
        lineCounter = 0
        for line in file:
            if str(lineCounter) in wordID2TermAppearances:
                termAppearanceInfo.append([line.split()[0], wordID2TermAppearances[str(lineCounter)], line.split()[2]])
            lineCounter += 1

    return termAppearanceInfo
