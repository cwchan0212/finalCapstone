# =====importing libraries===========
'''This is the section where you will import libraries'''
#
# Task 21 - Capstone Project II - Files
# Compulsory Task Part 1
# Compulsory Task Part 2 ****
# Project Name: Task Manager
# task_manager.py
# Author: Eddy Chan, Chi-wai
# Date: 12 December 2022
########################################################################################################################
#
# Compulsory Task Part 1
# START: Import library
#
import os
from datetime import datetime
#
# END: import library
#
########################################################################################################################
#
# Compulsory Task Part 1
# START: Set the environment variables
#
# Set the variable "current_directory" to store the current directory path
# Replace the backslash of the variable "current_directory" with a dash
current_directory = os.getcwd().replace("\\", "/")
# Set the variable "file_name" and store the text file name "user.txt"
user_file = "user.txt"
# Set the variable "task_file" and store the text file name "tasks.txt"
task_file = "tasks.txt"
# Set the variable "display_width" of the display width to 100
display_width = 120
# Set a variable "double_dash_separator" to a dotted line separator for display purpose
double_dash_separator = f"{'=' * display_width}"
# Set the list "task_header" and store the task header
task_header = ["Task:", "Assigned to:", "Date Assigned:", "Due Date", "Task Complete?", "Task Description:"]
# Set the variable "max_task_header_length" to the maximum length of the element in the list "task_header"
max_task_header_length = len(max(task_header, key=len))
# Set the variable "task_header_length" to 25 as the spaces are occupied by the task header 
task_header_length = 25
# Set the list "username_text_list" to store the default setting of the text file "user.txt"
username_text_list = [
    "admin, adm1n",
    "boss, b0ss"

]
# Set the list "task_text_list" to store the default setting of the text file "tasks.txt"
task_text_list = [
    "admin, Register Users with taskManager.py, Use taskManager.py to add the usernames and passwords for all team members that will be using this program., 10 Oct 2019, 20 Oct 2019, No",
    "admin, Assign initial tasks, Use taskManager.py to assign each team member with appropriate tasks, 10 Oct 2019, 25 Oct 2019, No",
    "boss, Meet the new customers, Discuss with them the detail of the new contracts, 14 Nov 2022, 31 Dec 2023, No",
    "boss, Visit the customers' shops and office, Seek their feedback on the company services, 16 Dec 2022, 30 Nov 2025, No"
]
########################################################################################################################
#
# Compulsory Task Part 1
# START: Create self-defined functions
########################################################################################################################
# Create a function "valid_date" to validate the date inputs with the parameters of "year_param", "month_param", "day_param"
#
def valid_date(year_param, month_param, day_param):
    # Use try-except to handle the exception of the date input
    try:
        # When the date input is valid, it returns true
        newDate = datetime(year_param, month_param, day_param)
        return True
    # When the date input is not valid, it returns false
    except ValueError:
        return False
#
# END: self-defined function
#
########################################################################################################################
#
# START: self-defined function - "get_username_list"
#
# Create a function "get_username_list" to get the list of usernames in the text file user.txt
#
def get_username_list():
    # Set a list "username_list" to empty
    username_list = []
    # Use try and except block to read the text file user.txt as the "file" object
    try:
        with open(f"{current_directory}/{user_file}", "r") as file:
            # Set the list "username_list" to store all the elements "user_line" in the "file" object
            username_list = [user_line.split(",")[0].strip() for user_line in file]
    # If it fails to load the text file user.txt, print the message to notify 
    # the user to check the current path and the location of the text file user.txt
    except:
        print(f"Fail to load the text file {user_file}. Please check the current path and the location of the text file {task_file}.\n")
    # Return the list "username_list"
    return username_list
