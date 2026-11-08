
# Mollee Beck
# CSD-325
# Assignment: Brownfield + Flowchart(s)
# Modified Cho-Han Program
#
# Changes made:
# 1. Changed both input prompts to MB:
# 2. Changed the house fee from 10% to 12%.
# 3. Added a notice explaining the 10-mon bonus.
# 4. Added a 10-mon bonus when the dice total is 2 or 7.

"""Cho-Han, by Al Sweigart al@inventwithpython.com
The traditional Japanese dice game of even-odd.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: short, beginner, game"""

import random, sys

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN',
                    4: 'SHI', 5: 'GO', 6: 'ROKU'}

# Display the game introduction and bonus notice.
print('''Cho-Han, by Al Sweigart al@inventwithpython.com

In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number.

BONUS: If the dice total is 2 or 7, you receive a 10 mon bonus!
''')

purse = 5000

while True:  # Main game loop.

    # Place your bet.
    print('You have', purse, 'mon. How much do you bet? (or QUIT)')

    while True:
        pot = input('MB: ')

        if pot.upper() == 'QUIT':
            print('Thanks for playing!')
            sys.exit()

        elif not pot.isdecimal():
            print('Please enter a number.')

        elif int(pot) > purse:
            print('You do not have enough to make that bet.')

        else:
            # This is a valid bet.
            pot = int(pot)
            break

    # Roll the dice.
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    print('The dealer swirls the cup and you hear the rattle of dice.')
    print('The dealer slams the cup on the floor, still covering the')
    print('dice and asks for your bet.')
    print()
    print('    CHO (even) or HAN (odd)?')

    # Let the player bet cho or han.
    while True:
        bet = input('MB: ').upper()

        if bet != 'CHO' and bet != 'HAN':
            print('Please enter either "CHO" or "HAN".')
            continue
        else:
            break

    # Reveal the dice results.
    print('The dealer lifts the cup to reveal:')
    print('  ', JAPANESE_NUMBERS[dice1], '-', JAPANESE_NUMBERS[dice2])
    print('    ', dice1, '-', dice2)

    # Assignment change: Calculate the dice total.
    diceTotal = dice1 + dice2

    # Assignment change: Award a 10-mon bonus for a total of 2 or 7.
    if diceTotal == 2 or diceTotal == 7:
        print('The dice total is', diceTotal, '!')
        print('You received a 10 mon bonus!')
        purse = purse + 10

    # Determine if the player won.
    rollIsEven = diceTotal % 2 == 0

    if rollIsEven:
        correctBet = 'CHO'
    else:
        correctBet = 'HAN'

    playerWon = bet == correctBet

    # Display the bet results.
    if playerWon:
        print('You won! You take', pot, 'mon.')
        purse = purse + pot

        # Assignment change: The house fee is now 12% instead of 10%.
        houseFee = pot * 12 // 100
        print('The house collects a', houseFee, 'mon fee.')
        purse = purse - houseFee

    else:
        purse = purse - pot
        print('You lost!')

    # Check if the player has run out of money.
    if purse == 0:
        print('You have run out of money!')
        print('Thanks for playing!')
        sys.exit()