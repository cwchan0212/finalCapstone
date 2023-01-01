# Task 12 - Capstone Project I - Variables and Control Structures
# Compulsory Task 1 (Revised)
# Project Name: Financial Calculator
# finance_calculators.py
# Author: Eddy Chan, Chi-wai
# Date: 6 December 2022
# -------------------------------------------------------------------------------------------------------------- #
# import math library
#
import math
#
# -------------------------------------------------------------------------------------------------------------- #
# Set environment variable 
#
# Set a variable "display_width" to 120 for display purpose
display_width = 120
# Set a variable "double_dash_seperator" to a dotted line separator for display purposes
double_dash_seperator = f"{'=' * display_width}"
#
# -------------------------------------------------------------------------------------------------------------- #
# Self-defined functions
# -------------------------------------------------------------------------------------------------------------- #
# START: print_banner
# 
# Reference: ASCII Text Art Generator
# https://fsymbols.com/generators/carty/
#
# Create a function "print_banner" to print the banner of the system 
# 
def print_banner():
    # Set a list "logo_list" to store each line of the logos
    logo_list = [
    "███████ ██ ███    ██  █████  ███    ██  ██████ ██  █████  ██      ",
    "██      ██ ████   ██ ██   ██ ████   ██ ██      ██ ██   ██ ██      ",
    "█████   ██ ██ ██  ██ ███████ ██ ██  ██ ██      ██ ███████ ██      ",
    "██      ██ ██  ██ ██ ██   ██ ██  ██ ██ ██      ██ ██   ██ ██      ",
    "██      ██ ██   ████ ██   ██ ██   ████  ██████ ██ ██   ██ ███████ ",
    "                                                                                   ",                                                                                   
    " ██████  █████  ██       ██████ ██    ██ ██       █████  ████████  ██████  ██████  ",
    "██      ██   ██ ██      ██      ██    ██ ██      ██   ██    ██    ██    ██ ██   ██ ",
    "██      ███████ ██      ██      ██    ██ ██      ███████    ██    ██    ██ ██████  ",
    "██      ██   ██ ██      ██      ██    ██ ██      ██   ██    ██    ██    ██ ██   ██ ",
    " ██████ ██   ██ ███████  ██████  ██████  ███████ ██   ██    ██     ██████  ██   ██ ",
    ]   
    # Print a double dash separator with the variable "double_dash_seperator"
    print(f"\n{double_dash_seperator}\n")
    # Use for-loop to print each element "line" in the list "logo_list"
    for line in logo_list:
        # Set the variable "logo_line" to store the elements of the line with the required spaces
        logo_line = f"{' ' * ((display_width - len(line))//2) }{line}"
        # Print the colored text of the logo by calling the function "colored_text"
        print(f"{colored_text('bold', f'{logo_line}')}")
        # print(f"{' ' * ((display_width - len(line))//2) }{line}")
    # Set a variable "menu_header" to store the menu header
    menu_header = "==help you calculate=="
    # Set a variable "menu_header_with_space" to store the menu header with space
    menu_header_with_space = " ".join([character.upper() for character in menu_header])
    # Print the variable "menu_header_with_space" with the required spaces
    print(f"\n{' ' * ((display_width - len(menu_header_with_space))//2) }{colored_text('bold',f'{menu_header_with_space}')}")    
    # Print a double dash separator with the variable "double_dash_seperator"
    print(f"\n{double_dash_seperator}\n")
#
# END: print_banner
# -------------------------------------------------------------------------------------------------------------- #
# Start: colored_text
#
# Create a function "colored_text" with the parameters "color" and "text" to return the colored string
def colored_text(color, text):
    # Set a dictionary "color_dictionary" to store the keys and values of the colors
    color_dictionary = {
        "black": "\033[30m",
        "blue": "\033[94m",
        "default": "\033[99m",
        "yellow": "\033[93m",
        "black": "\033[90m",
        "cyan": "\033[96m",
        "green": "\033[92m",
        "magenta": "\033[95m",
        "white": "\033[97m",
        "darkcyan": "\033[36m",
        "red": "\033[91m",
        "bold": "\033[1m",
        "italic": "\033[3m",
        "underline": "\033[4m",
        "blink": "\033[6m",
        "end": "\033[0m",
    }
    # Return the colored string with the parameter "text" and the values of the dictionary "color_dictionary" 
    return f"{color_dictionary[color]}{text}{color_dictionary['end']}"