#
# END: Create self-defined function - "get_username_list"
#
########################################################################################################################
# Create a function "print_banner" to print the banner of the system 
# 
def print_banner():
    # Set a list "logo_list" to store each line of the logos
    logo_list = [
    "########    ###     ######  ##    ##    ##     ##    ###    ##    ##    ###     ######   ######## ######## ",
    "   ##      ## ##   ##    ## ##   ##     ###   ###   ## ##   ###   ##   ## ##   ##    ##  ##       ##     ##",
    "   ##     ##   ##  ##       ##  ##      #### ####  ##   ##  ####  ##  ##   ##  ##        ##       ##     ##",
    "   ##    ##     ##  ######  #####       ## ### ## ##     ## ## ## ## ##     ## ##   #### ######   ######## ",
    "   ##    #########       ## ##  ##      ##     ## ######### ##  #### ######### ##    ##  ##       ##   ##  ",
    "   ##    ##     ## ##    ## ##   ##     ##     ## ##     ## ##   ### ##     ## ##    ##  ##       ##    ## ",
    "   ##    ##     ##  ######  ##    ##    ##     ## ##     ## ##    ## ##     ##  ######   ######## ##     ##",
    ]    
    
    # Print a double dash separator with the variable "double_dash_separator"
    print(f"\n{double_dash_separator}\n")
    # Use for-loop to print each element "line" in the list "logo_list"
    for line in logo_list:
        # Print the element of line with the required spaces
        print(f"{' ' * ((display_width - len(line))//2) }{line}")
    # Set a variable "menu_header" to store the menu header
    menu_header = "== Help you manage the tasks=="
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
# Create a function "restore_file" with the parameters "text_file_list" and "text_file" to restore the text file to default setting
def restore_file(text_file_list, text_file):
    # Create a variable "is_restored" to false
    is_restored = False
    # If the parameter "text_file_list" is not empty, try to write the text file
    if text_file_list:
        # Set the list "text_file_list" to store all reformatted elements "line" in the list "text_file_list" 
        text_file_list = [ f"{line}\n" if index != len(text_file_list) -1 else f"{line}" for index, line in enumerate(text_file_list) ]
        # Use try-except block to write the text file as the file object
        try: 
            with open(f"{current_directory}/{text_file}", "w") as file: 
                file.writelines(text_file_list)
                # Set the variable "is_restored" to true
                is_restored = True
        # If it fails to write the text file, print the message to notify the user
        except:
            print(f"Fail to load the text file {text_file}.\nPlease check the current directory and the file location of the text file {text_file}.\n")
    # Return the variable "is_restored"
    return is_restored
#
# End: Create self-defined function - restore_file
#
#######################################################################################################################
# 
# *********************************************************************************************************************
#
# Compulsory Task Part 2
# Set the variable "admin_login" to false
admin_login = False
#
# **********************************************************************************************************************
#
# END: set the environment variables
#
########################################################################################################################

# ====Login Section====
'''Here you will write code that will allow a user to log in.
    - Your code must read usernames and passwords from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file.
    - Use a while loop to validate your username and password.
'''

########################################################################################################################
#
# Compulsory Task Part 1
# START: Login Section
#
# Loading the default setting of the text file inventory.txt
#
# If it fails to restore the default setting of the text file, print the error message to notify the user 
# by calling the function "restore_file" with  the parameters "inventory_text_list" and "inventory_file"
# and use exit() to exit the program
if not restore_file(username_text_list, user_file) or not restore_file(task_text_list, task_file):
    print(f"Fail to load the default setting of the text files {user_file} or/and {task_file}.\n")
    exit()
########################################################################################################################
# Create an empty list "usernames" to store a list of usernames 
usernames = []
# Create an empty list "passwords" to store a list of passwords 
passwords = []
# Call a function to "print_banner" for login
print_banner()
# Set a variable "note" to store the note for the user
note = f"Note: All data will be restored to the default setting".upper()
# Print the variable "note" with the required spaces
print(f"{' ' * ((display_width - len(note)) // 2) } {note}\n")
#
print(f"Accounts for testing - \nusername: admin\t\tusername: boss\npassword: adm1n \tpassword: b0ss\n")
#
# Read the file "user.txt" as the "file" object
with open(f"{current_directory}/{user_file}", "r") as file:
    # User for-loop to store the username and passwords in the list "usernames" and the list "passwords"
    # for all the elements "line" in the "file" object
    for line in file:
        # If the variable "line" is not empty and comma in the variable "line", execute the following if/else statements
        if line and line.find(",") != -1:
        # Set the list "user_split" to store the part that is split by comma
            user_split = line.split(",")
            # Add the index 0 (first part) of "user_split" into the list "usernames"
            # The first part is the username, its leading and trailing spaces are removed
            usernames.append(user_split[0].strip())
            # Add the index 1 (second part) of "user_split" into the list "passwords"
            # The second part is the password, its leading and trailing spaces are removed
            passwords.append(user_split[1].strip())

