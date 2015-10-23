__author__ = 'Ciaran'

import random

def generateWord():
    list_of_words = ["python", "jumble", "easy", "difficult", "answer",  "xylophone"]
    randomWord = random.choice(list_of_words)
    #print(word)
    return randomWord

def showBlank(randomWord):
    blankWord = len(randomWord) * "*"
    print(blankWord)

# def printCurrentLives(currentLives):
#     while currentLives > 0:
#         print(currentLives)

def guessLetter():
    letter = input("Guess a letter: ")
    return letter

def replaceLetter(letter, randomWord, blankWord):
    index = randomWord.find(letter)
    blankWord = blankWord[:index] + letter + blankWord[index+1:]
    print(blankWord)
    return blankWord

def checkLetter(letter, randomWord):
    #returns true if letter is in word otherwise return false
    for i in range(len(randomWord)):
        if randomWord[i] == letter:
            correct = True
        else:
            correct = False
        return correct


def main():
    randomWord = generateWord()
    currentLives = 10
    blankWord = showBlank(randomWord)
    while currentLives > 0:
        letter = guessLetter()
        guess = checkLetter(letter, randomWord)
        if guess:
            replaceLetter(letter, randomWord, blankWord)
        else:
            currentLives = currentLives - 1
            print(blankWord)
        print(currentLives)





main()