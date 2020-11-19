# Shantanu Jhaveri
# ITP 449 Fall 2020
# HW1
# Question 4

# Write a program that prompts the user to enter a loan amount, annual interest rate, and number of
# years for a car loan. Then it prints the monthly payment amount.

loanAmount = float(input("ENTER A LOAN AMOUNT: "))
i = float(input("ENTER AN ANNUAL INTEREST RATE: ")) / 12 * 0.01
t = float(input("ENTER NUMBER OF YEARS FOR THE LOAN: ")) * 12


# based on the equation given in the document, but for some reason has the wrong
# answer

def pmt(loanAmount, i, t):
    monthlyPayments = float((loanAmount * i * ((1 + i) ** t))
                            /
                            (((1 + i) ** t) - 1))

    # monthlyPayments = loanAmount * (i/(1-(1+i)**(-t))) * 1/(1+i)
    return monthlyPayments


print(i)
print(t)
print(pmt(loanAmount, i, t))