# Set a variable "username_input" to empty
username_input = ""
# Set a variable "password_input" to empty
password_input = ""

# Set the variable "logged" to false for the login status
logged = False
# Use while-loop to execute the following statements if the condition of the variable "logged" is true 
while not logged:
    # If the variable "username_input" is empty, ask the user to enter the username
    if username_input == "": 
        # Ask the user to enter the username and store in the variable "username_input"
        username_input = input("Please enter your username: ").strip()
        # If the variable "username_input" is empty, use "break" to exit the while-loop
        if username_input == "":
            break
    # If the variable "username_input" is not empty, execute the following if/else statements
    else:
    # If the variable "password_input" is empty, ask the user to enter the password
        if password_input == "": 
            # Ask the user to enter the password and store in the variable "password_input"
            password_input = input("Please enter your password: ").strip()
            # If the variable "password_input" is empty, use "break" to exit the while-loop
            if password_input == "":
                break
        # If the variable "password_input" is not empty, execute the following if/else statements
        else:
            # If the variable "username_input" is found in the list "username", execute the following the statements
            if username_input in usernames:
                # Set the variable "index" to the position of the variable "username_input" in the list "usernames"
                index = usernames.index(username_input)
                # If the variable "password_input" is matched with the "index" element of the list "passwords",
                # execute the following statements     
                if password_input == passwords[index]:
                    #
                    # **********************************************************************************************************
                    #
                    # Compulsory Task Part 2
                    #
                    # Set the variable "admin_login" to True if the variable "username_input" is equal to "admin",
                    # otherwise it sets to false
                    admin_login = True if username_input == "admin" else False
                    #
                    # **********************************************************************************************************
                    #
                    # Set the variable "logged" to true after the new username is registered
                    # It leads to the exit of the while-loop
                    logged = True            
                    # Print a new line
                    print("\n")
                    # Print the welcome message to the user
                    print(f"Welcome back, {username_input}!\n")
                # If the user enters the incorrect username/password, print the error message to the user,
                # set the variables "username_input" and "password_input" to empty
                # Note: It does not reveal the specific type of error to the user due to security concern
                else:
                    print("Username and/or password are incorrect.\n")
                    username_input = ""
                    password_input = ""
                    # Use a break to stop the while-loop
                    # break
            # If the username is not found in the list "username", print the error message to the user,
            # set the variables "username_input" and "password_input" to empty
            # Note: It does not reveal the specific type of error to the user due to security concern
            else:
                print("Username and/or password are incorrect.\n")
                username_input = ""
                password_input = ""
                # Use a break to stop the while-loop
                # break

# If the variable "logged" is not true, exit the program
if not logged:
    exit()
#
# END: Login Section
#
########################################################################################################################

