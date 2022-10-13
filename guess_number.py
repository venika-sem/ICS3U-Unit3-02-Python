#!/usr/bin/env python3

# Created by: Venika Sem
# Created on: oct 2022
# This program guess the random number

import constants


def main():
    # this function guess the random number

    # input
    guess = int(input("Enter a number between 0 and 9: "))
    print("")

    # process & output
    if guess == constants.GUESSING_NUMBER:
        print("Congratulations, you guessed correct!")

    if guess != constants.GUESSING_NUMBER:
        print("Sorry, you guessed wrong!")

    print("\nDone.")


if __name__ == "__main__":
    main()