#
# END: colored_text
# -------------------------------------------------------------------------------------------------------------- #
# Start: check_input_number
#
# Create a function "check_input_number" with the parameter "number_string" to check whether the number is a string, integer or float
# Return 1: integer, 0: float, -1: string
def check_input_number(number_string):
    # If the parameter "number_string" is an integer, return 1
    if str(number_string).isdigit():
        # Return 1 as it is an integer
        return 1
    # If the parameter "number_string" is not an integer, test it as a float or string
    else:
        # Use try-catch block to test the parameter as float or string
        try:
            # try to convert the data type of the parameter "number_string"
            float(str(number_string))
            # Return 0 as it is a float
            return 0
        # If it is an exception, return -1 as it is a string
        except:
            # Return -1 as it is a string
            return -1
#
# END: check_input_number
# -------------------------------------------------------------------------------------------------------------- #
# Set global variables
# -------------------------------------------------------------------------------------------------------------- #
# Set a 2d list "investment_list" to store the query strings and the value the user entered for the investment option 
investment_list = [
    [f"Please enter the {colored_text('blue', 'amount of money'.upper())} that you deposit", ""],
    [f"Please enter the number of {colored_text('blue', 'interest rate'.upper())}", ""],
    [f"Please enter the number of {colored_text('blue', 'year(s)'.upper())} you plan on investing", ""],
    [f"Please select the {colored_text('blue', 'type'.upper())} of interest", ""]
]
# Set a 2d list "bond_list" to store the query strings and the value the user entered for the bond_list option 
bond_list = [
    [f"Please enter the {colored_text('green', 'present value of the house'.upper())}", ""],
    [f"Please enter the number of {colored_text('green', 'interest rate'.upper())}", ""],
    [f"Please enter the number of {colored_text('green', 'month(s)'.upper())} you plan to take to repay the bond", ""]
]

# Set a variable "option" to empty
option = ""
# Set a list "investment_header_list" to store the items of the investment option
investment_header_list = ["deposit amount", "interest rate", "year", "interest type"]
# Set a list "bond_header_list" to store the items of the bond option
bond_header_list = ["present value of the house", "interest rate", "number of months"]

