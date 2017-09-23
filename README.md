# Bagels-AI

## Description

This is an AI (artificial intelligence) that I developed in Python from complete scratch to play the game of Bagels. Bagels is a game in which a user attempts to guess a secret three-digit code that can range from 000 to 999. After every guess (e.g. "043"), the user is notified of how many of his digits exactly match up with digits in the secret code (fermis), how many of his digits have a correspondingly identical digit in the secret code but in a different location (picos), and how many of his digits have no correspondingly identical digit in the secret (bagels). For example, if the secret code was "325" and the user guessed "302," his clue would be: 1 fermi, 1 pico, and 1 bagel. For a more complete description of the game Bagels, see [here](http://www.mathfairy.com/wp/kids/pico-fermi-bagels/).

My AI is able to correctly guess the solution for any secret code in an average of about 10.1 guesses. My program also allows the user to play the game of Bagels without the assistance of an AI.

I wrote this program as an assignment for CS100, an introductory programming class I took during my first semester at NJIT.

## Demo/Setup

If you haven't already, download Python 3.6 onto your machine from [this link](https://www.python.org/downloads/release/python-362/). Be sure to install IDLE during the process.

Open up IDLE (Python 3.6 Shell) and go to File -> Open on the menu bar. Browse to the directory that you cloned this repository into and select "Bagels_JohnDaudelin.py" to open.

Once the .py file has opened, hit Run -> Run Module from the menu bar. IDLE should now run Bagels and ask you to play the game of Bagels! After you've played, the program will show an example of the AI playing a game of Bagels and then test the AI 10,000 times, showing the overall statistics of its game performance to show the efficiency of the program algorithm.

## Code

The driver for my program is at the bottom of Bagels_JohnDaudelin.py:

```python
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
```

This snipet
* initializes the global variables that will be used by the AI to keep track of what is known and help make educated guesses,
* prints a welcome message to the user,
* allows the user to play the game once,
* shows a sample game played by the computer AI,
* makes the AI play 10,000 times and displays the statistics of how efficiently the AI played.

I use helper functions to create a random secret code, play the game, return a clue based on a given guess, analyze a given clue for what information can be gathered (only used by the AI), generate an intelligent guess based on previous information (also only used by the AI), and test the AI any number of times on the game.

## History

Started development mid-November, 2016.

Finished and submitted on December 6, 2016.

## Authors

John Daudelin