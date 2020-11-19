# Shantanu Jhaveri
# ITP 449 Fall 2020
# HW1
# Question 3

# Write a program that prompts the user to enter a month (as a number), then prints the name of the
# month and the number of days in that month.

month = int(input("ENTER THE MONTH AS A NUMBER: "))

monthNames = {
    1: "JANUARY",
    2: "FEBRUARY",
    3: "MARCH",
    4: "APRIL",
    5: "MAY",
    6: "JUNE",
    7: "JULY",
    8: "AUGUST",
    9: "SEPTEMBER",
    10: "OCTOBER",
    11: "NOVEMBER",
    12: "DECEMBER"
}


def calendarDay(month):
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        numOfDays = 31
    if month == 2:
        numOfDays = 28
    else:
        numOfDays = 30
    return numOfDays


def calendarName(month):
    return monthNames[month]


print(str(calendarName(month)) + ' HAS ' + str(calendarDay(month)) + ' DAYS')


