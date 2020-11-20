# Shantanu Jhaveri
# ITP 449 Fall 2020
# HW2
# Question 3

# Write a program to ask the user to enter a password. Then check to see if it is a valid password
# based on these requirements
#   a. Must be at least 8 characters long
#   b. Must contain both uppercase and lowercase letters
#   c. Must contain at least one number between 0-9
#   d. Must contain a special character -!,@,#,$


def passLength(password):
    if len(password) < 8:
        return False
    else:
        return True


def passCase(password):
    passwordArray = []
    for i in password:
        if i.isupper():
            passwordArray.append(1)
        if i.islower():
            passwordArray.append(0)
    if 1 not in passwordArray or 0 not in passwordArray:
        return False
    else:
        return True


def passSym(password):
    if "!" not in password and "@" not in password and "#" not in password and "$" not in password:
        return False
    else:
        return True


def passNum(password):
    passwordArray = []
    for i in password:
        if i.isdigit():
            passwordArray.append("d")
        if i.isalpha():
            passwordArray.append("a")
    if "a" not in passwordArray or "d" not in passwordArray:
        return False
    else:
        return True


def fun_main():
    initial = True
    password = input("PLEASE ENTER A PASSWORD WITH THE FOLLOWING REQUIREMENTS\n"
                     "\tA. MUST BE AT LEAST 8 CHARACTERS LONG\n"
                     "\tB. MUST CONTAIN BOTH UPPERCASE AND LOWERCASE LETTERS\n"
                     "\tC. MUST CONTAIN AT LEAST ONE NUMBER BETWEEN 0-9\n"
                     "\tD. MUST CONTAIN A SPECIAL CHARACTER -!,@,#,$\n"
                     "PASSWORD: ")
    while initial:
        if passSym(password) and passLength(password) and passNum(password) and passCase(password):
            print("PASSWORD VALID. ACCESS GRANTED")
            initial = False
        else:
            print("PASSWORD INVALID. PLEASE TRY AGAIN")
            password = input('PASSWORD: ')
            initial = True


fun_main()

