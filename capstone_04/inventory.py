# Task 32 - Capstone Project IV - OOP
# Compulsory Task
# Project Name: Inventory System
# inventory.py
# Author: Eddy Chan, Chi-wai
# Date: 22 December 2022
#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        # pass
        '''
        In this function, you must initialise the following attributes:
            ● country,
            ● code,
            ● product,
            ● cost, and
            ● quantity.
        '''
        
        # Set the attribute "country" of the class "Shoe" to the parameter "country"
        self.country = country
        # Set the attribute "code" of the class "Shoe" to the parameter "code"
        self.code = code
        # Set the attribute "product" of the class "Shoe" to the parameter "product"
        self.product = product
        # Set the attribute "cost" of the class "Shoe" to the parameter "cost"
        self.cost = cost
        # Set the attribute "quantity" of the class "Shoe" to the parameter "quantity"
        self.quantity = quantity
        
    def get_cost(self):
        # pass
        '''
        Add the code to return the cost of the shoe in this method.
        '''
        # Return the attribute "cost" of the class "Shoe"
        return self.cost

    def get_quantity(self):
        # pass
        '''
        Add the code to return the quantity of the shoes.
        '''
        # Return the attribute "quantity" of the class "Shoe"
        return self.quantity

    def __str__(self):
        # pass
        '''
        Add a code to return a string representation of a class.
        '''
        # Return the string representation of the class "Shoe"
        return f"{self.country},{self.code},{self.product},{self.cost},{self.quantity}"


#######################################################################################################################
#
# Import os, copy, tabulate library
# # https://pypi.org/project/tabulate/
# pip install tabulate (required)
#
import os, copy
from tabulate import tabulate
#
#######################################################################################################################
#
# Set environment variables
#
# Set the variable "current_directory" to store the current directory path
# Replace the backslash of the variable "current_directory" with a dash
current_directory = os.getcwd().replace("\\", "/")
# Set a variable "inventory_file" to the text file of the inventory
inventory_file = "inventory.txt"
# Set a variable "display_width" to 120 for display purpose
display_width = 120
# Set a variable "dotted_line_separator" to a dotted line separator for display purposes
dotted_line_separator = f"{'-' * display_width}"
# Set a variable "double_dash_separator" to a dotted line separator for display purposes
double_dash_separator = f"{'=' * display_width}"
# Set the list "shoe_header" to store the default value of the header of the shoes
shoe_header = ["Country", "Code", "Product", "Cost", "Quantity"]
#
#
#######################################################################################################################
#
# Self-defined function:
# START: get_one_shoe
#
# Create a function "get_one_shoe" with the parameter "shoe_index" to return the list "one_shoe_list"
#
def get_one_shoe(shoe_index):
    # Set a list "shoe_list" to store the list of the "Shoe" object by calling a function "capture_shoes"
    shoe_list = capture_shoes()
    # Set a list "one_shoe_list" to empty
    one_shoe_list = []
    # If the list "shoe_list" is not empty and the length of the list "shoe_list" is greater than the parameter "shoe_index",
    # set the list "one_shoe_list" to the list of the "Shoe" object with the parameter "shoe_index" 
    if shoe_list and len(shoe_list) > shoe_index:
       one_shoe_list = shoe_list[shoe_index]    
    # Return the list "one_shoe_list"
    return one_shoe_list
#
# END: get_one_shoe
#
#######################################################################################################################
#
# START: print_shoe_result
#
# Create a function "print_shoe_result" with the parameters "shoe_main_header", "shoe_header" and "shoe_body" 
# to print the table of the shoes with the library function "tabulate"
#
def print_shoe_result(shoe_main_header, shoe_header, shoe_body):
    # Print a double-dash separator
    print(f"{double_dash_separator}")
    # Print the parameter "shoe_main_header" with the required spaces   
    print(f"{ ' ' * ((display_width - len(shoe_main_header))  // 2) }  {shoe_main_header}".upper())
    # Print double dash separator 
    print(f"{double_dash_separator}\n")
    # Print the parameter "shoe_body" and "shoe_header" with the library function "tabulate"
    print(tabulate(shoe_body, shoe_header, tablefmt='psql', showindex=False, intfmt=',')) 
    # print a new line
    print("\n")