# Use while-loop to execute the following if/else statements if the condition is true
while True:
    # If the variable "option" is empty, execute the following if/else statements 
    if option == "":
        # Call a function "print_banner" to print the banner
        print_banner()
        # Set a variable "investment_option_statement" to store the statement of the investment option
        investment_option_statement = f"investment - to calculate the amount of interest you'll earn on your investment"
        # Set a variable "bond_option_statement" to store the statement of the bond option
        bond_option_statement = f"bond       - to calculate the amount you'll have to pay on a home loan"
        # Print the statement to ask the user to enter the option 
        print(f"\nChoose either {colored_text('blue','investment')} or {colored_text('green', 'bond')} from the menu below to proceed:\n\n\
        {colored_text('blue', investment_option_statement)}\n\
        {colored_text('green', bond_option_statement)}\n"
        )
        # Create a variable "option" to store the option the user entered
        option = input(f"[Enter {colored_text('blue', '1 - investment')}, {colored_text('green', '2 - bond')}, press {colored_text('bold', 'Enter - EXIT')}]:  ").strip()
        # Print a new line
        print(f"\n")
        # If the variable "option" is empty, use "break" to exit the while-loop
        if option == "":
            break
        # If the variable "option" is not empty, use "break" to exit the while-loop
        else:
            # If the variable "option" is "1", execute the following if/else statements 
            if option == "1":
                # Set the variable "count" to 0
                count = 0
                # When the variable "count" is less than 4, execute the following if/else statements 
                while count < 4:
                    # If the index 1 of the element "investment_list" is empty, ask the user to answer the queries of the element "investment_list"
                    if investment_list[count][1] == "":
                        # Set a variable "option_tag" to store the exit options of the investment option 
                        option_tag =  f"[press {colored_text('bold', 'Enter to exit')}]: " if count < 3 else f"[Enter {colored_text('bold', '1 - simple'.upper())}, {colored_text('bold', '2 - compound'.upper())}, press {colored_text('bold', 'Enter')} to exit]: "
                        # Set the index 1 of the element  "investment_list" to store the user input
                        investment_list[count][1] = input(f"{investment_list[count][0].strip()} {option_tag}:  ") 
                        # If the index 1 of the element "investment_list" is empty, use "exit()" to exit program
                        if investment_list[count][1].strip() == "":
                            exit()
                    # If the index 1 of the element "investment_list" is not empty, execute the following if/else statements 
                    else:
                        # If the variable "count" is less than 3, execute the following if/else statements for the first 3 elements of the list "investment_option"
                        if count < 3:
                            # If the index 1 of the element "investment_list" is a string, print the error message to the user for string input
                            # by calling the function "check_input_number" with the parameter the index 1 of the element "investment_list"
                            if check_input_number(investment_list[count][1]) == -1:
                                print(f"\n{colored_text('red', f'{investment_header_list[count].upper()}')} is not a number. Please try again.\n")
                                # Set the index 1 of the element "investment_list" to empty
                                investment_list[count][1] = ""
                            # If the index 1 of the element "investment_list" is not a string, check whether the user input is an integer or float 
                            else:
                                # If the variable "count" is less than or equal to 1, check whether the index 1 of the element "investment_list" is a positive number or not
                                if count <= 1:
                                    # If the index 1 of the element "investment_list" is less than or equal to 0, print the error message to the user for the negative input
                                    if float(investment_list[count][1]) <= 0:
                                        print(f"\n{colored_text('red', investment_header_list[count].upper())} is less than zero. Please try again.\n")
                                        # Set the index 1 of the element "investment_list" to empty
                                        investment_list[count][1] = ""
                                    # If the index 1 of the element "investment_list" is not less than or equal to 0, the variable "count" is added by 1
                                    else:
                                        count += 1
                                # If the variable "count" is equal to 2, check whether the index 1 of the element "investment_list" is a positive number or not
                                elif count == 2:
                                    # If the index 1 of the element "investment_list" is less than or equal to 0, print the error message to the user for the negative input
                                    if float(investment_list[count][1]) <= 0:
                                        print(f"\n{colored_text('red', investment_header_list[count].upper())} is less than zero. Please try again.\n")
                                        # Set the index 1 of the element "investment_list" to empty
                                        investment_list[count][1] = ""
                                    # If the index 1 of the element "investment_list" is not an integer (i.e. float), print the error message to the user for the non-whole number input
                                    # by calling the function "check_input_number" with the parameter the index 1 of the element "investment_list"
                                    elif check_input_number(investment_list[count][1]) == 0:
                                        print(f"\n{colored_text('red', investment_header_list[count].upper())} is not a whole number. Please try again.\n")
                                        # Set the index 1 of the element "investment_list" to empty
                                        investment_list[count][1] = ""
                                    # If the index 1 of the element "investment_list" is an integer (i.e. float), the variable "count" is added by 1
                                    else:
                                        count += 1
                        # If the variable "count" is not less than 3, execute the following if/else statements for the first 3 elements of the list "investment_option"
                        else:
                            # If the index 1 of the element "investment_list" is not "1" or "2", print the error message to the user for an invalid option
                            if investment_list[count][1] != "1" and investment_list[count][1] != "2":
                                print(f"\n{colored_text('red', investment_header_list[count].upper())} is not equal to 1 or 2. Please try again.\n")
                                # Set the index 1 of the element "investment_list" to empty
                                investment_list[count][1] = ""
                            # If the index 1 of the element "investment_list" is "1" or "2", the variable "count" is added by 1
                            else:
                                investment_list[count][1] = "simple" if investment_list[count][1] == "1" else "compound"
                                count += 1
                # If the variable "count" is 4, execute the following if/else statements
                if count == 4:
                    # Set the variables "deposit_amount", "interest_rate", "year", and "interest_type" to store the index 1 of all elements of the list "investment_list" 
                    deposit_amount, interest_rate, year, interest_type = [int(investment_item[1]) if check_input_number(investment_item[1]) == 1 else float(investment_item[1]) if check_input_number(investment_item[1]) == 0 else investment_item[1]for index, investment_item in enumerate(investment_list)]
                    # If the variable "interest_type" is "simple", set the variable "amount" to store the calculation at the simple interest rate
                    if interest_type == "simple":
                        amount = round(deposit_amount *(1 + (interest_rate/100) * year), 2)
                    # If the variable "interest_type" is "compound", set the variable "amount" to store the calculation at the compound interest rate
                    elif interest_type == "compound":
                        amount = round(deposit_amount * math.pow((1 + (interest_rate/100)), year), 2)
                    # Print the result of the calculation to the user and use "break" to exit the while-loop function
                    print(f"\nThe total amount of {colored_text('blue', 'principal and interest'.upper())} is R {colored_text('cyan', amount)} at {colored_text('cyan', interest_type)} interest rate of {colored_text('cyan', interest_rate)} % after {colored_text('cyan', year)} year(s) deposited.")
                    break
            # If the variable "option" is "2", execute the following if/else statements 
            elif option == "2":
                # Set the variable "count" to 0
                count = 0
                # When the variable "count" is less than 3, execute the following if/else statements 
                while count < 3:
                    # If the index 1 of the element "bond_list" is empty, ask the user to answer the queries of the element "bond_list"
                    if bond_list[count][1] == "":
                        # Set a variable "option_tag" to store the exit options of the bond option 
                        option_tag =  f"[press {colored_text('bold', 'Enter to exit')}]: "
                        # Set the index 1 of the element  "bond_list" to store the user input
                        bond_list[count][1] = input(f"{bond_list[count][0]} - {option_tag}").strip()
                        # If the index 1 of the element "bond_list" is empty, use "exit()" to exit program
                        if bond_list[count][1] == "":
                            exit() 
                    # If the index 1 of the element "bond_list" is not empty, execute the following if/else statements 
                    else:
                        # If the index 1 of the element "bond_list" is a string, print the error message to the user for string input
                        # by calling the function "check_input_number" with the parameter the index 1 of the element "bond_list"
                        if check_input_number(bond_list[count][1]) == -1:
                            print(f"\n{colored_text('red', bond_header_list[count]).upper()} is not a number. Please try again.\n")
                            # Set the index 1 of the element "bond_list" to empty
                            bond_list[count][1] = ""
                        # If the index 1 of the element "bond_list" is not a string, check whether the user input is a positive number or not 
                        else:
                            # If the variable "count" is less than or equal to 1, check whether the index 1 of the element "bond_list" is a positive number or not
                            if count <= 1:
                                # If the index 1 of the element "bond_list" is less than or equal to 0, print the error message to the user for the negative input
                                if float(bond_list[count][1]) <= 0:
                                    print(f"\n{colored_text('red', bond_header_list[count].upper())} is not a whole number. Please try again.\n")
                                    # Set the index 1 of the element "bond_list" to empty
                                    bond_list[count][1] = ""
                                # If the index 1 of the element "bond_list" is not less than or equal to 0, the variable "count" is added by 1
                                else:
                                    count += 1
                            # If the variable "count" is 2, check whether the index 1 of the element "bond_list" is a positive number or a whole number
                            elif count == 2:
                                # If the index 1 of the element "bond_list" is less than or equal to 0, print the error message to the user for the negative input
                                if float(bond_list[count][1]) <= 0:
                                    print(f"\n{colored_text('red', bond_header_list[count].upper())} is not a number. Please try again.\n")
                                    # Set the index 1 of the element "bond_list" to empty
                                    bond_list[count][1] = ""
                                # If the index 1 of the element "bond_list" is not an integer (i.e. float), print the error message to the user for the non-whole number input
                                # by calling the function "check_input_number" with the parameter the index 1 of the element "bond_list"
                                elif check_input_number(bond_list[count][1]) == 0:
                                    print(f"\n{colored_text('red', bond_header_list[count].upper())} is not a whole number. Please try again.\n")
                                    # Set the index 1 of the element "bond_list" to empty
                                    bond_list[count][1] = ""
                                # If the index 1 of the element "bond_list" is an integer (i.e. float), the variable "count" is added by 1
                                else:
                                    count += 1
                # If the variable "count" is 3, execute the following if/else statements
                if count == 3:
                    # Set the variables "present_value_of_the_house", "interest_rate", and "number_of_months" to store the index 1 of all elements of the list "bond_list" 
                    present_value_of_the_house, interest_rate, number_of_months = [int(bond_item[1]) if check_input_number(bond_item[1]) == 1 else float(bond_item[1]) if check_input_number(bond_item[1]) == 0 else bond_item[1] for index, bond_item in enumerate(bond_list)]
                    # Set the variable "amount" to store the calculation at the monthly repayment amount
                    amount = round(((interest_rate/100)/12) * present_value_of_the_house / (1 - math.pow((1 + ((interest_rate/100)/12)), (-number_of_months))), 2)
                    # Print the amount of repayment after a certain month(a) at the given interest rate and use "break" to exit while-loop
                    print(f"\nThe {colored_text('green', 'monthly repayment amount'.upper())} is R {colored_text('cyan', amount)} at {colored_text('cyan', interest_rate)} %.")
                    break
            # If the variable "option" is not "1" or "2", print the error message to the user
            else:
                print(f"\n{colored_text('red', 'Your investment option is not valid.')}\n")
                option = ""
