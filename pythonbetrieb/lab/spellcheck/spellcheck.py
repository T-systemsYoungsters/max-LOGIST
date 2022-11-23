import re
def splitLine(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)
def main():
    dictionaryList = []
    file = open((r"C:\Users\A200162668\Desktop\Python\pythonbetrieb\lab\spellcheck\dictionary.txt"))
    for line in file:
        line = line.strip()
        dictionaryList.append(line)
    file.close()
    print("--- Linear Search ---")
    file = open((r"C:\Users\A200162668\Desktop\Python\pythonbetrieb\lab\spellcheck\AliceInWonderLand200.txt"))
    lineCount = 0
    for line in file:
        lineCount += 1
        words = splitLine(line)
        for word in words:
            i = 0
            while i < len(dictionaryList) and dictionaryList[i] != word.upper():
                i += 1
            if not (i < len(dictionaryList)):
                print("Line " + str(lineCount) + " - Possible misspelled word: "+ word)
    file.close()
    print("--- Binary Search ---")
    file = open((r"C:\Users\A200162668\Desktop\Python\pythonbetrieb\lab\spellcheck\AliceInWonderLand200.txt"))
    lineCount = 0
    for line in file:
        lineCount = lineCount + 1
        words = splitLine(line)
        for word in words:
            lowerBound = 0
            upperBound = len(dictionaryList) - 1
            found = False
            while lowerBound <= upperBound and not found:
                middlePos = (lowerBound + upperBound) // 2
                if dictionaryList[middlePos] < word.upper():
                    lowerBound = middlePos + 1
                elif dictionaryList[middlePos] > word.upper():
                    upperBound = middlePos - 1
                else:
                    found = True
            if not found:
                print("Line " + str(lineCount) + " - Possible misspelled word: "
                      + word)
    file.close()
main()
