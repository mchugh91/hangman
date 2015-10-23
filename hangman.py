__author__ = 'Ciaran'

import random

def genRandomWord():
    list_of_words = ["python", "jumble", "easy", "difficult", "answer",  "xylophone"]
    word = random.choice(list_of_words)
    return word

def createCurrentBlank(word):
    currentBlanks = len(word) * "_"
    return currentBlanks

def printCurrentBlanks(currentBlanks):
    for i in range(0,len(currentBlanks)):
        print(currentBlanks[i], end = " ")


def guessALetter():
    letter=input("Guess a letter: ")
    return letter

def goodGuess(letter,word):
    #returns true if letter is in word otherwise return false
    match=False
    for i in range(len(word)):
        if word[i]==letter:
            match=True

    return match


def updateCurrentBlanks(letter,word,currentBlanks):
    # check word for letter and replace blanks in currentBlacks with any matches
    wordList = list(word)
    for x in range(len(wordList)):
        if wordList[x] == letter:
            currentBlanks = currentBlanks[:x] + wordList[x] + currentBlanks[x+1:]
    return currentBlanks

def printRules():
    print('rules!')

def printLives(currentLives):
    print(currentLives)


def main():
    printRules()

    word = genRandomWord()
    currentBlanks = createCurrentBlank(word)
    printCurrentBlanks(currentBlanks)
    currentLives = 10
    while currentLives > 0 and word != currentBlanks:
        letter = guessALetter()
        lastGuessGood = goodGuess(letter,word)
        if lastGuessGood:
            currentBlanks = updateCurrentBlanks(letter,word,currentBlanks)
        else:
            currentLives = currentLives - 1

        printCurrentBlanks(currentBlanks)
        printLives(currentLives)

main()