#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Singular to Plural program
Author: Jary Chen
Date Created: October 13, 2021
Date Modified: October 15, 2021
"""

# The 'questions' for the user
integer = input("input # of items: ")
string = input("inhput a word: ")

if integer.isdigit() == True and string.isalpha() == True:

    # Checking if integer is a number if True it'll proceed checking the rules
    if integer.isdigit():
        integer = int(integer)

        # Singular if singular number and word
        if integer == 1:
            print(f"{integer} {string}")
        # Plural
        if integer > 1 or integer == 0:

            # Endings with vowel and replacing it with 's'
            if string.endswith("ay") or string.endswith("ey") or string.endswith("iy") or string.endswith("oy") or string.endswith("uy"):
                print(f"{integer} {string}s")

            # All the Irregular words
            elif string.endswith("man"):
                print(f"{integer} men")
            elif string.endswith("child"):
                print(f"{integer} children")
            elif string.endswith("foot"):
                print(f"{integer} feet")
            elif string.endswith("tooth"):
                print(f"{integer} teeth")
            elif string.endswith("mouse"):
                print(f"{integer} mice")
            elif string.endswith("person"):
                print(f"{integer} people")

            # For Quiz since it need to have two 'z's
            elif string.endswith("quiz"):
                print(f"{integer} quizzes")

            # Exceptions
            elif string.endswith("piano") or string.endswith("photo") or string.endswith("roof") or string.endswith("cliff"):
                print(f"{integer} {string}s")

            # The no changing words
            elif string.endswith("sheep") or string.endswith("deer") or string.endswith("fish") or string.endswith("series") or string.endswith("species"):
                print(f"{integer} {string}")

            # Words ending with Vowel +O
            elif string.endswith("ao") or string.endswith("eo") or string.endswith("io") or string.endswith("oo"):
                print(f"{integer} {string}s")

            # Words ending with Constants +O
            elif string.endswith("o"):
                print(f"{integer} {string}es")

            # Words ending with Constant
            elif string.endswith("y"):
                print(f"{integer} {string[:-1]}ies")

            # words ending with 's' or 'ch' or 'sh' or 'x' or 'z'
            elif string.endswith("s") or string.endswith("ch") or string.endswith("sh") or string.endswith("x") or string.endswith("z"):
                print(f"{integer} {string}es")

            # word ending with 'f' replacing it with 'ives'
            elif string.endswith("f"):
                print(f"{integer} {string[:-1]}ves")

            # word ending with 'fe' replacing it with 'ives'
            elif string.endswith("fe"):
                print(f"{integer} {string[:-2]}ves")

            # Regular nouns
            else:
                print(f"{integer} {string}s")

#'invalid input' is given if
else:
    print("invalid input")