while True:
    # presenting the menu to the user and
    # Make sure that the user input is converted to lowercase.
    #
    # ******************************************************************************************************************
    #
    # Compulsory Task Part 2
    # Set the variable "register_user_option" to "r - Registering a user" if the variable "admin_login" is true,
    # otherwise it sets to false
    register_user_option = "r - Registering a user\n" if admin_login else ""
    # Set the variable "view_statistics_option" to "vs - View statistics" if the variable "admin_login" is true,
    # otherwise it sets to false
    view_statistics_option = "vs - View statistics\n" if admin_login else ""
    #
    # ******************************************************************************************************************
    #
    # Compulsory Task Part 2
    # Amend the variable "menu" by using the f-string
    menu = input(f"Select one of the following Options below:\n\
{register_user_option}\
a - Adding a task\n\
va - View all tasks \n\
vm - View my task\n\
{view_statistics_option}\
e - Exit\n\
:   ").lower()
    #
    # ******************************************************************************************************************
    #
    # Compulsory Task 2 requirement
    # If the variable "menu" is "r" and the variable "admin_login" is true, 
    # it displays the option of registering a user
    if menu == 'r' and admin_login:
    #
    # ******************************************************************************************************************
        # pass
        '''In this block, you will write code to add a new user to the user.txt file
        - You can follow the following steps:
            - Request input of a new username
            - Request input of a new password
            - Request input of password confirmation.
            - Check if the new password and confirmed password are the same.
            - If they are the same, add them to the user.txt file,
            - Otherwise, you present a relevant message.'''

########################################################################################################################
#
# Compulsory Task Part 1
# START: Registering a user
#
        # Print a new line
        print("\n")
        # Ask the user to enter a new username and store in the variable "new_username_input"
        new_username_input = input("Please enter a new username: ").strip()
        # # Ask the user to enter a new password and store in the variable "new_password_input"
        new_password_input = input("Please enter a new password: ").strip()        
        # Set the variable "username_added" to false for the registration status 
        username_added = False
        # If the variable "new_username_input" and the variable "new_password_input" are not blank,
        # execute the following statements
        if new_username_input and new_password_input: 
            # Use while-loop to execute the following statement if the condition of the variable "username_added" is true 
            while not username_added:
                # Ask the user to enter the password again for confirmation and store in the variable "new_confirmed_password_input"
                new_confirmed_password_input = input("Please enter a new password again: ").strip()   
                # If the variable "new_password_input" is matched with the variable "new_confirmed_password_input", 
                # it writes the new username and password with the separator (i.e. comma) in the text file "user.txt as the "file" object
                if new_password_input == new_confirmed_password_input:
                    with open(f"{current_directory}/{user_file}", "a") as file:
                        file.write(f"\n{new_username_input}, {new_password_input}")
                    # Print a new line
                    print("\n")
                    # Print the message to notify the user the new username registered successfully
                    print(f"The new username {new_username_input} is registered successfully.\n")
                    # Set the variable "username_added" to true after the new username is registered
                      # Set the variable "username_added" to true to exit the while-loop after adding a new username     
                    username_added = True
                # If the variable "new_password_input" is not matched with the variable "new_confirmed_password_input",
                # execute the following statements
                else:
                    # Print a new line
                    print("\n")
                    # Print the message to notify the user the confirmed that not matched.
                    print("The passwords are not matched. Please try again.")
                    # Ask the user to enter the new password again 
                    # if the confirmed password is not matched with the new password
                    new_password_input = input("Please enter a new password: ").strip() 
        # If the user does not enter the username or the password,
        # it prints the message to notify the user
        else:
            print("You do not enter username/password.\n")
#
# END: Registevariableuser
#
########################################################################################################################
        
    elif menu == 'a':
        # pass
        '''In this block, you will put code that will allow a user to add a new task to the task.txt file
        - You can follow these steps:
            - Prompt a user for the following: 
                - A username of the person to whom the task is assigned,
                - A title of a task,
                - A description of the task and 
                - the due date of the task.
            - Then get the current date.
            - Add the data to the file task.txt and
            - You must remember to include the 'No' to indicate if the task is complete.'''
        
