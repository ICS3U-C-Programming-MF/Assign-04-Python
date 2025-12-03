#!/usr/bin/env python3
# Created by Maximiliano Fairman
# Created on Nov 11th, 2025
# This program asks the user for two numbers.
# It then calculates and displays the
# Lowest Common Multiple of the two numbers.

print("")
print("Hello user")
print("Please input your 2 numbers.")
print("To get the lowest common multiple of them.")
print("")

keep_running = "yes"

while keep_running == "yes":

    # INPUT VALIDATION LOOP
    valid_input = False
    while not valid_input:
        try:
            num1 = int(input("Enter the first whole number: "))
            num2 = int(input("Enter the second whole number: "))

            if num1 <= 0 or num2 <= 0:
                print("Both numbers must be GREATER than zero. Try again.\n")
            else:
                valid_input = True

        except ValueError:
            print("ERROR: You must enter whole numbers only. Try again.\n")

    # --- COMPUTE LCM USING LOOPS ONLY ---
    if num1 > num2:
        lcm = num1
    else:
        lcm = num2

    while True:
        if (lcm % num1 == 0) and (lcm % num2 == 0):
            break
        else:
            lcm = lcm + 1

    # OUTPUT
    print("\nThe Lowest Common Multiple of", num1, "and", num2, "is:", lcm)

    # MENU
    print("\nWould you like to calculate another LCM?")
    keep_running = input("Enter 'yes' to continue or anything else to quit: ")

    if keep_running != "yes":
        print("\nThank you for using the LCM Calculator!")
