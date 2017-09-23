# John Daudelin
# CS 100 2016F Section H01
# Bagels Project, December 6, 2016

import random
import string

def threeDigits():
    """Return a string containing three random digits."""
    digit1 = random.choice(string.digits)
    digit2 = random.choice(string.digits)
    digit3 = random.choice(string.digits)
    return digit1 + digit2 + digit3

def computer1Guess(count):
    """
    Returns an intelligent guess based on previous information gathered from
    calls to the function computer1Analysis().

    Keyword arguments:
    count -- the number of guesses already made (will be 1 for the first guess)

    Note: this function uses information stored in several global variables not
    defined or initialized here. They are described further on in the program.

    If the first, second, or third digit is already known, always
    make a guess with this digit in place.

    For the first four guesses, guess 123, 456, 789, and possibly 000
    """
    certainty = [False, False, False]
    digits = ['0', '0', '0']  #Default guess will be 000

    if inFirst != "":
        digits[0] = inFirst
        certainty[0] = True
    if inSecond != "":
        digits[1] = inSecond
        certainty[1] = True
    if inThird != "":
        digits[2] = inThird
        certainty[2] = True

    it = iter(defIn)
    
    if True not in certainty:
        if count < 4:
            #Test the guesses 123, 456, 789 first
            digits[0] = str(count * 3 - 2)
            digits[1] = str(count * 3 - 1)
            digits[2] = str(count * 3)
        elif count > 4 or (len(notIn[0]) + len(notIn[1]) + len(notIn[2])) > 9:  #Do NOT test default 4th guess of 000 if certain info is already known
            #If there are any digits in defIn, test these digits first in the first position
            for i in range(len(defIn) + 1):
                if i == len(defIn):
                    digits[0] = random.choice(remainingDigits[0])
                else:
                    digits[0] = next(it)
                    if digits[0] not in notIn[0]:
                        break
            #Select the last two digits as dummy digits (ones known to be wrong)
            #Also, make sure these digits are the same as each other
            for i in range(len(notIn[1])):
                digits[1] = notIn[1][i]
                if digits[1] in notIn[2]:
                    digits[2] = digits[1]
                    break
    elif certainty.count(True) == 1:
        found = False
        for i in range(3):
            if not certainty[i]:
                #Select the first non-certain digit from a list of remaining candidates
                #The second non-certain digit as simply a dummy digit (one known to be wrong)
                if found == False:
                    #If there are any digits in defIn, test these digits first
                    for j in range(len(defIn) + 1):
                        if j == len(defIn):
                            digits[i] = random.choice(remainingDigits[i])
                        else:
                            digits[i] = next(it)
                            if digits[i] not in notIn[i]:
                                break
                    found = True
                else:
                    digits[i] = notIn[i][0]
    else:    
        for i in range(3):
            if not certainty[i]:
                for j in range(len(defIn)):
                    digits[i] = next(it)
                    if digits[i] not in notIn[i]:
                        break
                if len(defIn) == 0 or digits[i] in notIn[i]:
                    digits[i] = random.choice(remainingDigits[i])
        
    return digits[0] + digits[1] + digits[2]