########################################################################################################################
#
# Compulsory Task Part 1
# START: Adding a task
#
        # print a new line
        print("\n")        
        # Set the variable "task_added" to false for adding the task
        task_added = False
        # Set the variable "username_assigned" of the assigned username to an empty string
        username_assigned = ""
        # Set the variable "task_title" of the task title to an empty string 
        task_title = ""
        # Set the variable "task_description" of task description to an empty string
        task_description = ""
        # Set the variable "task_due_date" of the task due date to an empty string
        task_due_date = ""
        # Use while-loop to execute the following statement if the condition of the variable "task_added" is true 
        while not task_added:            
            # If the variable "username_assigned" is empty, ask the user to enter the username whom the task is assigned
            if not username_assigned:
            # Create a list "username_list" to store the list of username
                username_list = get_username_list()
                # Create a list "username_index" to store the ist of username index
                username_index = [str(index + 1) for index in range(len(username_list))]
                # create a variable "username_assigned_string" to empty 
                username_assigned_string = ""
                # Use for-loop to store the concatenate the list of username for display
                for index, username in enumerate(username_list):
                    username_assigned_string += f"  {username_index[index]} - {username_list[index]}\n"

                # Remove the leading and trailing spaces of the username to whom the task is assigned,
                # store it in the variable "username_assigned"
                # Note: the variable "username_assigned" is set to the number string first, 
                # finally it returns to the username and store in the user.text
                username_assigned = input(f"Please enter the number of the username whom the task is assigned\n{username_assigned_string}   :  ").strip()

                # If the variable "username_assigned" is empty, print the message to notify the user of the blank input
                if username_assigned == "":
                    print("The assigned username is blank.\n")  
                # If the username_assigned is not found in the list "username_list",
                # print the message to notify the user that the number of the assigned username, 
                # and set the variable "username_assigned" to empty
                elif username_assigned not in username_index:
                    username_assigned = ""
                    print("The number of the assigned username is not found in the list.\n") 
                # If any other case, set the variable "username_assigned" to  store the username 
                # at the index of the list "username_list"
                else:
                    username_assigned = username_list[int(username_assigned)-1]

            # If the variable "username_assigned" is not empty, proceed to check the variable "task_title"      
            else:
                # If the variable "task_title" is empty, ask the user to enter the title of the task
                if not task_title:
                    # Remove the leading and trailing spaces of the title of the task,
                    # store it in the variable "task_title"
                    task_title = input("Please enter a title of task: ").strip()   
                    # If the variable "task_title" is empty, print the message to notify the user
                    if task_title == "":
                        print("The title of task is blank.\n")   
                # If the variable "task_title" is not empty, proceed to check the variable "task_description"         
                else: 
                    # If the variable "task_description" is empty, ask the user to enter a description of the task
                    if not task_description:
                        # Remove the leading and trailing spaces of a description of the task,
                        # store it in the variable "task_description"
                        task_description = input("Please enter a description of task: ").strip()
                        # If the variable "task_description" is empty, print the message to notify the user
                        if task_description == "":
                            print("The description of task is blank.\n") 
                    # If the variable "task_description" is not empty, proceed to check the variable "task_due_date"    
                    else:
                        # If the variable "task_due_date" is empty, ask the user to enter the due date of the task
                        if not task_due_date:
                            # Remove the leading and trailing spaces of the due date of the task,
                            # store it in the variable "task_due_date"
                            task_due_date = input("Please enter a due_date of task - [DDMMYYYY]: ").strip()  
                            # If the variable "task_due_date" is empty, print the message to notify the user
                            if task_due_date == "":
                                print("The due date of task is blank.\n") 
                        # If the variable "task_due_date" is not empty, proceed to check the validity of variable "task_due_date"    
                        else:
                            # if the variable "task_due_date" is not a digit or the length of the variable "task_due_date" is not equal to 8,
                            # Set the variable "task_due_date" to empty string
                            # Print the message to notify the user
                            if not task_due_date.isdigit() or len(task_due_date) != 8:
                                task_due_date = ""
                                print("The due date of task contains non-numeric characters or the number of characters is not equal to 8.\n")
                            # If the variable "task_due_date" is a digit and the length of the variable "task_due_date" is equal to 8,
                            # it checks the validity of the due date of the task input
                            elif task_due_date.isdigit() and len(task_due_date) == 8:
                                # The variable "task_due_date" is entered into the format DDMMYYYY
                                # Split the variable "task_due_date" into 3 parts: day, month and year for validation                                
                                # Set the variable "task_due_date_day" and store the day of the due date of the task
                                # from the index of the variable "task_due_date" from 0 to 1 is the day of the due date of the task
                                task_due_date_day = int(task_due_date[:2])
                                # Set the variable "task_due_date_month" and store the  month of the due date of the task
                                # from the index of the variable "task_due_date" from 2 to 3 is the month of the due date of the task
                                task_due_date_month = int(task_due_date[2:4])
                                # Set the variable "task_due_date_year" and store the year of the due date of the task
                                # from the index of the variable "task_due_date" from 4 to 7 is the year of the due date of the task
                                task_due_date_year = int(task_due_date[4:])                                
                                # If the variable "task_due_date" is not a valid date, 
                                # set the variable "task_due_date" to empty and ask the user to enter the due date of the task again
                                # Print the message to notify the user of the invalid date format of the due date of the task 
                                if not valid_date(task_due_date_year, task_due_date_month, task_due_date_day):
                                    task_due_date = ""
                                    print("The due date of task is invalid format. [DDMMYYYY]. Please enter task due date again.\n")
                                # If the variable "task_due_date" is a valid date, execute the following statements
                                else:
                                    # Set the variable "task_due_date_string" and 
                                    # store the variable "task_due_date" for a converted due task of task 
                                    task_due_date_string = datetime(task_due_date_year, task_due_date_month, task_due_date_day)
                                    # Set the variable "task_due_date_formatted" and 
                                    # store the formatted date string of the variable "task_due_date_string"
                                    task_due_date_formatted = f"{task_due_date_string.strftime('%d %b %Y')}"
                                    # Create a current date object and store it in the variable "today"
                                    today = datetime.now()
                                    # Set the variable "task_assigned_date" to store an assigned date of the task
                                    task_assigned_date = f"{today.strftime('%d %b %Y')}"
                                    # Append the text file "tasks.txt" as the "file" object, 
                                    # store the assigned username, title, description, assigned date and due date and completion of the task 
                                    with open(f"{current_directory}/{task_file}", "a") as file:
                                        # Write a new line in the text file "tasks.txt" including:
                                        # assigned username, title, description, assigned date, due date and completion of the task 
                                        # with the separator (i.e. comma)                                         
                                        file.write(f"\n{username_assigned}, {task_title}, {task_description}, {task_assigned_date}, {task_due_date_formatted}, No")
                                    # Print a new line
                                    print("\n")
                                    # Create a list "task_body" to store the detail of the new task for display
                                    task_body = [task_title, username_assigned, task_assigned_date, task_due_date_formatted, "No", task_description]
                                    # Print the detail of the new task to the user
                                    print(f"A new task is added.\n")
                                    # Print a new line with a separator "-"
                                    print(f"{'-' * display_width}\n")                                    
                                    # Use for-loop to print the detail of the new task if the index of the list "task_header" is ranged from 0 to the length of task_header - 1
                                    for i in range(len(task_header)):
                                        # Note: both the lengths of the list "task_header" and the list "task_body" are same
                                        # If the index of the list "task_header" is not equal to the length of the list "task_body" - 1, 
                                        # print the element of the list "task_header" an element of the list "task_body", 
                                        # print the required space between the elements of the list "task_header" and an element of the list "task_body"
                                        if i != len(task_body)-1: 
                                            print(f"{task_header[i]}{' ' * (task_header_length-len(task_header[i]))} {task_body[i]}")
                                        # If the index of the list "task_header" is equal to the length of the list "task_body" - 1, 
                                        # print the last element of the list "task_header" and an element of the list "task_body" with a new line
                                        else:
                                            print(f"{task_header[-1]}\n {task_body[-1]}\n")
                                            # Print a new line with a separator "-"
                                            print(f" {'-' * display_width}\n")
                                    # Set the variable "task_added" to true to exit the while-loop after adding a new task     
                                    task_added = True
