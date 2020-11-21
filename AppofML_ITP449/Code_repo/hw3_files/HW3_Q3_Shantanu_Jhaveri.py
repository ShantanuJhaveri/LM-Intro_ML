# Shantanu Jhaveri
# ITP 449 Fall 2020
# HW3
# Question 3

# Write a program that prompts the user to enter a loan amount, interest rate,
# and number of years for a car loan. Then it prints the monthly payment amount.

import numpy as np
import math
import matplotlib.pyplot as plt

# RECYCLED CODE FROM HW 1 Q4
loanAmount = float(
    30000
    # input("ENTER A LOAN AMOUNT: ")
)
i = float(
    4
    # input("ENTER AN ANNUAL INTEREST RATE: ")
) / 12 * 0.01
t = int(
    5
    # input("ENTER NUMBER OF YEARS FOR THE LOAN: ")
) * 12
monthlyPayments = float((loanAmount * i * ((1 + i) ** t))
                        /
                        (((1 + i) ** t) - 1))

monIntPaid = np.array([])
timeArray = np.array([])
loanArray = np.array([])

balance = 30000
interest = balance * i
TOT_interest = loanAmount * i

for j in range(0, t):
    outstand = balance - (j*monthlyPayments)
    total = balance + interest - monthlyPayments*j
    timeArray = np.append(timeArray, j)
    loanArray = np.append(loanArray, outstand)
    monIntPaid = np.append(monIntPaid, total)

#
myFig = plt.figure()
plt.suptitle('Jhaveri_Shantanu_HW3_Q3')
ax1 = myFig.add_subplot(2,2,1)
ax2 = myFig.add_subplot(2,2,2)
ax1.plot(timeArray, monIntPaid, markersize=3, marker='o', linestyle='-')
ax2.plot(timeArray, loanArray, markersize=3, marker='o', linestyle='-', color='red')
#
#

# plt.xlabel('Month')
# plt.ylabel('Loan Balance')
# finalplots[1].plot(timeArray, monIntPaid, marker=',')


plt.show()