def computer1Analysis(guess, clue):
    """
    Analyze what information can be gathered from a clue for a given guess.

    Keyword arguments:
    guess -- the three-digit string for which the clue is applicable
    clue -- the list of fermis, picos, and bagels in the given guess
    """
    global notIn
    global defIn
    global inFirst
    global inSecond
    global inThird
    global remainingDigits
    defIn = set(defIn)

    #For convenient referencing later on
    digits = [guess[0], guess[1], guess[2]]

    #Handle the case of three bagels
    if clue[2] == 3:
        for i in range(3):
            for j in range(3):
                notIn[i].append(digits[j])
                remainingDigits[i] = remainingDigits[i].replace(digits[j], "")
              
    #Handle the case of one fermi and two bagels
    elif clue[0] == 1 and clue[2] == 2:
        #Handle when two digits are explicitely known to be the bagels
        if digits[0] in notIn[0] and digits[1] in notIn[1]:
            inThird = digits[2]
            defIn.discard(digits[2])
        elif digits[0] in notIn[0] and digits[2] in notIn[2]:
            inSecond = digits[1]
            defIn.discard(digits[1])
        elif digits[1] in notIn[1] and digits[2] in notIn[2]:
            inFirst = digits[0]
            defIn.discard(digits[0])

        #Handle when one digit is known to be the fermi
        elif digits[2] == inThird or digits[2] in defIn:
            for i in range(2):
                for j in range(2):
                    notIn[i].append(digits[j])
                    remainingDigits[i] = remainingDigits[i].replace(digits[j], "")
            inThird = digits[2]
            defIn.discard(digits[2])
        elif digits[1] == inSecond or digits[1] in defIn:
            for i in range(0, 3, 2):
                for j in range(0, 3, 2):
                    notIn[i].append(digits[j])
                    remainingDigits[i] = remainingDigits[i].replace(digits[j], "")
            inSecond = digits[1]
            defIn.discard(digits[1])
        elif digits[0] == inFirst or digits[0] in defIn:
            for i in range(1, 3):
                for j in range(1, 3):
                    notIn[i].append(digits[j])
                    remainingDigits[i] = remainingDigits[i].replace(digits[j], "")
            if inFirst == "":
                inFirst = digits[0]
                defIn.discard(digits[0])

        #Handle when all digits are the same
        elif digits[0] == digits[1] and digits[1] == digits[2]:
            defIn.add(digits[0])
            
    #It is assumed here that the third digit is a bagel, since a winning
    #message would be displayed otherwise
    elif clue[0] == 2:
        #Handle the case of two fermis when two digits are already known
        if digits[0] == inFirst and digits[1] == inSecond:
            notIn[2].append(digits[2])
            remainingDigits[2] = remainingDigits[2].replace(digits[2], "")
        if digits[1] == inSecond and digits[2] == inThird:
            notIn[0].append(digits[0])
            remainingDigits[0] = remainingDigits[0].replace(digits[0], "")
        if digits[0] == inFirst and digits[2] == inThird:
            notIn[1].append(digits[1])
            remainingDigits[1] = remainingDigits[1].replace(digits[1], "")

        #Handle the case of two fermis and one digit that is known to not be in the secret
        if digits[0] in notIn[0]:
            inThird = digits[2]
            inSecond = digits[1]
            defIn.discard(digits[2])
            defIn.discard(digits[1])
        elif digits[1] in notIn[1]:
            inThird = digits[2]
            inFirst = digits[0]
            defIn.discard(digits[2])
            defIn.discard(digits[0])
        elif digits[2] in notIn[2]:
            inFirst = digits[0]
            inSecond = digits[1]
            defIn.discard(digits[0])
            defIn.discard(digits[1])
    #Handle the case of three picos
    elif clue[1] == 3:
        for i in range(3):
            notIn[i].append(digits[i])
            remainingDigits[i] = remainingDigits[i].replace(digits[i], "")
            defIn.add(digits[i])
    #Handle the case of no fermis
    elif clue[0] == 0:
        #If there is a pico as well...
        if clue[1] == 1:
            if digits[1] in notIn[0] and digits[1] in notIn[2] and digits[1] in notIn[1] and digits[2] in notIn[0] and digits[2] in notIn[1] and digits[2] in notIn[2]:
                defIn.add(digits[0])
        for i in range(3):
            notIn[i].append(digits[i])
            remainingDigits[i] = remainingDigits[i].replace(digits[i], "")
    #Handle the case of one fermi and at least one pico
    elif clue[0] == 1 and clue[1] > 0:
        if inFirst == digits[0]:
            #Handle when two picos
            if clue[1] == 2:
                inSecond = digits[2]
                inThird = digits[1]
                defIn.discard(digits[2])
                defIn.discard(digits[1])
            #Handle when one pico
            elif clue[1] == 1:
                if digits[1] in notIn[2]:
                    inSecond = digits[2]
                    defIn.discard(digits[2])
                elif digits[2] in notIn[1]:
                    inThird = digits[1]
                    defIn.discard(digits[1])
                notIn[1].append(digits[1])
                remainingDigits[1] = remainingDigits[1].replace(digits[1], "")
                notIn[2].append(digits[2])
                remainingDigits[2] = remainingDigits[2].replace(digits[2], "")
        elif digits[1] in notIn[1] and digits[2] in notIn[2]:
            inFirst = digits[0]
            defIn.discard(digits[0])
        elif digits[0] in notIn[0] and digits[2] in notIn[2]:
            inSecond = digits[1]
            defIn.discard(digits[1])
        elif digits[0] in notIn[0] and digits[1] in notIn[1]:
            inThird = digits[2]
            defIn.discard(digits[2])

def clue(secret, guess):
    """
    Return a clue in the form of a three-element list.

    Keyword arguments:
    secret -- the three-digit string to compare the guess to
    guess -- the three-digit string to analyze in comparison with the secret

    Calculate the number of digits in the guess that exactly match up with digits
    in the secret (fermis), the number of digits in the guess that have a correspondingly
    identical digit in the secret but in a different location (picos), and the number
    of digits in the guess that have no correspondingly identical digit in the secret
    (bagels). Total fermis, picos, and bagels must add up to three. In addition,
    the same digit from the secret may not be compared to more than one digit
    in the guess.

    Return these three numbers in a list containing fermis first, picos second, and bagels
    third.
    """
    
    lst = [0, 0, 0]
    usedSecret = []
    usedGuess = []

    #find fermis in guess
    for i in range(3):
        if secret[i] == guess[i]:
            lst[0] += 1
            usedSecret.append(i)
            usedGuess.append(i)

    #find picos
    for i in range(3):
        for j in range(3):
            if i not in usedSecret and j not in usedGuess and secret[i] == guess[j]:
                lst[1] += 1
                usedSecret.append(i)
                usedGuess.append(j)

    #find bagels
    lst[2] = len(secret) - lst[0] - lst[1]

    return lst
    
    