#
# END: Adding a task 
#                              
########################################################################################################################

    elif menu == 'va':
        # pass
        '''In this block, you will put code so that the program will read the task from the task.txt file and
         print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
         You can do it in this way:
            - Read a line from the file.
            - Split that line where there is a comma and space.
            - Then print the results in the format shown in Output 2 
            - It is much easier to read a file using a for a loop.'''

########################################################################################################################
#
# Compulsory Task Part 1
# START: View all tasks
#
        # Set the list "all_tasks" to empty
        all_tasks = []
        # Read the text file "tasks.txt" as the "file" object
        with open(f"{current_directory}/{task_file}", "r") as file:
            # Use for-loop to add all the elements "task_line" in the "file" object to the list "all_tasks"
            all_tasks = [task_line for task_line in file]
        # If the list "all_tasks" is not empty, print the message to notify the user
        if all_tasks:
            print(f"\nView all tasks - {username_input} [No. of tasks: {len(all_tasks)}]\n ")            
            # Use for-loop to extract the element of the variable "task" in the list "all_task"
            for task in all_tasks:
                # Set the variable "task_split" to store the split element of the variable "task"
                task_split = task.split(",")
                # Set the variable "username_assigned" to the index 0 element of the split variable "task"
                username_assigned = task_split[0].strip()
                # Set the variable "task_title" to the index 1 element of the split variable "task"
                task_title = task_split[1].strip()
                # Set the variable "task_description" to the index 2 element of the split variable "task"
                task_description = task_split[2].strip()
                # Set the variable "task_assigned_date" to the index 3 element of the split variable "task"
                task_assigned_date = task_split[3].strip()
                # Set the variable "task_due_date" to the index 4 element of the split variable "task"
                task_due_date = task_split[4].strip()
                # Set the variable "task_completed" to the index 5 element of the split variable "task"
                task_completed = task_split[5].strip()   
                # Set the list "task_body" store the variables "task_title", "username_assigned", "task_assigned_date", 
                # "task_due_date", "task_completed", "task_description"
                task_body = [task_title, username_assigned, task_assigned_date, task_due_date, task_completed, task_description]                
                # If the list "task_body" is not empty, print the details of all the tasks  
                if task_body:
                    # Print a new line with a separator "-"
                    print(f"{'-' * display_width}\n")
                    # Use for-loop to print the detail of each task
                    # if the index "i" of the list "task_header" is ranged from 0 to the length of the list "task_header" - 1
                    for i in range(len(task_header)-1):
                        # Print the index i of the elements of the list "task_header" and the list "task_body" as well as 
                        # the required space between the elements of the list "task_header" and the element of the list "task_body"
                        print(f"{task_header[i]}{' ' * (task_header_length-len(task_header[i]))} {task_body[i]}")
                    # Print the last elements of the list "task_header" and the list "task_body"
                    print(f"{task_header[-1]}\n {task_body[-1]}\n")  
            # Print a new line with a separator "-"
            print(f"{'-' * display_width}\n")
        # If the list "all_tasks" is empty, print the message to notify the user with a new line
        else:
            print("\n")
            print("No task is found!\n")
