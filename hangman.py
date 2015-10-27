__author__ = 'Ciaran'

import random

def genRandomWord(n):
    # list_of_words = ["python", "jumble", "easy", "difficult", "answer",  "xylophone"]
    # word = random.choice(list_of_words)
    listOFWords = []
    with open("dictionary.txt", "r") as f:
        for line in f:
            for word in line.split():
                if len(word) == n:
                    listOFWords.append(word)
    word = random.choice(listOFWords)
    print(word)


    return word

def printWord(word):
    print(word)

def createCurrentBlank(word):
    currentBlanks = (len(word)) * "_"
    return currentBlanks

def printCurrentBlanks(currentBlanks):
    for i in range(0,len(currentBlanks)):
        print(currentBlanks[i], end = " ")


def guessALetter():
    letter = input("Guess a letter: ")
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
    print('The computer will choose a random word. You must guess a letter from that word. If you are right the letter(s) will be '
          'revealed, if not you will lose a life. You have 10 lives.')

def printLives(currentLives):
    print(currentLives)


def main():
    printRules()
    n = int(input("Enter difficulty level: "))
    word = genRandomWord(n)
    currentBlanks = createCurrentBlank(word)
    printCurrentBlanks(currentBlanks)
    currentLives = 10
    listOfLetter = "Used letters: "
    while currentLives > 0 and word != currentBlanks:
        letter = guessALetter()
        listOfLetter += letter + "-"
        print(listOfLetter)
        lastGuessGood = goodGuess(letter,word)
        if lastGuessGood:
            currentBlanks = updateCurrentBlanks(letter,word,currentBlanks)
        else:
            currentLives = currentLives - 1
        printCurrentBlanks(currentBlanks)
        printLives(currentLives)
    if currentLives == 0:
        print("Game Over")
        printWord(word)

main()