#
#
# END: print_shoe_result
#
#######################################################################################################################
#
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
        "░██████╗  ██╗░░██╗  ░█████╗░  ███████╗  ░██████╗",
        "██╔════╝  ██║░░██║  ██╔══██╗  ██╔════╝  ██╔════╝",
        "╚█████╗░  ███████║  ██║░░██║  █████╗░░  ╚█████╗░",
        "░╚═══██╗  ██╔══██║  ██║░░██║  ██╔══╝░░  ░╚═══██╗",
        "██████╔╝  ██║░░██║  ╚█████╔╝  ███████╗  ██████╔╝",
        "╚═════╝░  ╚═╝░░╚═╝  ░╚════╝░  ╚══════╝  ╚═════╝░"
    ]
    # Print a double dash separator with the variable "double_dash_separator"
    print(f"\n{double_dash_separator}\n")
    # Use for-loop to print each element "line" in the list "logo_list"
    for line in logo_list:
        # Print the element of line with the required spaces
        print(f"{' ' * ((display_width - len(line))//2) }{line}")
    # Set a variable "menu_header" to store the menu header
    menu_header = "==Inventory System=="
    # Set a variable "menu_header_with_space" to store the menu header with space
    menu_header_with_space = " ".join([character.upper() for character in menu_header])
    # Print the variable "menu_header_with_space" with the required spaces
    print(f"\n{' ' * ((display_width - len(menu_header_with_space))//2) }{menu_header_with_space}")    
    # Print a double dash separator with the variable "double_dash_separator"
    print(f"\n{double_dash_separator}\n")
#
# END: print_banner
#
#######################################################################################################################

#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
# Set a list "shoe_list" to store the list of the "Shoe" objects
shoe_list = []


#==========Functions outside the class==============
def read_shoes_data():
    # pass
    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object to the shoe list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''
    
#######################################################################################################################
# 
# START: read_shoes_data
# 
    # Set a list "inventory_list" to empty (2D list)
    inventory_list = []
    # Use try and except block to read the text file "inventory.txt" as a file object
    try:
        with open(f"{current_directory}/{inventory_file}", "r") as file:
            # Set the list "inventory_list" to store all the split elements "inventory_line" in the "file" object 
            # (except the index 0 is not stored)
            inventory_list = [inventory_line.strip().split(",") for index, inventory_line in enumerate(file) if index != 0]
    # If it fails to load the text file "inventory.txt", please the message to notify the user 
    # for checking the current directory and the file location of the text file
    except:
        print(f"Fail to load the text file {inventory_file}.\nPlease check the current directory and the file location of the text file {inventory_file}.\n")
        exit()
    # Return the list "inventory_list"
    return inventory_list
# 
# END: read_shoes_data
#
#######################################################################################################################

def capture_shoes():
    # pass
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''
#######################################################################################################################
#
# START: capture_shoes
# 
    # Set the list "inventory_list" to store the 2d list of the text file "inventory.txt"
    # by calling the function read_shoes_data
    inventory_list = read_shoes_data()
    # Set a list "shoe_list" to empty
    shoe_list = []
    # If the list "inventory_list" is not empty, store the list of the "Shoe" object
    if inventory_list:
        # Use for-loop to store the list of the Shoe object with all the elements "inventory_line" of the list "inventory_list", 
        for index, inventory_line in enumerate(inventory_list):
            # Use the list "shoe_list" to store the "Shoe" objects
            # index of the list "inventory_line": Country, Code, Product, Cost, Quantity
            shoe_list.append(Shoe(inventory_line[0], inventory_line[1], inventory_line[2], inventory_line[3], inventory_line[4]))
    # Return the list "shoe_list"
    return shoe_list
#
# START: capture_shoes
#
#######################################################################################################################