#
# END: View all tasks
#
########################################################################################################################

    elif menu == 'vm':
        # pass
        '''In this block, you will put code the that will read the task from task.txt file and
         print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
         You can do it in this way:
            - Read a line from the file
            - Split the line where there is a comma and space.
            - Check if the username of the person logged in is the same as the username you have
            read from the file.
            - If they are the same print it in the format of Output 2 in the task PDF'''

########################################################################################################################
#
# Compulsory Task Part 1
# START: View my task
#
        # Set the empty list "user_tasks"
        user_tasks = []
        # Read the text file "tasks.txt" as the "file" object
        with open(f"{current_directory}/{task_file}", "r") as file:
            # Use for-loop to add all the elements "task_line" in the "file" object to the list "user_tasks"
            # if the index 0 element of the variable "task_line" is matched with the variable "username_input"
            user_tasks = [task_line for task_line in file if task_line.split(",")[0].strip().find(username_input) != -1]
        # If the list "user_tasks" is not empty, print the message to notify the user
        if user_tasks:
            print(f"\nView my tasks - {username_input} [No. of tasks: {len(user_tasks)}]\n ")
            # Use for-loop to extract the element of the variable "task" in the list "user_tasks"
            for task in user_tasks:
                # Set the variable "task_split" to store the split element of the variable "task"
                task_split = task.split(",")
                # Set the variable "username_assigned" to the index 0 element of the split variable "task"
                username_assigned = task_split[0].strip()
                # Set the variable "task_title" to the index 1 element of the split variable "task"
                task_title = task_split[1].strip()
                # Set the variable "task_description" to the index 2 element of the split variable "task"
                task_description = task_split[2].strip()
                # Set the variable "task_assigned_date" to the index 3 element of the split variable "task"
                task_assigned_date = task_split[3].strip()
                # Set the variable "task_due_date" to the index 4 element of the split variable "task"
                task_due_date = task_split[4].strip()
                # Set the variable "task_completed" to the index 5 element of the split variable "task"
                task_completed = task_split[5].strip()   
                # Set the list "task_body" store the variables "task_title", "username_assigned", "task_assigned_date",
                # "task_due_date", "task_completed", "task_description"
                task_body = [task_title, username_assigned, task_assigned_date, task_due_date, task_completed, task_description]
                # If the list "task_body" is not empty, print the details of my tasks  
                if task_body:
                    # Print a new line with a separator "-"
                    print(f"{'-' * display_width}\n")
                    # Use for-loop to print the detail of each task 
                    # if the index "i" of the list "task_header" is ranged from 0 to the length of the list "task_header" - 1
                    for i in range(len(task_header)-1):
                        # Print the index i of the elements of the list "task_header" and the list "task_body" as well as 
                        # the required space between the element of the list "task_header" and the element of the list "task_body"
                        print(f"{task_header[i]}{' ' * (task_header_length-len(task_header[i]))} {task_body[i]}")
                    # Print the last elements of the list "task_header" and the list "task_body"
                    print(f"{task_header[-1]}\n {task_body[-1]}\n")    
            # Print a new line with a separator "-"
            print(f"{'-' * display_width}\n")
        # If the list "all_tasks" is empty, print the message to notify the user with a new line
        else:
            print("\n")
            print("No task is found!\n")
