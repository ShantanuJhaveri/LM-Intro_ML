# Shantanu Jhaveri
# ITP 449 Fall 2020
# HW2
# Question 2

# Ask the user to enter two positive integers between 1 and 100. Read those integers. Then
# output a multiplication table of the first number times the second number.

while True:
    try:
        x = int(input("ENTER THE FIRST NUMBER: "))
        y = int(input('ENTER THE SECOND NUMBER: '))


        def tables(x, y):
            for i in range(1, y + 1):
                mult = x * i
                print(str(x) + " x " + str(i) + "\t=\t" + str(mult))

        tables(x, y)

        break
    except ValueError:
        print("NOT VALID INPUT, TRY AGAIN")