def playGame(player):
    """
    Play the game of Bagels.

    Keyword arguments:
    player -- a string dictating how guesses are retrieved

    Create a secret and enter a loop which does three things repetively:
      1. Retrieve a new guess
      2. Generate the clue for the new guess
      3. Print the results of the clue, analyze the results (if
         using a computer AI), and break out of the loop if
         the secret was guessed correctly or if the max number
         of guesses has been reached
    """
    secret = threeDigits()
    guessNum = 0
    maxGuesses = 30  #Can change at will...

    while True:
        #Retrieve a guess
        if player == "human":
            guess = input("You have " + str(maxGuesses - guessNum) + " guesses left. Enter a three digit guess: ")
        elif player == "computer1":
            guess = computer1Guess(guessNum + 1)
            print("Computer guessed " + guess)

        #Test if the guess is in a valid format (for human player),
        #and if not, start at beginning of loop again
        if len(guess) != 3 or guess[0] not in string.digits or guess[1] not in string.digits or guess[2] not in string.digits:
            print("Sorry, wrong type of input.")
            continue

        #Retrieve the clue for the given guess and increment guess count
        clueLst = clue(secret, guess)
        guessNum += 1

        #If using an AI, analyze the clue for the recent guess and update
        #global variables accordingly
        if player == "computer1":
            computer1Analysis(guess, clueLst)

        #Print results of the guess
        if clueLst[0] == 3:
            print("Problem Solved!")
            break
        else:
            print("Clue: ", clueLst[0], "fermis,", clueLst[1], "picos, and", clueLst[2], "bagels.")

            #End game if user is out of guesses
            if guessNum == maxGuesses:
                print("Sorry! You're out of guesses.\nThe secret was ", secret, "!")
                break

def testGame(testNum):
    """
    Test the computer AI on the game of Bagels.

    Keyword arguments:
    testNum -- the number of times to test

    Play the game of Bagels testNum times (using computer1) and display the average,
    minimum, and maximum number of guesses taken by the computer to guess the secret.

    Note: this function does not use the function playGame() because the amount of output
    from every call to playGame() would be too great for the user to handle or make sense 
    of for large test batches.
    """
    global notIn
    global defIn
    global inFirst
    global inSecond
    global inThird
    global remainingDigits
    
    summation = 0
    maximum = 0
    minimum = 25

    print("Testing " + str(testNum) + " times.")
    
    for i in range(testNum):
        #reset global variables to be used by AI
        notIn = [[], [], []]
        defIn = []
        inFirst = ""
        inSecond = ""
        inThird = ""
        remainingDigits = [string.digits, string.digits, string.digits]
        
        secret = threeDigits()
        guessNum = 0
        
        #If this test case fails, infoString will be used later to
        #print the entire results of the failed test case.
        infoString = secret + "\n"

        while True:
            #Retrieve a guess
            guess = computer1Guess(guessNum + 1)

            #Retrieve the clue for the given guess and increment guess count
            clueLst = clue(secret, guess)
            guessNum += 1
            
            #Analyze the clue and update global variables accordingly
            computer1Analysis(guess, clueLst)

            #Update infoString with new guess information
            infoString += guess + "\n" + str(clueLst) + "\nfirst: " + inFirst + ", second: " + inSecond + ", third: " + inThird + "\n"

            if clueLst[0] == 3:
                #Update analytics for the entire batch of test cases and break
                #out to start the next test case.
                summation += guessNum
                if guessNum > maximum:
                    maximum = guessNum
                if guessNum < minimum:
                    minimum = guessNum
                break
            elif guessNum > 30:
                #Test case failed. Print results of specific test case that failed.
                print("max guesses exceeded")
                print(infoString)
                break
    
    #Print analytics for test batch
    print("Average number of guesses was " + str(summation / testNum))
    print("Maximum number of guesses was " + str(maximum))
    print("Minimum number of guesses was " + str(minimum))

#Initialize global variables to be used by the AI, "computer1"
notIn = [[], [], []]
defIn = []
inFirst = ""
inSecond = ""
inThird = ""
remainingDigits = [string.digits, string.digits, string.digits]

#Run the program: allow the user to play, show complete output for a sample AI run,
#and test the AI 10,000 times
print("Welcome to Bagels! This program will first allow you to play the game.\nIt will then demonstrate and test the AI.\n")
playGame("human")
print("\nWe will now look at a sample AI solution.\n")
playGame("computer1")
print("\nWe will now test the AI solution 10,000 times.\n")
testGame(10000)