#
# END: View my task
#
########################################################################################################################

    elif menu == 'e':
        # Add a new line
        print(f'\nGoodbye!!!\n')
        exit()

# **********************************************************************************************************************
#
# Compulsory Task Part 2
# View statistics [new menu option]
#   
    # If the variable "menu" is "vs" and the variable "admin_login" is true, 
    # it displays the option of viewing statistics
    elif menu == "vs" and admin_login:
        # Set the empty list "user_list"
        user_list = []
        # Set the empty list "task_list"
        task_list = []
        # Read the text file "user.txt" as the "file" object
        with open(f"{current_directory}/{user_file}", "r") as file:
            # Use for-loop to add all the elements "user" in the "file" object to the list "user_list"
            user_list = [user for user in file]
        
        # Read the text file "tasks.txt" as the "file" object
        with open(f"{current_directory}/{task_file}", "r") as file:
            # Use for-loop to add all the elements "task" in the "file" object to the list "task_list"
            task_list = [task for task in file]
        # Print a new line
        print("\n")
        # Print the message "View statistics" to notify the user
        print(f"View statistics - {username_input}\n")
        # Print a new line with a separator "-"
        print(f"{'-' * display_width}\n")
        # Print the total number of users with the length of the list "user_list"
        print(f"Total number of users: {len(user_list)}")   
        # Print the total number of users with the length of the list "task_list"
        print(f"Total number of tasks: {len(task_list)}") 
        # Print a new line
        print("\n")
        # Print a new line with a separator "-"
        print(f"{'-' * display_width}\n")
#
# **********************************************************************************************************************
#
    else:
        # Add a new line
        print("\n")
        # Add a new line
        print("You have made a wrong choice, Please Try again.\n")
