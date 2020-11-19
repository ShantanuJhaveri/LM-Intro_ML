# Shantanu Jhaveri
# ITP 449 Fall 2020
# HW1
# Question 5

# Write a program to that prompts the user to enter their first name. It then prints whether or not their
# name is a palindrome.

wordInput = input("ENTER YOUR FIRST NAME TO SEE IF ITS A PALINDROME:")
n = len(wordInput)


def isPalidrome(word, start):
    end = len(word) - 1
    if start >= end - start: return True
    word = list(word)
    if word[start] != word[end - start]: return False
    return isPalidrome(word, ++start)


print(isPalidrome(wordInput, n))

