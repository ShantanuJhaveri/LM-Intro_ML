# Shantanu Jhaveri
# ITP 449 Fall 2020
# HW1
# Question 2

# Prompt
# Write a program that prompts the user to enter their full name then prints the number of characters in
# their name (do not count spaces).

name = input("ENTER YOUR FULL NAME:\n")


def nameCounter(name):
    count = len(name) - name.count(' ')
    return count


print("YOU HAVE " + str(nameCounter(name)) + " CHARACTERS IN YOUR FULL NAME")
