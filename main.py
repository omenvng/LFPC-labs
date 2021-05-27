from rulesLibrary import *
from string import ascii_letters
import re


if __name__ == '__main__':

    rules = {}
    voc = []
    # This list's going to be our "letters pool" for naming new states
    let = list(ascii_letters[26:]) + list(ascii_letters[:25])

    let.remove('e')

    # Number of grammar rules
    while True:
        userInput = input('Give number of rules\n')
        try:
            # check if N is integer >=2
            numberOfRules = int(userInput)
            if numberOfRules <= 2:
                print('N must be a number >=2!')
            else:
                break
        except ValueError:
            print("That's not an int!")

    # Initial state
    while True:
        S = input('Give initial state\n')
        if not re.match("[a-zA-Z]*$", S):
            print('Initial state must be a single character!')
        else:
            break

    print('+------------------------------------------------------+\n' +
          '|Give rules in the form A B for the form A->B          |\n' +
          '|or A BCD, if more than one states in the right part   |\n' +
          '|(without spaces between right part members).          |\n' +
          '+------------------------------------------------------+')

    for i in range(numberOfRules):
        fr, to = map(str, input('Rule #' + str(i + 1)).split())
        print('\n')
        for letter in fr:
            if letter != 'e' and letter not in voc:
                voc.append(letter)
            if letter in let:
                let.remove(letter)
        for letter in to:
            if letter != 'e' and letter not in voc:
                voc.append(letter)
            if letter in let:
                let.remove(letter)
        # Insert rule to dictionary
        rules.setdefault(fr, []).append(to)

    # remove large rules and print new rules
    print('\nRules after large rules removal')
    rules, let, voc = large(rules, let, voc)
    printRules(rules)
    # print voc

    # remove empty rules and print new rules
    print('\nRules after empty rules removal')
    rules, voc = empty(rules, voc)
    printRules(rules)
    # print voc

    print('\nRules after short rules removal')
    rules, D = short(rules, voc)
    printRules(rules)

    print('\nFinal rules')
    rules = finalRules(rules, D, S)
    printRules(rules)
