import random
import string
 
WORDLIST_FILENAME = "words.txt"
 
def loadWords():
    """
   Returns a list of valid words. Words are strings of lowercase letters.
   
   Depending on the size of the word list, this function may
   take a while to finish.
   """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist
 
def chooseWord(wordlist):
    """
   wordlist (list): list of words (strings)
 
   Returns a word from wordlist at random
   """
    return random.choice(wordlist)
 
# end of helper code
# -----------------------------------
 
# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()
 
 
def isWordGuessed(secretWord, lettersGuessed):
    if secretWord == '':
        return True
    else:
        if lettersGuessed.count(secretWord[0]) > 0:
            return isWordGuessed(secretWord[1:], lettersGuessed)
        else:
            return False
 
 
def getGuessedWord(secretWord, lettersGuessed):
    if len(secretWord) == 0:
        return ''
    else:
        if lettersGuessed.count(secretWord[0]) > 0:
            return secretWord[0] + ' ' + getGuessedWord(secretWord[1:], lettersGuessed)
        else:
            return '_ ' + getGuessedWord(secretWord[1:], lettersGuessed)
 
 
def getAvailableLetters(lettersGuessed):
    lettersLeft = 'abcdefghijklmnopqrstuvwxyz'
    x = lettersGuessed[:]
    while len(x) > 0:
        g = x.pop(0)
        if lettersLeft.find(g) != -1:
            lettersLeft = lettersLeft[0:lettersLeft.find(g)] + lettersLeft[lettersLeft.find(g)+1:]
    return lettersLeft
   
 
def hangman(secretWord):
    '''
   secretWord: string, the secret word to guess.
 
   Starts up an interactive game of Hangman.
 
   * At the start of the game, let the user know how many
     letters the secretWord contains.
 
   * Ask the user to supply one guess (i.e. letter) per round.
 
   * The user should receive feedback immediately after each guess
     about whether their guess appears in the computer's word.
 
   * After each round, you should also display to the user the
     partially guessed word so far, as well as letters that the
     user has not yet guessed.
 
   Follows the other limitations detailed in the problem write-up.
   '''
    guessesLeft = 8
    guessedLetters = []
   
    print("")
    print("  Hangman 1.0  ")
    print("---------------")
    print("")
 
    print("The word is " + str(len(secretWord)) + " letters long.")
    print("")
   
    while guessesLeft > 0:
        print("You have " + str(guessesLeft) + " guesses left.")
        a = raw_input("Guess a letter:")
        #while (a not in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"):
        #    a = raw_input("That is not a letter. Please guess a letter:")
        if a.lower() in getAvailableLetters(guessedLetters):
            guessedLetters.append(a.lower())
        print(guessedLetters)
        #else:
        #    while a.lower() not in getAvailableLetters(guessedLetters):
        #        a = raw_input("You have already guessed that letter. Please guess a new letter:")
        #    guessedLetters.append(a.lower())
        #    print(guessedLetters)
        if a.lower() in secretWord:
            print("Correct: " + getGuessedWord(secretWord, guessedLetters))
        else:
            print("Incorrect: " + getGuessedWord(secretWord, guessedLetters))
            guessesLeft -= 1
        print('')
    print("Sorry, you have no more guesses. The word was: " + secretWord)
# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)
 
# secretWord = chooseWord(wordlist).lower()
secretWord = "cunt"
hangman(secretWord)