def view_all():
    # pass
    '''
    This function will iterate over the shoe list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''
    
####################################################################################################################### 
#
# START: view_all
#
    # Set the list "shoe_list" to store the list of the "Shoe" objects
    shoe_list = capture_shoes()    
    # If the list "shoe_list" is not empty, print the inventory list of the shoes
    if shoe_list:
        # Set a 2d list "shoe_data" to store the list of the "Shoe" objects by splitting its string representation
        shoe_data = [str(shoe).strip().split(",") for shoe in shoe_list] 
        # Set a 2d list "shoe_data_copy" to copy the list "shoe_data" for display purpose
        shoe_data_copy = copy.deepcopy(shoe_data)
        # Use for-loop to format the index 3 and 4 of all the elements of the list "shoe_data_copy"
        for index, shoe in enumerate(shoe_data_copy):
            # Convert the data type of the index 3 and 4 of all the elements of the list "shoe_data_copy" to integer
            shoe_data_copy[index][3], shoe_data_copy[index][4] = int(shoe_data_copy[index][3]) , int(shoe_data_copy[index][4]) 
            # Add the variable "index" + 1 to the index 0 of all the elements of the list "shoe_data_copy"
            shoe_data_copy[index].insert(0, index + 1)
        # Set the variable "shoe_main_header" to store the main header of the table
        shoe_main_header = "List of inventory"
        # Set the list "shoe_header" to store the header of the "Shoe" table
        shoe_header = ["No.", "Country", "Code", "Product", "Cost", "Quantity"]
        # Print the shoe table by calling a function "print_shoe_result" 
        # with the parameters "shoe_main_header", "shoe_header", "shoe_data_copy"
        print_shoe_result(shoe_main_header, shoe_header, shoe_data_copy)
    # If it fails to load the text file "inventory.txt", please the message to notify the user 
    # for checking the current directory and the file location of the text file
    # and exit program
    else:
        print(f"No shoes data are captured in the text file {inventory_file}.\nPlease check the current directory and the file location of the text file {inventory_file}.\n")
        exit()
#
# START: view_all
#
#######################################################################################################################

def re_stock():
    # pass
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''
#######################################################################################################################
#
# START: re_stock
#
    # shoe_list = capture_shoes() 
    # Set a variable "item_number" to empty
    item_number = ""
    # Set a variable "number_of_shoes" to empty
    number_of_shoes = ""
    # Set a variable "is_confirmed" to empty
    is_confirmed = "" 
    # Set a variable "restock_again" to empty
    restock_again = ""
    # Set a variable "is_restocked" to False
    is_restocked = False 
    # Use while-loop to execute the following if/else statements if the condition is true
    while True: 
        # Set the list "shoe_list" to store the list of the "Shoe" objects
        shoe_list = capture_shoes() 
        # If the list "shoe_list" is not empty, execute the following if/else statements
        if shoe_list:           
            # Set a 2d list "shoe_data" to store the list of the "Shoe" objects by splitting its string representation        
            shoe_data = [str(shoe).strip().split(",") for shoe in shoe_list]  
            # Set a 2d list "shoe_data_copy" to copy the list "shoe_data" for display purpose
            shoe_data_copy = copy.deepcopy(shoe_data) 
            # Set a 2d list "shoe_data_update" to copy the list "shoe_data" for updating purpose
            shoe_data_update = copy.deepcopy(shoe_data)            
            # Use for-loop to format the index 3 and 4 of all the elements of the list "shoe_data_copy"
            for index, shoe in enumerate(shoe_data_copy):
                # Convert the data type of the index 3 and 4 of all the elements of the list "shoe_data_copy" to integer
                shoe_data_copy[index][3], shoe_data_copy[index][4] = int(shoe_data_copy[index][3]) , int(shoe_data_copy[index][4]) 
                # Add the variable "index" + 1 to the index 0 of all the elements of the list "shoe_data_copy"
                shoe_data_copy[index].insert(0, index + 1)
            # Set a variable "lowest_quantity" to store the minimum quantity of the shoe item of the list "shoe_data_copy"
            # by using lambda expression - comparing the 5th element of the list "shoe_data_copy"
            # Note: It prevents the missing items as they have the same quantities
            lowest_quantity = min(shoe_data_copy, key=lambda x : x[5])[5]
            # Set a list "shoe_result" to store the list of the shoes with the lowest quantity
            shoe_result = []  
            # Use for-loop to store the list of the shoes with the lowest quantity for all the elements of the list "shoe_data_copy"
            for index, shoe in enumerate(shoe_data_copy):
                # If the index 5 of the list "shoe_data_copy" is equal to the variable "lowest_quantity",
                # store the element "shoe_data_copy" to the list "shoe_result"
                if shoe_data_copy[index][5] == lowest_quantity:
                    shoe_result.append(shoe_data_copy[index])
            # If the list "shoe_result" is not empty, print the list of the inventory with the lowest quantity 
            if shoe_result: 
                # Set the variable "shoe_main_header" to store the main header of the table             
                shoe_main_header = "list of the inventory at the lowest quantity"
                # Set the list "shoe_header" to store the header of the "Shoe" table
                shoe_header = ["No.", "Country", "Code", "Product", "Cost", "Quantity"] 
                # Print the shoe table by calling a function "print_shoe_result" 
                # with the parameters "shoe_main_header", "shoe_header", "shoe_result"
                print_shoe_result(shoe_main_header, shoe_header, shoe_result)                 
                # Set a list "shoe_result_index" to store the index of the item with the lowest quantity
                
                # for all the elements of the list "shoe_result"
                shoe_result_index = [ str(shoe_result[index][0]) for index, shoe in enumerate(shoe_result)]
            # If the list "shoe_result" is empty, print the message to notify the user 
            # that no records are matched with the code 
            else:
                print(f"No records are found.\n")   
            
            # If the variable "is_restocked" is true, execute the following if/else statements
            if not is_restocked:            
            # If the variable "item_number" is empty, ask the user to enter the item number to be restocked
                if item_number == "":                    
                    item_number = input(f"Please enter the item number [No.] to restock. (press Enter to exit)  :    ").strip()
                    # Print a new line
                    print("\n")       
                    # If the variable "item_number", use "break" to exit while=loop         
                    if item_number == "":
                        break 
                # If the variable "item_number" is not empty, ask the user to enter the quantity to be restocked
                else:  
                    # If the variable "item_number" is found in the list "shoe_result_index", execute the following if/else statements
                    if item_number in shoe_result_index:
                        # If the variable "number_of_shoes" to empty, ask the user to enter the quantity to be restocked
                        if number_of_shoes == "":     
                            # Set the variable "number_of_shoes" to store the quantity restocked the user entered
                            number_of_shoes = input(f"Please enter the quantity to be restocked. (press Enter to exit)  :    ").strip()
                            # Print a new line
                            print("\n")
                            # If the variable "number_of_shoes" is empty, use "break" to exit while-loop
                            if number_of_shoes == "":
                                item_number = ""
                                break  
                        else:
                            # If the variable "number_of_shoes" is not empty and is a digit, execute the following if/else statements
                            if number_of_shoes != "" and number_of_shoes.isdigit():                            
                                # If the variable "number_of_shoes" (as an integer) is greater than 0, 
                                # ask the user to confirm the restocked quantity
                                if int(number_of_shoes) > 0:
                                    # If the variable "is_confirmed" is empty, ask the user to confirm the restocked quantity
                                    if is_confirmed == "":   
                                        # Set the variable "is_confirmed" to store the restocked quantity the user confirmed               
                                        is_confirmed = input(f"Please confirm to the restocked quantity (+{number_of_shoes}) for [No. {item_number}]. \n 1 - YES\n 2 - NO\t\t\n(press Enter to exit)  :    ").strip()
                                        # Print a new line
                                        print("\n") 
                                        # Set the variable "is_confirmed" as empty, and use "break" to exit the while-loop                       
                                        if is_confirmed == "":
                                            break
                                    # If the variable "is_confirmed" is not empty, execute the following if/else statements
                                    else:                                     
                                        # If the variable "is_confirmed" is "1", update the quantity of the item 
                                        if is_confirmed == "1": 
                                            # Set a variable "total_of_shoes" to store the updated quantity of the item
                                            # as the sum of the variable "number_of_shoes" and the index 4 elements of the list "shoe_data_update"
                                            total_of_shoes = int(number_of_shoes) +  int(shoe_data_update[int(item_number) - 1][4])
                                            # Set the index 4 elements of the list "shoe_data_update" to the variable "total_of_shoes"
                                            shoe_data_update[int(item_number) - 1][4] = str(total_of_shoes)
                                            # Set the list "shoe_header" to store the header of the "Shoe" table
                                            # and store into the 1st line of the text file inventory.txt
                                            shoe_header = ["Country", "Code", "Product", "Cost", "Quantity"]   
                                            # Insert the variable "shoe_header" to the index 0 of the list "shoe_data_update"
                                            shoe_data_update.insert(0, shoe_header)
                                            # Set a variable "shoe_update_text" to the joined elements of its list "shoe_data_update"
                                            shoe_update_text = "\n".join([ f"{','.join(shoe_data_update[index])}" for index, shoe in enumerate(shoe_data_update)])                                           

                                            # If the variable "is_restocked" is true, execute the following if/else statements
                                            if not is_restocked: 
                                                # Use try and except block to write the text file "inventory.txt" as the "file" object
                                                try:
                                                    with open(f"{current_directory}/{inventory_file}", "w") as file:  
                                                        # Write the variable "shoe_update_text" to the text file "inventory.txt"    
                                                        file.writelines(f"{shoe_update_text}")                                        
                                                    # Set a variable "one_shoe" to store 1 "Shoe" object for displaying updated item
                                                    one_shoe = get_one_shoe( int(item_number) - 1)
                                                    # If the variable "one_shoe" is not empty, print the detail of the restocked item
                                                    if one_shoe:
                                                        # Set a list "one_shoe_list" to the split variable "one_list
                                                        one_shoe_list = [str(one_shoe).split(",")]
                                                        # Store the index 3 of the list "one_shoe_list" with converted data type - integer        
                                                        one_shoe_list[0][3] = int(one_shoe_list[0][3])
                                                        # Store the index 4 of the list "one_shoe_list" with converted data type - integer
                                                        one_shoe_list[0][4] = int(one_shoe_list[0][4])
                                                        # Store the index 0 of the list "one_shoe_list" with converted data type - integer
                                                        # Add the variable "item_number" to the index 0 of the list "one_shoe_list"
                                                        one_shoe_list[0].insert(0, int(item_number))
                                                        # Set the variable "shoe_main_header" to store the main header of the table 
                                                        # with the variables "item_number" and "number_of_shoes"
                                                        shoe_main_header = f"Item - [{item_number}]: {number_of_shoes} restocked"
                                                        # Set the list "shoe_header" to store the header of the "Shoe" table
                                                        shoe_header = ["No.", "Country", "Code", "Product", "Cost", "Quantity"]
                                                        # Print the shoe table by calling a function "print_shoe_result" 
                                                        # with the parameters "shoe_main_header", "shoe_header", "one_shoe_list"
                                                        print_shoe_result(shoe_main_header, shoe_header, one_shoe_list)
                                                        # Set the variable "is_restocked" to true after restocked
                                                        is_restocked = True
                                                # If it fails to update the text file "inventory.txt", please the message to notify the user 
                                                # for checking the current directory and the file location of the text file
                                                # and exit program
                                                except:
                                                    print(f"Fail to update the text file {inventory_file}. Please check the current directory and the location of the text file {inventory_file}.\n")
                                                    exit()       
                                        # If the variable "is_confirmed" is "2", 
                                        # initialise the variables "number_of_shoes" and is_confirmed" 
                                        # Note: Ask the user to enter the number of shoes again
                                        elif is_confirmed == "2":                                    
                                            number_of_shoes = ""
                                            is_confirmed = ""
                                        # If the variable "is_confirmed" is empty, 
                                        # initialise the variables "item_number", "number_of_shoes" and is_confirmed" 
                                        # Note: Ask the user to enter the item number of the shoe
                                        elif is_confirmed != "1" or is_confirmed != "2":
                                        #     item_number = ""
                                        #     number_of_shoes = ""
                                            print(f"\nYou do not confirm the quantity of the shoes. Please try again.\n")
                                            is_confirmed = ""
                                        # If any other cases, use "break" to exit while-loop 
                                        else:
                                            break
                                # If the variable "number_of_shoes" is less than 1, set the variable "number_of_shoes" to empty
                                else:
                                    print("The number of shoes cannot be less than 1. Please try again.\n")
                                    number_of_shoes = ""
                            # If the variable "number_of_shoes" is not valid, set the variable "number_of_shoes" to empty
                            else:
                                print(f"You enter the invalid quantity of shoes. Please try again.\n")
                                number_of_shoes = ""
                    # If the variable "item_number" is not valid, set the variable "item_number" to empty          
                    else:
                        print("You enter the invalid item number. Please try again.\n")
                        item_number = ""
            # If the variable "is_restocked" is not true, execute the following if/else statements
            else:
                # If the variable "is_confirmed" is "1", ask the user to restock the quantity of another item or not
                if is_confirmed == "1":
                    # If the variable "restock_again" is empty, ask the user to restock the quantity of another item or not
                    if restock_again == "":
                        # Set a variable "restock_again" to store the user's option for restocking other items with the lowest quantity                                            
                        restock_again = input(f"Do you need to restock another item with the lowest quantity? \n1 - YES\n2 - NO\t\t\n(press Enter to exit)  :    ").strip()
                        # Print a new line
                        print("\n")
                        # Set the variable "restock_again" as empty, and use "break" to exit the while-loop
                        if restock_again == "":
                            break  
                    # If the variable "restock_again" is not empty, execute the following if/else statements
                    else:           
                        # If the variable "restock_again" is equal to "1", 
                        # set the variables "item_number", "number_of_shoes" and "is_confirmed", "restock_again" to empty
                        # and set the variable "is_restocked" to false
                        if restock_again == "1":
                            item_number = ""
                            number_of_shoes = ""
                            is_confirmed = ""
                            restock_again = "" 
                            is_restocked = False                                         
                        # If the variable "restock_again" is "2" or empty, 
                        # use "break" to exit while-loop                                            
                        elif restock_again == "2":
                            break
                        # If the variable "restock_again" is not "1" or "2", print the message to notify the user of the invalid option for restocking the item again
                        # Set the variable "restock_again" to empty                    
                        elif restock_again != "1" or restock_again != "2":                                                        
                            print(f"\nYou enter the invalid option for restocking item again. Please try again.\n")
                            restock_again = ""
                        # If any other cases, use "break" to exit while-loop 
                        else:
                           break
        # If it fails to load the text file "inventory.txt", please the message to notify the user 
        # for checking the current directory and the file location of the text file
        else:
            print(f"No shoes data are captured in the text file {inventory_file}.\nPlease check the current directory and the file location of the text file {inventory_file}.\n")
            break
#
# END: re_stock
#
#######################################################################################################################        
            
def search_shoe():
    # pass
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''
    
#######################################################################################################################
#
# START: search_shoe
#
    # Set the list "shoe_list" to store the list of the "Shoe" objects
    shoe_list = capture_shoes()
    # Set a variable "shoe_code" to empty
    shoe_code = ""
    # Set a variable "search_again" to empty
    search_again = ""
    # If the list "shoe_list" is not empty, execute the following if/else statements
    if shoe_list:        
        # Use while-loop to execute the following if/else statements if the condition is true
        while True:
            # Set a variable "shoe_code" to store the code of the shoe the user looked for
            shoe_code = input(f"Please enter the code of the shoes you looked for.\n(press Enter to exit)  :    ").strip()
            # Print a new line
            print('\n')            
            # If the variable "shoe_code" is not empty, execute the following if/else statements
            if shoe_code != "":               
                # Set a 2d list "shoe_data" to store the list of the "Shoe" objects by splitting its string representation 
                shoe_data = [str(shoe).strip().split(",") for shoe in shoe_list]  
                # Set a 2d list "shoe_data_copy" to copy the list "shoe_data" for display purpose
                shoe_data_copy = copy.deepcopy(shoe_data) 
                # Set a list "shoe_result" to store the list of the "searched" shoes                
                shoe_result = []  
                # Use for-loop to store the list of the "searched" shoes  for all the elements of the list "shoe_data_copy"
                for index, shoe in enumerate(shoe_data_copy):
                    # Convert the data type of the index 3 and 4 of all the elements of the list "shoe_data_copy" to integer
                    shoe_data_copy[index][3], shoe_data_copy[index][4] = int(shoe_data_copy[index][3]) , int(shoe_data_copy[index][4]) 
                    # Add the variable "index" + 1 to the index 0 of all the elements of the list "shoe_data_copy"
                    shoe_data_copy[index].insert(0, index + 1)
                    # If the index 2 of the list "shoe_data_copy" is equal to the variable "shoe_code",
                    # Add the element of the list "shoe_data_copy" in the list "shoe_result"
                    if shoe_data_copy[index][2].lower() == shoe_code.lower():
                        shoe_result.append(shoe_data_copy[index])
                # If the list "shoe_result" is not empty, print the list of the inventory that the code the user entered 
                if shoe_result:
                    # Set the variable "shoe_main_header" to store the main header of the table 
                    # with the variables "shoe_code"
                    shoe_main_header = f"Search Result - [{shoe_code}]"
                    # Set the list "shoe_header" to store the header of the "Shoe" table 
                    shoe_header = ["No.", "Country", "Code", "Product", "Cost", "Quantity"]
                    # Print the shoe table by calling a function "print_shoe_result" 
                    # with the parameters "shoe_main_header", "shoe_header", "shoe_result"
                    print_shoe_result(shoe_main_header, shoe_header, shoe_result)
                # If the list "shoe_result" is empty, print the message to notify the user 
                # that no records are matched with the code 
                else:
                    print(f"No records are matched with your code {shoe_code}.\n")               
                # Set a variable "search_again" to store the user's option for searching again  
                search_again = input(f"Do you need to search the shoes again? \n1 - YES\n2 - NO\t\t\n(press Enter to exit)  :    ").strip()
                print("\n")
                # Set the variable "shoe_code" to empty after searched
                shoe_code = ""
                # If the variable "search_again" is not empty and is a digit, execute the following if/else statements
                if search_again != "" and search_again.isdigit():
                    # If the variable "search_again" is "1", 
                    # initialise the variables "shoe_code" and "search_again" to empty                    
                    if search_again == "1":
                        shoe_code = ""
                        search_again = ""
                    # If the variable "search_again" is, use "break" to exit the while-loop
                    elif search_again == "2" or search_again == "":
                        break
                # If the variable "search_again" is empty, use "break" to exit while-loop
                elif search_again == "":
                    break
                # If any other case, print the message to notify the user of the invalid option
                else:
                    print("You enter the invalid option. Please try again.\n")                   
            # If the variable "shoe_code" is empty, use "break" to exit the while-loop
            elif shoe_code == "":
                break
            # If any other case, print the message to notify the user of the invalid code
            else:
                print("You do not enter invalid code of the shoes. \n")
    # If it fails to load the text file "inventory.txt", please the message to notify the user 
    # for checking the current directory and the file location of the text file
    else:
        print(f"No shoes data are captured in the text file {inventory_file}.\nPlease check the current directory and the file location of the text file {inventory_file}.\n")
#
#
# END: search_shoe
#
#######################################################################################################################

def value_per_item():
    # pass
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''

#######################################################################################################################
#
# START: value_per_item
#
    # Set the list "shoe_list" to store the list of the "Shoe" objects
    shoe_list = capture_shoes()
    # If the list "shoe_list" is not empty, execute the following if/else statements
    if shoe_list:
        # Set a 2d list "shoe_data" to store the list of the "Shoe" objects by splitting its string representation 
        shoe_data = [str(shoe).strip().split(",") for shoe in shoe_list]       
        # Set a 2d list "shoe_data_copy" to copy the list "shoe_data" for display purpose
        shoe_data_copy = copy.deepcopy(shoe_data)    
        # Use for-loop to store the list of the shoes with the variable "shoe_value" for all the elements of the list "shoe_data_copy"
        for index, shoe in enumerate(shoe_data_copy):
            # Convert the data type of the index 3 and 4 of all the elements of the list "shoe_data_copy" to integer
            shoe_data_copy[index][3], shoe_data_copy[index][4] = int(shoe_data_copy[index][3]) , int(shoe_data_copy[index][4]) 
            shoe_value = int(shoe_list[index].get_cost()) * int(shoe_list[index].get_quantity())
            # Add the variable "index" to the index 0 of all the elements of the list "shoe_data_copy"
            shoe_data_copy[index].insert(0, index + 1)
            # Add the variable "shoe_value" to the last index of all the elements of the list "shoe_data_copy"
            shoe_data_copy[index].append(shoe_value)
        # Set the variable "shoe_main_header" to store the main header of the table 
        shoe_main_header = f"Total value of the inventory"
        # Set the list "shoe_header" to store the header of the "Shoe" table
        shoe_header = ["No.", "Country", "Code", "Product", "Cost (C)", "Quantity (Q)", "Value (C x Q)"]
        # Print the shoe table by calling a function "print_shoe_result" 
        # with the parameters "shoe_main_header", "shoe_header", "shoe_data_copy"
        print_shoe_result(shoe_main_header, shoe_header, shoe_data_copy)        
    # If it fails to load the text file "inventory.txt", please the message to notify the user 
    # for checking the current directory and the file location of the text file
    else:
        print(f"No shoes data are captured in the text file {inventory_file}.\nPlease check the current directory and the file location of the text file {inventory_file}.\n")
#
# END: value_per_item
#
#######################################################################################################################

def highest_qty():
    pass
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''
#######################################################################################################################
#
# START: highest_qty
#
    # Set the list "shoe_list" to store the list of the "Shoe" objects
    shoe_list = capture_shoes()
    # If the list "shoe_list" is not empty, execute the following if/else statements
    if shoe_list:
        # Set a 2d list "shoe_data" to store the list of the "Shoe" objects by splitting its string representation 
        shoe_data = [str(shoe).strip().split(",") for shoe in shoe_list]        
        # Set a 2d list "shoe_data_copy" to copy the list "shoe_data" for display purpose
        shoe_data_copy = copy.deepcopy(shoe_data)
        # Use for-loop to store the list of the shoes at the highest quantity with the variable "shoe_value" 
        # for all the elements of the list "shoe_data_copy"
        for index, shoe in enumerate(shoe_data_copy):
            # Convert the data type of the index 3 and 4 of all the elements of the list "shoe_data_copy" to integer
            shoe_data_copy[index][3], shoe_data_copy[index][4] = int(shoe_data_copy[index][3]) , int(shoe_data_copy[index][4]) 
            # Add the variable "index" + 1 to the index 0 of all the elements of the list "shoe_data_copy"
            shoe_data_copy[index].insert(0, index + 1)
        # Set a variable "highest_quantity" to store the maximum quantity of the shoe item of the list "shoe_data_copy"
        # by using lambda expression - comparing the 5th element of the list "shoe_data_copy"
        # Note: It prevents the missing items as they have the same quantities
        highest_quantity = max(shoe_data_copy, key=lambda x : x[5])[5]
        # Set a list "shoe_result" to store the list of the shoes with the highest quantity
        shoe_result = []
        # Use for-loop to store the list of the shoes at the highest quantity with the variable "shoe_value" 
        # for all the elements of the list "shoe_data_copy"
        for index, shoe in enumerate(shoe_data_copy):
            # If the index 5 of the list "shoe_data_copy" is equal to the variable "highest_quantity",
            # store the element "shoe_data_copy" to the list "shoe_result
            if shoe_data_copy[index][5] == highest_quantity:
                shoe_result.append(shoe_data_copy[index])
        # If the list "shoe_result" is not empty, print the list of the inventory with the highest quantity 
        if shoe_result:   
            # Set the variable "shoe_main_header" to store the main header of the table
            shoe_main_header = f"Item being for sale"
            # Set the list "shoe_header" to store the header of the "Shoe" table
            shoe_header = ["No.", "Country", "Code", "Product", "Cost", "Quantity"]
            # Print the shoe table by calling a function "print_shoe_result" 
            # with the parameters "shoe_main_header", "shoe_header", "shoe_result"
            print_shoe_result(shoe_main_header, shoe_header, shoe_result)            
        # If the list "shoe_result" is empty, print the message to notify the user 
        # that no records are matched with the code 
        else:
            print(f"No records are found.\n")
    # If it fails to load the text file "inventory.txt", please the message to notify the user 
    # for checking the current directory and the file location of the text file
    else:
        print(f"No shoes data are captured in the text file {inventory_file}.\nPlease check the current directory and the file location of the text file {inventory_file}.\n")
#
# END: highest_qty
#
#######################################################################################################################

#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''
#######################################################################################################################
#
# START: Main Menu
#

# Set a variable "is_print_banner" as true, print the banner the first time
is_print_banner = True
# Use while-loop to execute the following if/else statements if the condition is true
while True:
    # If the variable "is_print_banner" is true, print the banner by calling a function "print_banner"
    if is_print_banner:  
        print_banner()
    # Set a variable "menu_option" to store the user's option for the main menu
    menu_option = input(f"\nPlease select an option: \n 1 - Check inventory \n 2 - Restock item \n 3 - Search shoe \n 4 - Inventory value \n 5 - Item being for sale \n(press Enter to exit)  :    ").strip()
    # Print a new line
    print("\n")
    # If the variable "menu_option" is empty and is a digit, execute the following if/else statements
    if menu_option != "" and menu_option.isdigit():
        # If the variable "menu_option" is "1", call the function "view_all"
        if menu_option == "1":
            view_all()
        # If the variable "menu_option" is "2", call the function "re_stock"
        elif menu_option == "2":
            re_stock()
        # If the variable "menu_option" is "3", call the function "search_shoe" 
        elif menu_option == "3":
            search_shoe()
        # If the variable "menu_option" is "4", call the function "value_per_item" 
        elif menu_option == "4":
            value_per_item()
        # If the variable "menu_option" is "5", call the function "highest_qty" 
        elif menu_option == "5":
            highest_qty()
        # If any other case, print the message to notify the user of the invalid option
        else:
            print("You enter an invalid option. Please enter an option from 1 - 5.\n")
    # If the variable "menu_option" is empty, use "break" to exit while-loop
    elif menu_option == "":
        break
    # If any other case, print the message to notify the user of the invalid option
    else:
        print("You enter an invalid option. Please enter an option from 1 - 5.\n")
    # Set the variable "is_print_banner" to false if the operation is done
    is_print_banner = False
#
# END: Main Menu
#
#######################################################################################################################
