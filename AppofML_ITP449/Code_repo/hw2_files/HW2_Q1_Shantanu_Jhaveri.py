# Shantanu Jhaveri
# ITP 449 Fall 2020
# HW2
# Question 1

# Write a program to compute and print all possible combinations of change for $1.
# Denominations to be considered – quarter, dime, nickel, penny
import numpy as np

import math

change = 100
for q in range(math.floor(change / 25) + 1):
    change = 100 - 25 * q
    for d in range(math.floor(change / 10) + 1):
        # print(q, 'Quarters &', d, 'Dimes will be', 25*q + 10*d, 'cents!')
        change = 100 - 25 * q - 10 * d
        for n in range(math.floor(change / 5) + 1):
            change = 100 - 25 * q - 10 * d - 5 * n
            for c in range(math.floor(change) + 1):
                change = 100 - 25 * q - 10 * d - 5 * n - c
                print(q, ' quarters, ', d, ' dimes, ', n, ' nickels, and ', c, ' pennies')

# works in cpp but doesnt work here ----------------------------------
# for quarters in range(0,ONE_DOLLAR-quarters,25):
#     TOTAL_MINUS_QUARTERS = ONE_DOLLAR - quarters*25
#     for dimes in range(0,TOTAL_MINUS_QUARTERS-dimes+10,10):
#         TOTAL_MINUS_Q_D = TOTAL_MINUS_QUARTERS - dimes*10
#         for nickels in range(0, TOTAL_MINUS_Q_D - nickels+ 5,5):
#             cents = TOTAL_MINUS_Q_D - nickels*5
#             print(quarters, dimes, nickels, cents)
# --------------------------------------------------------------------

# doesnt work at all -------------------------------------------------
# for i in range(0, ONE_DOLLAR, 25):
#     quarters += 1
#     for j in range(0, ONE_DOLLAR - (quarters * 25), 10):
#         dimes += 1
#         for k in range(0, ONE_DOLLAR - (quarters * 25) - (dimes * 10), 5):
#             nickels += 1
#             cents = ONE_DOLLAR - (quarters * 25) - (dimes * 10) - (nickels * 5)
#             print(quarters, dimes, nickels, cents)
# -------------------------------------------------------------------
