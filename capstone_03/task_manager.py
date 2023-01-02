# =====importing libraries===========
'''This is the section where you will import libraries'''
#
# Task 26 - Capstone Project III - Lists, Functions, and String Handling
# Compulsory Task Part 1
# Project Name: Task Manager (Modified)
# task_manager.py
# Author: Eddy Chan, Chi-wai
# Date: 17 December 2022
########################################################################################################################
#
# START: Import library
#
import os
from datetime import datetime
#
# END: import library
#
########################################################################################################################
#
# START: Set the environment variables
#
# Set the variable "current_directory" to store the current directory path
# Replace the backslash of the variable "current_directory" with a dash
current_directory = os.getcwd().replace("\\", "/")
# Set a variable "file_name" and store the text file name "user.txt"
user_file = "user.txt"
# Set a variable "task_file" and store the text file name "tasks.txt"
task_file = "tasks.txt"
# Set a variable "task_overview_file" and store the text file name "task_overview.txt"
task_overview_file = "task_overview.txt"
# Set a variable "user_overview_file" and store the text file name "user_overview.txt"
user_overview_file = "user_overview.txt"
# Set a variable "display_width" of the display width to 120
display_width = 120
# Set a variable "dotted_line_separator" to a dotted line separator for display purpose
dotted_line_separator = f"{'-' * display_width}"
# Set a variable "double_dash_separator" to a dotted line separator for display purpose
double_dash_separator = f"{'=' * display_width}"
# Set a variable "number_of_column" to 5 for report printing
number_of_column = 5 
# Set a variable "header_column_width" to the variable "display_width" / the variable "number_of_column" report printing
header_column_width = int(display_width / number_of_column)
# Set a variable "separator_double_dash_line" to the double dash line separator
separator_double_dash_line = f"{'=' * display_width}"
# Set a variable "separator_dotted_line" to the dotted line separator
separator_dotted_line = f"{'-' * display_width}"
# Set a list "task_header" and store the task header
task_header = ["Task:", "Assigned to:", "Date Assigned:", "Due Date:", "Task Complete?", "Task Description:"]
# Set a variable "max_task_header_length" to the maximum length of the element in the list "task_header"
max_task_header_length = len(max(task_header, key=len))
# Set a variable "task_header_length" to 25 as the spaces are occupied by the task header 
task_header_length = 25 
# Set a variable "username_input" to empty
username_input = ""
# 
# *********************************************************************************************************************
#
# Set a variable "admin_login" to false
admin_login = False
#
# **********************************************************************************************************************
#
# END: set the environment variables
#
########################################################################################################################
#
# START: Create self-defined functions
#
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
# END: valid_date
#
########################################################################################################################
#
# START: Create self-defined function - "print_banner"
#
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
    # Set a variable "menu_note" to store the menu header
    menu_note = "(Advanced Version)"
    # Set a variable "menu_header_with_space" to store the menu header with space
    menu_note_with_space = " ".join([character.upper() for character in menu_note])
    # Set a variable "menu_header" to store the menu header
    menu_header = "== Help you manage the tasks =="
    # Set a variable "menu_header_with_space" to store the menu header with space
    menu_header_with_space = " ".join([character.upper() for character in menu_header])
    # Print the variable "menu_note_with_space" with the required spaces
    print(f"\n{' ' * ((display_width - len(menu_note_with_space))//2) }{menu_note_with_space}") 
    # Print the variable "menu_header_with_space" with the required spaces
    print(f"\n{' ' * ((display_width - len(menu_header_with_space))//2) }{menu_header_with_space}")    
    # Print a double dash separator with the variable "double_dash_separator"
    print(f"\n{double_dash_separator}\n")
#
# END: self-defined function - "print_banner"
#
#######################################################################################################################
#
# START: Create self-defined function - "check_task_overdue"
#
# Create a function "check_task_overdue" with a parameter "task_due_date" to check the task that is overdue
#
def check_task_overdue(task_due_date):
    # Set a variable "task_is_overdue" to false that the task is not yet overdue
    task_is_overdue = False
    # If the parameter "task_due_date" is not empty, compare the due date of the task and today's date    
    if task_due_date:
        # Set a variable "task_overdue" to convert the data type of the variable "task_due_date" to the Date object
        task_overdue = datetime.strptime(task_due_date, '%d %b %Y')
        # Set a variable "today_date" to store the today's date of the Date object 
        today_date = datetime.now()
        # If the variable "task_overdue" is less than the variable "today_date", set the variable "task_is_overdue" to true
        # Note: The task is regarded as "overdue"
        if task_overdue < today_date:
            task_is_overdue = True
    # Return the variable "task_is_overdue"
    return task_is_overdue  
#
# END: self-defined function - "check_task_overdue"
#
########################################################################################################################
#
# START: Create self-defined function - "generate_file"
#
# Create a function "generate_file" with the parameters "file_name" and "file_line_list" to generate the text file
#
def generate_file(file_name, file_line_list):
    # If the parameters "file_line_list" and "file_name" are not empty, try and except block to open the text file for writing 
    if file_line_list and file_name:
        try:
            # Write the text file variable "file_name" as the "file" object, store each line in the list parameter "file_line_list"
            with open(f"{current_directory}/{file_name}", "w+") as file:
                file.write("\n".join([line for line in file_line_list]))
                # Return true as it is a success
                return True
        except:
            # Print the message to notify the user as it fails to generate the text file variable "file_name"
            print(f"Fail to generate the text file {file_name}. Please check the current path and the location of the text file {file_name}.\n")
            # Return true as it is a failure
            return False
    # If the parameters "file_line_list" or/and "file_name" are empty, 
    # print the message to notify the user as it fails to load the line of the task record.
    else:
        print(f"Fail to load the line of task record(s).\n")
#
# END: self-defined function - "generate_file"
#
########################################################################################################################
#
# START: Create self-defined function - "get_task_overview_list"
#
# Create a function "get_task_overview_list" to get the list of the task overview
#
def get_task_overview_list():
    # Initialise the set of variables of the task overview
    # Set a variable "total_number_of_tasks" to 0
    total_number_of_tasks = 0
    # Set a variable "total_number_of_completed_task" to 0
    total_number_of_completed_task = 0
    # Set a variable "total_number_of_uncompleted_task" to 0
    total_number_of_uncompleted_task = 0
    # Set a variable "total_number_of_overdue_task" to 0
    total_number_of_overdue_task = 0
    # Set a variable "total_number_of_uncompleted_and_overdue_task" to 0
    total_number_of_uncompleted_and_overdue_task = 0
    # Set a variable "percentage_of_incompleted_task" to 0
    percentage_of_incompleted_task = 0
    # Set a variable "percentage_of_overdue_task" to 0
    percentage_of_overdue_task = 0
    # Set a variable "task_overview_list" to a empty list
    task_overview_list = []
    # Set a list "all_task_list" to empty 
    all_task_list = []

    # try and except block to read the text file "tasks.txt" as the "file" object
    try:
        with open(f"{current_directory}/{task_file}", "r") as file:
            # Use the list "all_task_list" to store all elements "task_line" of the "file" object
            all_task_list = [task_line for task_line in file]
        
        # Set a 2d list "task_2d_list" to empty for storing the counting of tasks
        task_2d_list = []
        # If the list "all_task_list" is not empty, count the task overview for all the elements "task_line" of the list "all_task_list"
        if all_task_list:
            for task_line in all_task_list:
                # If the variable "task_line" is not empty, append the list "task_2d_list" by all elements "task_line"
                if task_line:
                    # Append the list "task_2d_list" by all elements "task_line"
                    task_2d_list.append(task_line.strip().split(","))
            
            # Use the variable "total_number_of_tasks" to store the length of the list "task_2d_list"
            total_number_of_tasks = len(task_2d_list)
            # Set a variable "total_number_of_tasks_line" to store the total number of tasks has been generated and tracked using the task_manager.py
            total_number_of_tasks_line = f"The total number of tasks has been generated and tracked using the task_manager.py: {total_number_of_tasks}"

            # Use for-loop to count the tasks for all the elements "task_line" of the list "task_2d_list"
            for task_line in task_2d_list:
                # If the index 5 of the element "task_line", i.e Task Complete, is equal to "Yes", 
                # the variable "total_number_of_completed_task" is added by 1
                if task_line[5].strip().lower() == "Yes".lower():
                    total_number_of_completed_task += 1
                # If the index 5 of the element "task_line", i.e Task Complete, is not equal to "Yes", 
                # the variable "total_number_of_uncompleted_task" is added by 1
                else:
                    total_number_of_uncompleted_task += 1
                # Call a function "check_task_overdue" to check the index 4 of the element "task_line", i.e. Due Date to be overdue
                # If the index 4 of the element "task_line" is overdue, the variable "total_number_of_overdue_task" is added by 1
                if check_task_overdue(task_line[4].strip()):
                    total_number_of_overdue_task += 1
                # If index 5 of the element "task_line" is not equal to "Yes" and index 4 of the element "task_line" is overdue,
                # the variable "total_number_of_uncompleted_and_overdue_task" is added by 1
                if task_line[5].strip().lower() == "No".lower() and check_task_overdue(task_line[4].strip()):
                    total_number_of_uncompleted_and_overdue_task += 1

            # Set a variable "percentage_of_incompleted_task" to store the percentage of the incompleted task
            # Use the variable "total_number_of_uncompleted_task" divided by the variable "total_number_of_tasks"
            percentage_of_incompleted_task = round(total_number_of_uncompleted_task / total_number_of_tasks * 100)
            # Set a variable "percentage_of_incompleted_task_line" to store the percentage of incompleted_task
            percentage_of_incompleted_task_line = f"The percentage of incompleted_task: {percentage_of_incompleted_task}%"
            # Set a variable "percentage_of_overdue_task" to store the percentage of the overdue task
            # Use the variable "total_number_of_overdue_task" divided by the variable "total_number_of_tasks"
            percentage_of_overdue_task = round(total_number_of_overdue_task / total_number_of_tasks * 100)
            # Set a variable "percentage_of_overdue_task_line" to store the percentage of overdue_task
            percentage_of_overdue_task_line = f"The percentage of overdue_task: {percentage_of_overdue_task}%\n"

            # Set a variable "task_overview_header" to store the header "Task Overview" with the required spaces
            task_overview_header = f"{ ' '.join([character.upper()  for character in 'Task Overview'])}"
            task_overview_header = f"{' ' * ((display_width - len(task_overview_header)) // 2) }{task_overview_header}{' ' * ((display_width - len(task_overview_header)) // 2) }"
            # Append the variable "separator_double_dash_line" to the list "task_overview_list"
            task_overview_list.append(separator_double_dash_line) 
            # Append the variable "task_overview_header" to the list "task_overview_list"
            task_overview_list.append(task_overview_header)
            # Append the variable "separator_double_dash_line" to the list "task_overview_list"
            task_overview_list.append(separator_double_dash_line + "\n") 
            # Append the variable "total_number_of_tasks_line" to the list "task_overview_list" 
            task_overview_list.append(total_number_of_tasks_line)
            # Set a variable "total_number_of_completed_task_line" to store the total number of completed tasks               
            total_number_of_completed_task_line = f"Total number of completed tasks: {total_number_of_completed_task}"
            # Append the variable "total_number_of_completed_task_line" to the list "task_overview_list" 
            task_overview_list.append(total_number_of_completed_task_line) 
            # Set a variable "total_number_of_uncompleted_task_line" to store the total number of uncompleted tasks
            total_number_of_uncompleted_task_line = f"Total number of uncompleted tasks: {total_number_of_uncompleted_task}"
            # Append the variable "total_number_of_uncompleted_task_line" to the list "task_overview_list" 
            task_overview_list.append(total_number_of_uncompleted_task_line) 
            # Set a variable "total_number_of_overdue_task_line" to store the total number of overdue tasks
            total_number_of_overdue_task_line = f"Total number of overdue tasks: {total_number_of_overdue_task}"
            # Append the variable "total_number_of_overdue_task_line" to the list "task_overview_list" 
            task_overview_list.append(total_number_of_overdue_task_line) 
            # Set a variable "total_number_of_uncompleted_and_overdue_task_line" to store 
            # the total number of tasks that haven't been completed and that are overdue
            total_number_of_uncompleted_and_overdue_task_line = f"Total number of tasks that haven't been completed and that are overdue: {total_number_of_uncompleted_and_overdue_task}"
            # Append the variable "total_number_of_uncompleted_and_overdue_task_line" to the list "task_overview_list" 
            task_overview_list.append(total_number_of_uncompleted_and_overdue_task_line) 
            # Set a variable "percentage_of_incompleted_task_line" to store the percentage of incomplete tasks
            percentage_of_incompleted_task_line = f"The percentage of tasks that are incompleted: {percentage_of_incompleted_task}%"
            # Append the variable "percentage_of_incompleted_task_line" to the list "task_overview_list" 
            task_overview_list.append(percentage_of_incompleted_task_line) 
            # Set a variable "percentage_of_overdue_task_line" to store the percentage of tasks that are overdue
            percentage_of_overdue_task_line = f"The percentage of tasks that are overdue: {percentage_of_overdue_task}%\n"
            # Append the variable "percentage_of_overdue_task_line" to the list "task_overview_list" 
            task_overview_list.append(percentage_of_overdue_task_line) 
    # If it fails to read the text file "tasks.txt", print the message to notify the user 
    # for checking the current directory and the location of the text file tasks.txt
    except:
        print(f"Fail to load the text file {task_file}. Please check the current path and the location of the text file {task_file}.\n")
    # Return the list "task_overview_list"       
    return task_overview_list
#
# END: self-defined function - "get_task_overview_list"
#
########################################################################################################################
#
# START: self-defined function - "get_user_overview_list"
#
# Create a function "get_user_overview_list" to get the list of the user overview
#
def get_user_overview_list():
    # Set a list "username_list" to the usernames by calling the function "get_username_list"
    username_list = get_username_list()
    # Set a list "username_sorted_list" to copy the list "username_list"
    username_sorted_list = username_list.copy()
    # Sort the list "username_sorted_list"
    username_sorted_list.sort()
    # Append the element "total" to the list "username_sorted_list" 
    username_sorted_list.append("total")

    # Set a list "user_overview_list" to empty 
    user_overview_list = []
    # Set a list "all_task_list" to empty
    all_task_list = []
    # index
    # 0. username
    # 1. The total number of tasks assigned to that user
    # 2. the tasks assigned to that user that have been completed
    # 3. the tasks assigned to that user that must still be completed (uncompleted but not yet overdue)
    # 4. the tasks assigned to that user that has not yet been completed and are overdue
    username_task_count = [[username.strip(), 0, 0, 0, 0] for username in username_sorted_list]
    # Set a variable "number_of_users_registered" to 0
    number_of_users_registered = 0
    # Set a variable "number_of_tasks_generated" to 0
    number_of_tasks_generated = 0
    
    # Use try and except block to read the text file "tasks.txt" as the "file" object
    try:
        with open(f"{current_directory}/{task_file}", "r") as file:
            # Set the list "all_task_list" to store all the elements "task_line" of the "file" object
            all_task_list = [task_line for task_line in file]
        # If the list "all_task_list" and the list "username_sorted_list" are not empty, 
        # count the user overview for all the elements "task_line" of the list "all_task_list"
    
        if all_task_list and username_sorted_list:
            # Use for-loop to count the user ask overview for all the elements of "username" of the list "username_sorted_list"
            # and check against the list "all_task_list"
            for index, username in enumerate(username_sorted_list):           
                for task_line in all_task_list:
                    # Set a list "task_split" to store the split "task_line"
                    task_split = task_line.split(",")
                    # If the index 0 of the element "task_split" is equal to the element "username" of the list "username_sorted_list",
                    # count the users' tasks - total, completed, uncompleted, ongoing and overdue
                    if task_split[0].strip().lower() == username.lower():
                        # Set the index[1] element of the list "username_task_count" to store the number of tasks assigned to the user
                        # and it is added by 1 
                        username_task_count[index][1] += 1
                        # Set the last element[1] of the list "username_task_count" [total] 
                        # to store the total number of tasks assigned to the user
                        # and it is added by 1 
                        username_task_count[-1][1] += 1
                        # If the index 5 of the element "task split" is equal to "Yes", count the number of tasks completed by the user
                        if task_split[5].strip().lower() == "Yes".lower():
                            # Set the index[2] element of the list "username_task_count" to store the number of tasks completed by the user
                            # and it is added by 1   
                            username_task_count[index][2] += 1
                            # Set the last element[2] of the list "username_task_count" [total] 
                            # to store the total number of tasks completed by the user
                            # and it is added by 1 
                            username_task_count[-1][2] += 1
                        # If index 4 of the element "task_split" is not overdue (call the function "check_task_overdue") and 
                        # the index 5 of the element "task split" is equal to "No", 
                        # count the number of tasks uncompleted by the user
                        if not check_task_overdue(task_split[4].strip()) and task_split[5].strip().lower() == "No".lower():
                            username_task_count[index][3] += 1
                            # Set the last element[3] of the list "username_task_count" [total] 
                            # to store the total number of task uncompleted
                            # and it is added by 1 
                            username_task_count[-1][3] += 1
                        # If index 4 of the element "task_split" is overdue (call the function "check_task_overdue") and 
                        # the index 5 of the element "task split" is equal to "No", 
                        # count the number of tasks uncompleted and overdue
                        if check_task_overdue(task_split[4].strip()) and task_split[5].strip().lower() == "No".lower():
                            # Set the last element[4] of the list "username_task_count" [total] 
                            # to store the total number of task uncompleted and overdue
                            # and it is added by 1 
                            username_task_count[index][4] += 1
                            username_task_count[-1][4] += 1
            # Set the variable "number_of_users_registered" to store the length of the list "username_list"
            number_of_users_registered = len(username_list)
            # Set the variable "number_of_tasks_generated" to store the length of the list "all_task_list"
            number_of_tasks_generated = len(all_task_list)
            # Set a variable "user_view_header" to store the header "User Overview" with the required spaces
            user_view_header = f"{ ' '.join([character.upper()  for character in 'User Overiew'])}"
            user_view_header = f"{' ' * ((display_width - len(user_view_header)) // 2) }{user_view_header}{' ' * ((display_width - len(user_view_header)) // 2) }"
            
            # Append the variable "user_overview_list" to the list "user_overview_list"
            user_overview_list.append(separator_double_dash_line)    
            # Append the variable "user_view_header" to the list "user_overview_list"
            user_overview_list.append(user_view_header)
            # Append the variable "separator_double_dash_line" to the list "user_overview_list"
            user_overview_list.append(separator_double_dash_line + "\n")
            # Set a variable "number_of_users_registered_line" to store the total number of users registered with task_manager.py
            number_of_users_registered_line = f"The total number of users registered with task_manager.py: {number_of_users_registered}"
            # Append the variable "number_of_users_registered_line" to the list "user_overview_list"
            user_overview_list.append(number_of_users_registered_line)
            # Set a variable "number_of_tasks_generated_line" to store the total number of tasks that have been generated and tracked using task_manager.py:
            number_of_tasks_generated_line = f"The total number of tasks that have been generated and tracked using task_manager.py: {number_of_tasks_generated}\n"
            # Append the variable "number_of_tasks_generated_line" to the list "user_overview_list"
            user_overview_list.append(number_of_tasks_generated_line)
            
            # Set a variable "user_report_header" to store 
            # the header of the user overview by calling the function "wrap_user_report_header"
            user_report_header = wrap_user_report_header()
            # Append the variable "user_report_header" to the list "user_overview_list"
            user_overview_list.append(user_report_header)        
            # Append the variable "separator_dotted_line" to the list "user_overview_list"
            user_overview_list.append(separator_dotted_line)
            
            # Use for-loop to count the user task overview: assigned, completed, ongoing, uncompleted and overdue
            # for all the elements "username_task" in the list "username_task_count"
            for index, username_task in enumerate(username_task_count):
                # If the index of the list "username_task_count" is equal to the length of the list "username_task_count" -1,
                # # Append the variable "separator_dotted_line" to the list "user_overview_list"
                if index == len(username_task_count) -1:
                    user_overview_list.append(separator_dotted_line)
                # Set the variable "username_assigned_task_count" to store the index[1] of the list "username_task_count"
                username_assigned_task_count = username_task_count[index][1]
                # Set the variable "username_completed_task_count" to store the index[2] of the list "username_task_count"
                username_completed_task_count = username_task_count[index][2]
                # Set the variable "username_completed_task_count" to store the index[3] of the list "username_task_count"
                username_ongoing_task_count = username_task_count[index][3]
                # Set the variable "username_uncompleted_overdue_task_count" to store the index[4] of the list "username_task_count"
                username_uncompleted_overdue_task_count = username_task_count[index][4]
                # Set the variable "username_assigned_width" to store the index[0] of the list "username_task_count"
                username_assigned = f"{username_task_count[index][0]}"
                # Set the variable "username_assigned_width" to the column width of the username column
                username_assigned_width = header_column_width - len(username_assigned)
                
                # Set the variable "username_assigned_percentage" to store the percentage of the tasks assigned to the user
                # Use the variable "username_assigned_task_count" divided by the variable "number_of_tasks_generated"
                username_assigned_percentage = round(username_assigned_task_count / number_of_tasks_generated * 100)
                # Set the variable "username_assigned_percentage_width" to store the space filled for the percentage column used
                username_assigned_percentage_width = 3 - len(str(username_assigned_percentage))
                
                # Set the variable "username_assigned_task_figure" to store the figure of the tasks assigned to the users
                username_assigned_task_figure = f"{username_assigned_task_count} ({' ' * username_assigned_percentage_width}{username_assigned_percentage}%)"
                # Set the variable "username_assigned_task_width" to store the space filled for the figure column used
                username_assigned_task_width = header_column_width - len(username_assigned_task_figure) 

                # Set the variable "username_completed_percentage" to store the percentage of the task completed by the user
                # Use the variable "username_completed_percentage" divided by the variable "number_of_tasks_generated"
                username_completed_percentage = round(username_completed_task_count / number_of_tasks_generated * 100)
                # Set the variable "username_completed_percentage_width" to store the space filled for the percentage column used
                username_completed_percentage_width = 3 - len(str(username_completed_percentage))
                # Set the variable "username_completed_task_figure" to store the figure of the completed tasks assigned to the users
                username_completed_task_figure = f"{username_completed_task_count} ({' ' * username_completed_percentage_width}{username_completed_percentage}%)"
                # Set the variable "username_completed_task_width" to store the figure of the completed tasks assigned to the users
                username_completed_task_width = header_column_width -  len(username_completed_task_figure)

                # Set the variable "username_ongoing_task_percentage" to store the percentage of the ongoing tasks assigned by the user
                # the variable "username_ongoing_task_percentage" divided by the variable "number_of_tasks_generated"
                username_ongoing_task_percentage = round(username_ongoing_task_count / number_of_tasks_generated * 100)
                # Set the variable "username_ongoing_task_percentage_width" to store the space filled for the percentage column used
                username_ongoing_task_percentage_width = 3 - len(str(username_ongoing_task_percentage))            
                # Set the variable "username_ongoing_task_figure" to store the figure of the ongoing tasks assigned to the users
                username_ongoing_task_figure = f"{username_ongoing_task_count} ({' ' * username_ongoing_task_percentage_width}{username_ongoing_task_percentage}%)"
                # Set the variable "username_ongoing_task_width" to store the figure of the ongoing tasks assigned to the users
                username_ongoing_task_width = header_column_width - len(username_ongoing_task_figure) 

                # Use the variable "username_uncompleted_overdue_task_percentage" divided by the variable "number_of_tasks_generated"
                username_uncompleted_overdue_task_percentage = round(username_uncompleted_overdue_task_count / number_of_tasks_generated * 100)
                # Set the variable "username_uncompleted_overdue_task_percentage_width" to store the space filled for the percentage column used
                username_uncompleted_overdue_task_percentage_width = 3 - len(str(username_uncompleted_overdue_task_percentage))   
                # Set the variable "username_uncompleted_overdue_task_figure" to store the figure of the uncompleted and overdue tasks assigned to the users
                username_uncompleted_overdue_task_figure = f"{username_uncompleted_overdue_task_count} ({' ' * username_uncompleted_overdue_task_percentage_width}{username_uncompleted_overdue_task_percentage}%)"
                # Set the variable "username_uncompleted_overdue_task_width" to store the figure of the uncompleted and overdue tasks assigned to the users
                username_uncompleted_overdue_task_width = header_column_width - len(username_uncompleted_overdue_task_figure)  
                # Set the variable "username_task_line" to store the figures of each user's line with the above variables 
                username_task_line = f"{username_assigned}{' ' * (username_assigned_width) }{' ' * username_assigned_task_width}{username_assigned_task_figure}{' ' * (username_completed_task_width)}{username_completed_task_figure}{' ' * ( username_ongoing_task_width)}{username_ongoing_task_figure}{' ' * ( username_uncompleted_overdue_task_width) }{username_uncompleted_overdue_task_figure}"
                # Append the variable "username_task_line" to the list "user_overview_list"
                user_overview_list.append(username_task_line)
    # If it fails to load the text file tasks.txt, print the message to notify 
    # the user to check the current path and the location of the text file tasks.txt 
    except:
        print(f"Fail to load the text file {task_file}. Please check the current path and the location of the text file {task_file}.\n")
    # Return the list "user_overview_list"
    return user_overview_list
#
# END: self-defined function - "get_user_overview_list"
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
#
# START: Create self-defined function - "wrap_user_report_header"
#
# Create a function "wrap_user_report_header" to wrap the report headers of each column
#
def wrap_user_report_header():
    # Set a list "user_report_header" to store the report headers of each column 
    user_report_header = ["No. of tasks assigned (%)", "No. of tasks completed (%)", "No. of ongoing tasks (%)", "No. of uncompleted overdue task (%)"]
    # Create a list "new_user_report_header_line_first_list" to store the first line of the report headers of each column
    new_user_report_header_line_first_list = []
    # Create a list "new_user_report_header_line_second_list" to store the second line of the report headers of each column
    new_user_report_header_line_second_list = []
    
    # Use for-loop to store the first and second lines of the report headers of each column 
    # for all the elements "user_report_header_line" of the list "user_report_header"
    for user_report_header_line in user_report_header:
        # Set a list "user_report_header_split" to store the split elements of the variable "user_report_header_line"
        user_report_header_split = user_report_header_line.split(" ")
        # If the length of the list "user_report_header_split" is less than 6, 
        # it appends the lists "new_user_report_header_line_first_list" and "new_user_report_header_line_second_list"
        # Note: It caters for the element of "No. of uncompleted overdue task (%)" (i.e. the last column) in the list "user_report_header" 
        if len(user_report_header_split) < 6:
            new_user_report_header_line_first_list.append(f"{user_report_header_split[0]} {user_report_header_split[1]} {user_report_header_split[2]}")
            new_user_report_header_line_second_list.append(f"{user_report_header_split[3]} {user_report_header_split[4]}")
        # If the length of the list "user_report_header_split" is not less than 6, 
        # it appends the lists "new_user_report_header_line_first_list" and "new_user_report_header_line_second_list"
        else:
            new_user_report_header_line_first_list.append(f"{user_report_header_split[0]} {user_report_header_split[1]} {user_report_header_split[2]}")
            new_user_report_header_line_second_list.append(f"{user_report_header_split[3]} {user_report_header_split[4]} {user_report_header_split[5]}")
 
    # Set a variable "new_user_report_header_first_line" to empty, store the first line of the report header
    new_user_report_header_first_line = ""
    # Set a variable "new_user_report_header_second_line" to empty, store the second line of the report header
    new_user_report_header_second_line = ""
    # Set a variable "new_user_report_header" to empty, store the report header
    new_user_report_header = ""
    # Use for-loop to concatenate the first line of the report header 
    # for all the elements "report_header" in the list "new_user_report_header_line_first_list" 
    for report_header in new_user_report_header_line_first_list: 
        new_user_report_header_first_line += f"{' ' * (header_column_width - len(report_header))}{report_header.strip()}" 
    # Use for-loop to concatenate the second line of the report header 
    # for all the elements "report_header" in the list "new_user_report_header_line_second_list"
    for report_header in new_user_report_header_line_second_list:        
        new_user_report_header_second_line += f"{' ' * (header_column_width - len(report_header))}{report_header.strip()}" 
    # Set the variable "new_user_report_header" to store the report header lines 
    new_user_report_header = f"{' ' * header_column_width}{new_user_report_header_first_line}\n{' ' * header_column_width}{new_user_report_header_second_line}"
    # Return the variable "new_user_report_header" 
    return new_user_report_header
#
# START: Create self-defined function - "wrap_user_report_header"
#
########################################################################################################################
#
# START: Create self-defined function - "check_username_exist"
#
# Create a function "check_username_exist" with the parameter "username_input" to check the existence of the username
#
def check_username_exist(username_input):
    # Set a variable "username_exist" to false as the username does not exist 
    username_exist = False
    # Set a list "usernames" to empty to store all "usernames"
    usernames = []
    # Use try and except block to read the text file user.txt
    try:
        with open(f"{current_directory}/{user_file}", "r") as file:
            # Use for-loop to store the username (the index 0 of the split element "line") to the list "usernames"
            for line in file:
                line = line.split(",")
                usernames.append(line[0].strip())
        # Set the variable "username_exist" to true if the parameter "username_input" is found in the list "usernames",
        # otherwise set the variable "username_exist" to false
        username_exist = True if username_input in usernames else False
    # If it fails to load the text file user.txt, print the message to notify the user 
    # for checking the current directory and the location of the text file user.txt
    except:
        print(f"Fail to load the text file {user_file}. Please check the current directory and the location of the text file {user_file}.\n")
    # Return the variable "username_exist"
    return username_exist
#
# END: self-defined function - "check_username_exist"
#
########################################################################################################################
#
# START: Create self-defined function - "mark_task_as_complete"
#
# Create a function "mark_task_as_complete" with the parameters "username", "task_number" and "my_task_line" 
# to mark the task as complete
#
def mark_task_as_complete(username, task_number, my_task_line):    
    # If the parameters "my_task_line" and "task_number" are not empty, proceed to mark the task as completed
    if my_task_line and task_number:
        # Set the dictionary "task_dictionary" to store the dictionary of the task 
        # by calling a function "create_task_dictionary" with the parameter "my_task_line"
        task_dictionary = create_task_dictionary(my_task_line)
        # If the key "Assigned to:" of the dictionary, "create_task_dictionary" is equal to the parameter "username" and
        # the key "Task Complete?" of the dictionary "create_task_dictionary" is equal to "No",
        # mark the task as completed
        if task_dictionary["Assigned to:"].lower() == username.lower() and task_dictionary["Task Complete?"].lower() == "No".lower():
            # Set a dictionary "task_complete_dictionary" to copy the dictionary "task_dictionary"
            task_complete_dictionary = task_dictionary.copy()
            # Set the dictionary "task_complete_dictionary" to store the dictionary of the "completed" task 
            # by calling a function "create_task_dictionary" with the parameter "my_task_line"
            task_complete_dictionary = create_task_dictionary(my_task_line)
            # Set the value of the dictionary "task_complete_dictionary" to Yes for the key "Task Complete?" of its dictionary 
            task_complete_dictionary["Task Complete?"] = "Yes" 
            # Set a variable "task_file_line" to convert the dictionary "task_complete_dictionary" into the line of the task
            # by calling a function "convert_dictionary_to_task_file_list" with the parameter "task_complete_dictionary"
            task_file_line = convert_dictionary_to_task_file_list(task_complete_dictionary)
            # Call a function "update_task_file" with the parameters "my_task_line" and "task_file_line" to update the task file
            # If the task file is updated successfully, print the message to notify the user of the update and return true
            if update_task_file(my_task_line, task_file_line):
                print(f"The Task [{task_number}] is marked as completed.\n")              
                return True
            # If the task file is not updated, print the message to notify the user of the update and return false 
            else:
                print(f"Fail to mark the task [{task_number}] completed.\n")
                return False
        # If any other cases, print the message to notify the user that the task has already been marked completed and return false
        else:
            print(f"Task [{task_number}] has already been marked completed.\n")
            return False
#
# END: self-defined function - "mark_task_as_complete"
#
########################################################################################################################
#
# START: Create self-defined function - "refresh_user_task"
#
# Crete a function "refresh_user_task" with the parameters "username" and "task_number" to 
# store the list of "refresh_task_list" 
#
def refresh_user_task(username, task_number):
    # Create a list "refresh_task_list" to empty
    refresh_task_list = []
    # If the parameters "username" and "task_number" are not empty, load the text file "tasks.txt"    
    if username and task_number:
        # Use try and except block to read the task file tasks.txt as the "file" object
        try:   
            with open(f"{current_directory}/{task_file}", "r") as file:
                # Create a list of the "file" object
                all_tasks = file.readlines()
            # Set a variable "count" to 0 and count the index of the list "all_tasks"
            count = 0
            
            # Deduct the parameter "task_number" by 1 (Adjust the index of the parameter "task_number") 
            task_number -= 1
            # Use for-loop to count the index of the element "user_task" in the list "all_tasks" 
            for user_task in all_tasks:
                # If the index 0 of the split element "user_task" is equal to the parameter "username",
                # the variable "count" is added by 1
                if user_task.split(",")[0].strip() == username:
                    count += 1
                # If the variable "count" equal to the task number, 
                # store the split element "user_task" to the list "refresh_task_list"
                # use "break" to exit the for-loop
                if count == task_number + 1:
                    refresh_task_list = user_task.split(",")
                    break
        # If it fails to load the text file user.txt, print the message to notify the user 
        # for checking the current directory and the location of the text file user.txt
        except:
            print(f"Fail to load the text file {user_file}. Please check the current directory and the location of the text file {user_file}.\n")
    # If any other cases, print the message to notify the user of the missing parameters
    else:
        print(f"The parameters \"username\" and \"task_number\" is missing.\n")
    # Return the list "refresh_task"
    return refresh_task_list
#
# END: self-defined function - "check_username_exist"
#
########################################################################################################################
#
# START: Create self-defined function - "create_task_dictionary"
#
# Create a function "create_task_dictionary" with the parameter "task_body" to create the dictionary of the task
#
def create_task_dictionary(task_body):
    # Create a list "task_file_header" to store the default key of the task dictionary
    task_file_header = ["Assigned to:", "Task:", "Task Description:", "Date Assigned:", "Due Date:", "Task Complete?"]  
    # Create an empty dictionary "task_dictionary"
    task_dictionary = dict()
    # Create a list "task_body_split" to store the split variable "task_body" (i.e. the line of the task)
    task_body_split = task_body.split(",")
    # Use for-loop to store the key/value of the dictionary "task_dictionary" 
    # for all the "index" of the element in the list "task_body_split"
    for index, task_line in enumerate(task_file_header):
        task_dictionary[task_line] = task_body_split[index].strip()
    # Return the dictionary "task_dictionary"
    return task_dictionary  
#
# END: self-defined function - "create_task_dictionary"
#
########################################################################################################################
#
# START: Create self-defined function - "check_task_overdue"
#
# Create a function "check_task_overdue" with the parameter "task_due_date" to check whether the task is overdue
#
def check_task_overdue(task_due_date):
    # Set a variable "task_is_overdue" to false for the overdue task
    # The sample of the format of the variable "task_due_date" is 31 Mar 2022
    task_is_overdue = False
    # If the parameter "task_due_date" is not empty, compare the due date of the task with today's date
    if task_due_date:
        # Set a variable "task_overdue" with the parameter "task_due_date"  to create a Date object
        task_overdue = datetime.strptime(task_due_date, '%d %b %Y')
        # Set a variable "today_date" to today's date as the Date object
        today_date = datetime.now()
        # If the variable "task_overdue" is less than the variable "today_date" 
        # to set the variable "task_is_overdue" to true
        if task_overdue < today_date:
            task_is_overdue = True
    # Return the variable "task_is_overdue"
    return task_is_overdue  
#
# END: self-defined function - "check_task_overdue"
#
# ########################################################################################################################
#
# START: Create self-defined function - "convert_dictionary_to_task_file_list"
#
# Create a function "convert_dictionary_to_task_file_list" with the parameter "task_dictionary" 
# to convert the task dictionary to the line of the task file (dictionary to string)
# 
def convert_dictionary_to_task_file_list(task_dictionary):
    # Create a variable "task_file_line" to empty
    task_file_line = ""
    # If the dictionary "task_dictionary" is empty, concatenate the values of the parameter "task_dictionary" to the line 
    if task_dictionary:
        # Set the variable "task_file_line" to store the values of the dictionary "task_dictionary" 
        # in the order of the line of the task file
        # ["Assigned to:", "Task:", "Task Description:", "Date Assigned:", "Due Date", "Task Complete?"] 
        task_file_line = f"{task_dictionary['Assigned to:']}, {task_dictionary['Task:']}, {task_dictionary['Task Description:']}, {task_dictionary['Date Assigned:']}, {task_dictionary['Due Date:']}, {task_dictionary['Task Complete?']}"
    # Return the variable "task_file_line"
    return task_file_line
#
# END: self-defined function - "convert_dictionary_to_task_file_list"
#
########################################################################################################################
#
# START: self-defined function - "print_newly_added_task"
# 
def print_newly_added_task(task_body):
    
    newly_added_tag = "[ADDED]"
    print(f"{(display_width - len(newly_added_tag) - 2) *' ' }{newly_added_tag}")
    # Use for-loop to print the detail of the new task if the index of the list "task_header" is ranged from 0 to the length of task_header - 1
    for i in range(len(task_header)):
        # Note: both the lengths of the list "task_header" and the list "task_body" are same
        # If the index of the list "task_header" is not equal to the length of the list "task_body" - 1, 
        # print the element of the list "task_header" an element of the list "task_body", 
        # print the required space between the elements of the list "task_header" and the element of the list "task_body"
        if i != len(task_body)-1: 
            print(f"{task_header[i]}{' ' * (task_header_length-len(task_header[i]))} {task_body[i]}")
        # If the index of the list "task_header" is equal to the length of the list "task_body" - 1, 
        # print the last element of the list "task_header" and the element of the list "task_body" with a new line
        else:
            print(f"{task_header[-1]}\n {task_body[-1]}\n")
            # Print a dotted line separator
            print(f" {separator_dotted_line}\n")


# END: self-defined function - "print_newly_added_task"
#
########################################################################################################################
#
# START: self-defined function - "print_refresh_task"
#
# Create a function "print_refresh_task" with the parameters "username_input and task_number"
# to print the list "refresh_task_list" in the appropriate format
#
def print_refresh_task(username_input, task_number):
    
    # If the parameters "username_input" and "task_number" are not empty, format the list of the refresh task
    if username_input and task_number: 
        # Set a list "refresh_task_list" with the parameters "username_input and task_number" 
        # to store the list of the refresh task by calling a function "refresh_user_task"
        refresh_task_list = refresh_user_task(username_input, task_number)   
        # Set a list "format_refresh_task_list" to store the formatted task list 
        # after concatenating all elements of the list "refresh_task_list" 
        # by calling a function "task_format_to_display"
        format_refresh_task_list = task_format_to_display((", ").join(refresh_task_list))
        # Print a new line                
        print("\n")
        # Print a separator with the dotted line
        print(separator_dotted_line + "\n")  
        # Printe the variable "task_number" with the required spaces
        print(f"{(display_width - len(str(task_number)) - 2) *' ' }[{task_number}]")
        # Use for-loop to print all the elements of the lists and "task_header" and "format_refresh_task_list"
        for item_index, task_header_item in enumerate(task_header):
            # Set a variable "item_index_space" to store the length of the variable "item_index"
            item_index_space = len(f"[{len(str(item_index))}]")
            # If the variable "item_index" is less than the length of the list "task_header" - 1,
            # print the list the element of the lists and "task_header" and "format_refresh_task_list" 
            if item_index < len(task_header)-1:
                print(f"[{item_index+1}] {task_header_item}{' ' * ( task_header_length - len(task_header_item) + item_index_space  ) } {format_refresh_task_list[item_index].strip()}")
            # If the variable "item_index" is not less than the length of the list "task_header" - 1,
            # print the last element of the lists and "task_header" and "format_refresh_task_list"  
            else:
                print(f"[{item_index+1}] {task_header_item}\n {' ' * item_index_space}{format_refresh_task_list[item_index].strip()}\n") 
    # Print a dotted line separator
    print(separator_dotted_line + "\n")
#
# END: self-defined function - "print_refresh_task"
#
########################################################################################################################
#
# START: Create self-defined function - "update_task_file"
#
# Create a function "update_task_file" with the parameters "old_task_line" and "new_task_line"
# to update the line of the task file
#
def update_task_file(old_task_line, new_task_line): 
    # If the parameters "old_task_line" and "new_task_line" are not empty, update the line of the task file 
    if old_task_line and new_task_line:
        # Use try and except block to read the text file tasks.txt as the "file" object
        try: 
            with open(f"{current_directory}/{task_file}", "r") as file:
                # Set a list "task_list" to store all the elements "line" in the "file" object
                task_list = [ line.strip() for line in file] 
            # Set a list "updated_list" to empty
            updated_list = []              
            # Use for-loop to update the element "task_line" of the list "task_list"
            for task_line in task_list:
                # If the variable "task_line" is not empty, execute the following if/else statement
                if task_line:
                    # If the element "task_line" is equal to the parameter "old_task_line",
                    # append the element "new_task_line" to the list "updated_list"
                    if task_line.strip() == old_task_line.strip():
                        updated_list.append(f"{new_task_line}\n")
                    # If the element "task_line" is not equal to the parameter "old_task_line", 
                    # append the element "task_line"  to the list "updated_list"
                    else:
                        updated_list.append(f"{task_line}\n")
            # Write the text file tasks.txt as the "file" object
            with open(f"{current_directory}/{task_file}", "w") as file:
                file.writelines(updated_list)
            # Return the true if it is successful
            return True
        # If it fails to update the text file "tasks.txt", print the message to notify the user if it fails to update the text file
        except:
            print(f"Fail to update the text file {task_file}. Please check the current path and the location of the file {task_file}.\n")
            # Return the true if it is a failure
            return False
    # If any other case, print the message to notify the user as the parameters "old_task_line" and "new_task_line" is/are missing
    else:
        print("The parameters of the old/new task line is missing.\n")
        # Return the false if it is a failure
        return False
#
# END: self-defined function - "update_task_file"
#
########################################################################################################################
#
# START: Create self-defined function - "edit_my_tasks"
#
# Create a function "edit_my_task" with the parameters "username_input", "task_number" and "my_task"
# to update the user's task
# 
def edit_my_task(username_input, task_number, my_task):
    # Set a list "task_body" to store the format of the task for display by calling a function "task_format_to_display" 
    task_body = task_format_to_display(my_task)   

    # Set a variable "updated_item" to empty
    updated_item = ""
    # Set a variable "option_input" to empty
    option_input = ""
    # Set a variable "item_number" to empty
    item_number = ""
    # Use while-loop to execute the following statement if the condition is true
    while True:
        # If the variable "option_input" or the variable "item_number" is/are empty, execute the following statement
        if option_input == "" or item_number == "":
            # Print a new line
            print("\n")
            # Print a dotted line separator 
            print(separator_dotted_line + "\n")  
            # Print the parameter "task_number" with the required spaces
            print(f"{(display_width - len(str(task_number)) - 2) *' ' }[{task_number}]")
            # Use for-loop to print the elements of the lists "task_header" and "task_body"
            for item_index, task_header_item in enumerate(task_header):
                # Set a variable "item_index_space" to store the length of the element "item_index"
                item_index_space = len(f"[{len(str(item_index))}]")
                # If the element "item_index" is less than the length of the list "task_header" - 1
                # print the elements of the lists "task_header" and "task_body" 
                if item_index < len(task_header)-1:
                    print(f"[{item_index+1}] {task_header_item}{' ' * ( task_header_length - len(task_header_item) + item_index_space  ) } {task_body[item_index].strip()}")
                # If the element "item_index" is not less than the length of the list "task_header" - 1
                # print the elements of the lists "task_header" and "task_body" with a new line
                else:
                    print(f"[{item_index+1}] {task_header_item}\n {' ' * item_index_space}{task_body[item_index].strip()}\n") 
            # Set the variable "option_input" to store the option the user entered
            option_input = input(f"Please select the option - [Enter 1 to MARK complete, 2 to EDIT task, -1 to EXIT]: ").strip()
            # Print a new line
            print("\n")
            # If the variable "option_input" is "1", ask the user to enter the option for confirmation
            if option_input == "1":
                # Set a variable "is_confirmed" to store the user's option for confirmation, 
                is_confirmed = input(f"Please confirm to MARK complete - [Enter 1 to YES, 2 to NO]: ")
                # If the variable "is_confirmed" is "1", call the function "mark_task_as_complete" with the parameters
                # "username_input", "task_number" and "my_task" mark the task as complete
                if is_confirmed == "1":
                    mark_task_as_complete(username_input, task_number, my_task)
                    # Call the function "print_refresh_task" to print the refresh task
                    # after updated
                    print_refresh_task(username_input, task_number)
                # Use "break" to exit "while-loop"
                break
            # If the variable "option_input" is "2", ask the user to enter the item number for modification,     
            elif option_input == "2":        
                # Set the variable "item_number" to store the item number the user entered
                item_number = input(f"Please enter the item number in the square brackets for modification - [Enter 1/2/4/5/6, or -1 to EXIT]:  ").strip()
                # Print a new line
                print("\n")
                # If the variable "item_number" is "-1", use "break" to exit "while-loop" 
                if item_number == "-1":
                    break                
                # If the variable "item_number" is "3", print the message to notify the user 
                # that the assignment date cannot be changed and use "break" to exit "while-loop"
                elif item_number == "3":
                    print("The assignment date cannot be changed.\n")
                    break
                # If the variable "item_number" is "1", "2", "4", "5" or "6", edit the task 
                elif item_number == "1" or item_number == "2" or item_number == "4" or item_number == "5" or item_number == "6":
                    # Convert the data type of the variable "item_number" from string to integer
                    item_number = int(item_number)
                    # If the variable "item_number" is 5, ask the user to enter the option for confirmation
                    if item_number == 5:
                        # Set the variable "is_confirmed" to store the user's option for confirmation
                        is_confirmed = input(f"Please confirm to MARK complete - [Enter 1 to YES, 2 to NO]: ")
                        # If the variable "is_confirmed" is "1", call the function "mark_task_as_complete" with the parameters
                        # "username_input", "task_number" and "my_task" mark the task as complete
                        if is_confirmed == "1":
                            mark_task_as_complete(username_input, task_number, my_task)
                            # Call the function "print_refresh_task" to print the refresh task
                            # after updated
                            print_refresh_task(username_input, task_number)
                        # Use "break" to exit "while-loop"
                        break
                    # If the variable "item_number" is 1, 2, 4 or 6, update the item of the task
                    elif item_number == 1 or item_number == 2 or item_number == 4 or item_number == 6:  
                        # Set a variable "updated_item" to store the modified item the user entered    
                        updated_item = input(f"Please enter the modified item [{(task_header[item_number-1]).replace(':', '').replace('?','')}]: ").strip()
                        # if the variable "updated_item" is not empty, execute the following statement
                        if updated_item != "":
                            # If the variable "updated_item" contains "," print the message to the user for the valid option
                            if updated_item.find(",") != -1:
                                print("You do not allow to enter a comma (,) in the updated item. Please try again.")
                                # Set the variable "item_number" is empty
                                item_number = ""   
                            # If any other cases, edit the detail of the task                      
                            else: 
                                # Set a variable "current_item" to empty                                                   
                                current_item = ""
                                # Set a dictionary "current_task_dictionary" to store the dictionary 
                                # by calling the function "create_task_dictionary" with the parameter "my_task"
                                current_task_dictionary = create_task_dictionary(my_task)
                                # Set a variable "current_task_line" to store the line of the task 
                                # by calling the function "convert_dictionary_to_task_file_list" with the parameter "current_task_dictionary"
                                current_task_line = convert_dictionary_to_task_file_list(current_task_dictionary) 
                                # Set a dictionary "update_task_dictionary" to copy the dictionary "current_task_dictionary"
                                update_task_dictionary = current_task_dictionary.copy()
                                # If the variable "item_number" is 1, 
                                # set the variable "current_item" to the value of the dictionary "current_task_dictionary" with the key "Task:"
                                # set the value of the dictionary "current_task_dictionary" with the key "Task:" to the variable "updated_item"
                                if item_number == 1:
                                    current_item = current_task_dictionary["Task:"]
                                    update_task_dictionary["Task:"] = updated_item
                                # If the variable "item_number" is 2, 
                                # set the variable "current_item" to the value of the dictionary "current_task_dictionary" with the key "Assigned to:"
                                # set the value of the dictionary "current_task_dictionary" with the key "Assigned to:" to the variable "updated_item"
                                elif item_number == 2:
                                    current_item = current_task_dictionary["Assigned to:"]
                                    update_task_dictionary["Assigned to:"] = updated_item
                                # If the variable "item_number" is 3, 
                                # set the variable "current_item" to the value of the dictionary "current_task_dictionary" with the key "Date Assigned:"
                                # set the value of the dictionary "current_task_dictionary" with the key "Date Assigned:" to the variable "updated_item"
                                elif item_number == 3:
                                    current_item = current_task_dictionary["Date Assigned:"]
                                    update_task_dictionary["Date Assigned:"] = updated_item
                                # If the variable "item_number" is 4, 
                                # set the variable "current_item" to the value of the dictionary "current_task_dictionary" with the key "Due Date:"
                                # set the value of the dictionary "current_task_dictionary" with the key "Due Date:" to the variable "updated_item"
                                elif item_number == 4:
                                    current_item = current_task_dictionary["Due Date:"]
                                    update_task_dictionary["Due Date:"] = updated_item
                                # If the variable "item_number" is 6, 
                                # set the variable "current_item" to the value of the dictionary "current_task_dictionary" with the key "Task Description:"
                                # set the value of the dictionary "current_task_dictionary" with the key "Task Description:" to the variable "updated_item"
                                elif item_number == 6:
                                    current_item = current_task_dictionary["Task Description:"]
                                    update_task_dictionary["Task Description:"] = updated_item
                                # Set the variable "updated_task_line" to store the updated line of the task
                                # by calling the function "convert_dictionary_to_task_file_list" with the parameter "update_task_dictionary"
                                updated_task_line = convert_dictionary_to_task_file_list(update_task_dictionary)                            
                                # Print the variables "item_number", "current_item" and "updated_item" to the user
                                print(f"[{item_number}]: \n{current_item} -> {updated_item}\n")
                                # Set the variable "is_confirmed" to store the user's option for confirmation
                                is_confirmed = input(f"Please confirm to update - [Enter 1 to YES, 2 to NO]: ")
                                # If the variable "is_confirmed" is "1", call the function "update_task_file" with the parameters
                                # "current_task_line" and "updated_task_line"
                                if is_confirmed == "1":
                                    if update_task_file(current_task_line, updated_task_line):  
                                        # Print the message to notify the user as the task is updated successfully
                                        print(f"The task [{item_number}] is updated successfully.\n")
                                        # Call the function "print_refresh_task" to print the refresh task
                                        # after updated
                                        print_refresh_task(username_input, task_number)
                                    # Use "break" to exit "while-loop"
                                    break
                                # If the variable "is_confirmed", set the variable "option_input" to empty
                                # and use "break" to exit "while-loop"
                                elif is_confirmed == "2":
                                    option_input = ""
                                    break
                # If the variable "item_number" is not "1", "2", "4", "5", "6" or "-1", 
                # print the message to notify the user of the invalid option
                # set the variable "item_number" to empty
                else:
                    print("Please enter the invalid item number for modification - [Enter 1/2/4/5/6, or -1 to EXIT] \n")
                    item_number = ""
            # If the variable "option_input" is "-1", use "break" to exit "while-loop"
            elif option_input == "-1":
                break
            # If any other cases for the variable "option_input", print the message to notify the user
            # set the variable "option_input" to empty 
            else:
                print("You enter the invalid option. [Enter 1 to MARK complete, 2 to EDIT task, -1 to EXIT]\n")
                option_input = ""
#
# END: self-defined function - "edit_my_tasks"
#
########################################################################################################################
#
# START: Create self-defined function - "task_format_to_display"
#
# Create a function "task_format_to_display" with the parameter "task_line" 
# to format the line of the task to the list of the formatted task for display
# 
def task_format_to_display(task_line):
    # If the parameter "task_line" is not empty, format the line of parameter"task_line" to the list of the task
    # Set a list "task_body" to empty
    task_body = []
    if task_line:
        # Set a dictionary "task_dictionary" to store the converted dictionary 
        # by calling a function "create_task_dictionary" with the parameter "task_line"
        task_dictionary = create_task_dictionary(task_line) 
        # Set the list "task_body" to store the formatted list of the task with the dictionary "task_dictionary"     
        task_body = [task_dictionary["Task:"], task_dictionary["Assigned to:"], task_dictionary["Date Assigned:"], task_dictionary["Due Date:"], task_dictionary["Task Complete?"], task_dictionary["Task Description:"]]
    # Return the list "task_body"
    return task_body
#
# START: Create self-defined function - "task_format_to_display"
########################################################################################################################
#
# START: Register user
# 
# Create a function "reg_user" to register a new user
#
def reg_user():
    
    new_username = False
    # Print a new line
    print("\n")
    # Ask the user to enter a new username and store it in the variable "new_username_input"
    new_username_input = input("Please enter a new username: ").strip()
    
    while not new_username:
        if check_username_exist(new_username_input):
            print(f"The username {new_username_input} exists. Please enter a new username again.\n")
            new_username_input = input("Please enter a new username: ").strip()
        else:
            new_username = True
            
    # # Ask the user to enter a new password and store it in the variable "new_password_input"
    new_password_input = input("Please enter a new password: ").strip()        
    # Set the variable "username_added" to false for the registration status 
    username_added = False
    # If the variable "new_username_input" and the variable "new_password_input" are not blank,
    # execute the following statements
    if new_username_input and new_password_input: 
        # Use while-loop to execute the following statement if the condition of the variable "username_added" is true 
        while not username_added:
            # Ask the user to enter the password again for confirmation and store it in the variable "new_confirmed_password_input"
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
    # it prints the message to notify the user of the blank input
    else:
        print("You do not enter username/password.\n")
#
# END: Register user
#
########################################################################################################################
#
# START: Add task
#
# Create a function "add_task" to add a new task
#
def add_task():
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
            # Remove the leading and trailing spaces of the username to whom the task is assigned,
            # store it in the variable "username_assigned"
            username_assigned = input("Please enter a username whom the task is assigned: ").strip()
            # If the variable "username_assigned" is empty, print the message to notify the user of the blank input
            if username_assigned == "":
                print("The assigned username is blank.\n")     
        # If the variable "username_assigned" is not empty, proceed to check the variable "task_title"      
        else:
            # If the variable "task_title" is empty, ask the user to enter the title of the task
            if not task_title:
                # Remove the leading and trailing spaces of the title of the task,
                # store it in the variable "task_title"
                task_title = input("Please enter a title of task: ").strip()   
                # If the variable "task_title" is empty, print the message to notify the user of the blank input
                if task_title == "":
                    print("The title of task is blank.\n")   
            # If the variable "task_title" is not empty, proceed to check the variable "task_description"         
            else: 
                # If the variable "task_description" is empty, ask the user to enter a description of the task
                if not task_description:
                    # Remove the leading and trailing spaces of a description of the task,
                    # store it in the variable "task_description"
                    task_description = input("Please enter a description of task: ").strip()
                    # If the variable "task_description" is empty, print the message to notify the user of the blank input
                    if task_description == "":
                        print("The description of task is blank.\n") 
                # If the variable "task_description" is not empty, proceed to check the variable "task_due_date"    
                else:
                    # If the variable "task_due_date" is empty, ask the user to enter the due date of the task
                    if not task_due_date:
                        # Remove the leading and trailing spaces of the due date of the task,
                        # store it in the variable "task_due_date"
                        task_due_date = input("Please enter a due_date of task - [DDMMYYYY]: ").strip()  
                        # If the variable "task_due_date" is empty, print the message to notify the user of the blank input
                        if task_due_date == "":
                            print("The due date of task is blank.\n") 
                        
                    # If the variable "task_due_date" is not empty, proceed to check the validity of variable "task_due_date"    
                    else:
                        # if the variable "task_due_date" is not a digit or the length of the variable "task_due_date" is not equal to 8,
                        # Set the variable "task_due_date" to empty string
                        # Print the message to notify the user of the invalid date format
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
                                # Set a variable "task_is_overdue" to store the status of the overdue the task
                                # by calling the function "check_task_overdue" with the parameter "task_due_date"
                                task_is_overdue = check_task_overdue(task_due_date_formatted)
                                # If the variable "task_is_overdue" is not true, add the task to the text file tasks.txt
                                if not task_is_overdue: 
                                    # Create a current date object and store it in the variable "today"
                                    today = datetime.now()
                                    # Set the variable "task_assigned_date" to store a assigned date of task
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
                                    # Print a dotted line separator
                                    print(separator_dotted_line + "\n")     
                                    # Print the detail of the newly added task                     
                                    print_newly_added_task(task_body)
                                    # Set a variable "added_again" to store the the option user entered for adding a new task again
                                    added_again = input(f"Do you need to add a new task again? - [Enter 1 to YES, 2 to NO]: ").strip()
                                    print("\n")
                                    # If the variable "added_again" is "1", set the variables "username_assigned", "task_title", "task_description"
                                    # and "task_due_date" to empty for reinput the new task
                                    if added_again == "1":
                                        username_assigned = ""
                                        task_title = ""
                                        task_description = ""
                                        task_due_date = ""
                                    # If the variable "added_again" is "2",
                                    # Set the variable "task_added" to true to exit the while-loop after adding a new task  
                                    elif added_again == "2":                                        
                                        task_added = True
                                        
                                    
                                       
                                    
                                # If the variable "task_is_overdue" is true, print the message to notify the user 
                                # that the due date of the task should be later than today's date.
                                # set the variable "task_due_date" to empty
                                else:
                                    print(f"The due date of the task should be later than today's date.\n")
                                    task_due_date = ""
#
# END: Add task 
#                              
########################################################################################################################
#
# START: View all tasks
#
# Create a function "view_all" to view all the tasks
#
def view_all():
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
        for task_index, task in enumerate(all_tasks):
            # Set a dictionary "task_dictionary" to store the dictionary by calling the function "create_task_dictionary"
            # with the parameter "task"
            task_dictionary = create_task_dictionary(task)
            # Set a variable "task_due_date" to store the value of the dictionary "task_dictionary" with its key "Due Date:"
            task_due_date = task_dictionary["Due Date:"]
            # Set a variable "task_complete" to store the value of the dictionary "task_dictionary" with its key "Task Complete?"
            task_complete = task_dictionary["Task Complete?"]
            # Set a variable "task_is_overdue" to store the status of the overdue the task
            # by calling the function "check_task_overdue" with the parameter "task_due_date"
            task_is_overdue = check_task_overdue(task_due_date)
            # Set a variable "overdue_flag" to [OVERDUE] if the variable "task_is_overdue" is true, otherwise set it to empty
            overdue_flag = "[OVERDUE]" if task_is_overdue else ""
            # Set a variable "completed_flag" to [DONE] if the variable "DONE" is "Yes", otherwise set it to empty
            completed_flag = "[DONE]" if task_complete.lower() == "Yes".lower() else ""
            # Set a list "task_body" to store the formatted task for display 
            # by calling the function "task_format_to_display" with the parameter "task"
            task_body = task_format_to_display(task)
            # If the list "task_body" is not empty, print the details of all the tasks  
            if task_body:
                # Print a new line with a separator "-"
                print(separator_dotted_line + "\n")
                # Print the variables "task_index", "overdue_flag" and "completed_flag" with the required spaces
                print(f"{(display_width - len(str(task_index+1)) - 2 - len(overdue_flag) - len(completed_flag)) *' ' }{overdue_flag}{completed_flag}[{task_index + 1}]")
                # Use for-loop to print the elements  "task_header" and "task_body" for all the elements
                for item_index, task_header_item in enumerate(task_header):
                    # If the variable "item_index" is less than the length of the list "task_header" - 1
                    # print the elements of the lists "task_header" and "task_body" for all the elements
                    if item_index < len(task_header) - 1:
                        print(f"{task_header[item_index]}{' ' * (task_header_length-len(task_header[item_index]))} {task_body[item_index]}")
                    # If the variable "item_index" is not less than the length of the list "task_header" - 1
                    # print the elements of the lists "task_header" and "task_body" for all the elements with a new line
                    else:
                        print(f"{task_header[-1]}\n {task_body[-1]}\n")  
        # Print a dotted line separator
        print(separator_dotted_line + "\n")
    # If the list "all_tasks" is empty, print the message to notify the user with a new line
    else:
        print("\n")
        print("No task is found in our task records!\n")
#
# END: View all tasks
#
########################################################################################################################
#
# START: View my task
#
# Create a function "view_mine" to view all the tasks
#
def view_mine():
    # Use while-loop to execute the following statements if the condition is true
    while True:        
        # Set the empty list "user_tasks"
        user_tasks = []
        # Read the text file "tasks.txt" as the "file" object
        with open(f"{current_directory}/{task_file}", "r") as file:
            # Use for-loop to add all the elements "task_line" in the "file" object to the list "user_tasks"
            # if the index 0 element of the variable "task_line" is matched with the variable "username_input"
            user_tasks = [task_line for task_line in file if task_line.split(",")[0].strip().find(username_input) != -1]
        # If the list "user_tasks" is not empty, print the details of the tasks to notify the user 
        if user_tasks:
            print(f"\nView my tasks - {username_input} [No. of tasks: {len(user_tasks)}]\n ")
            # Set a list "editable_task_index_list" to empty
            editable_task_index_list = []
            # Use for-loop to extract the element of the variable "task" in the list "user_tasks"
            for task_index, task in enumerate(user_tasks):
                # Set a dictionary "task_dictionary" to store the dictionary by calling the function "create_task_dictionary"
                # with the parameter "task"
                task_dictionary = create_task_dictionary(task)
                # Set a variable "task_due_date" to store the value of the dictionary "task_dictionary" with its key "Due Date:"
                task_due_date = task_dictionary["Due Date:"]
                # Set a variable "task_complete" to store the value of the dictionary "task_dictionary" with its key "Task Complete?"
                task_complete = task_dictionary["Task Complete?"]                
                # Set a variable "task_is_overdue" to store the status of the overdue the task
                # by calling the function "check_task_overdue" with the parameter "task_due_date"                
                task_is_overdue = check_task_overdue(task_due_date)
                # Set a variable "overdue_flag" to [OVERDUE] if the variable "task_is_overdue" is true, otherwise set it to empty
                overdue_flag = "[OVERDUE]" if task_is_overdue else ""
                # Set a variable "completed_flag" to [DONE] if the variable "DONE" is "Yes", otherwise set it to empty
                completed_flag = "[DONE]" if task_complete.lower() == "Yes".lower() else ""
                # Set a list "task_body" to store the formatted task for display 
                # by calling the function "task_format_to_display" with the parameter "task"
                task_body = task_format_to_display(task)
                # If the variable "task_complete" is "No" and the variable "task_is_overdue" is not true,
                # append the index "task_index" to the list of "editable_task_index_list"
                if task_complete.lower() == "No".lower() and not task_is_overdue:
                    editable_task_index_list.append(task_index)
                # If the list "task_body" is not empty, print the details of my tasks  
                if task_body:
                    # Print a new line with a separator "-"
                    print(separator_dotted_line + "\n")
                    # Print the variables "task_index", "overdue_flag" and "completed_flag" with the required spaces
                    print(f"{(display_width - len(str(task_index+1)) - 2 - len(overdue_flag) - len(completed_flag)) *' ' }{overdue_flag}{completed_flag}[{task_index + 1}]")
                    # Use for-loop to print the elements  "task_header" and "task_body" for all the elements
                    for item_index, task_header_item in enumerate(task_header):
                        # If the variable "item_index" is less than the length of the list "task_header" - 1
                        # print the elements of the lists "task_header" and "task_body" for all the elements                        
                        if item_index < len(task_header)-1:
                            print(f"{task_header[item_index]}{' ' * (task_header_length-len(task_header[item_index]))} {task_body[item_index]}")
                        # If the variable "item_index" is not less than the length of the list "task_header" - 1
                        # print the elements of the lists "task_header" and "task_body" for all the elements with a new line
                        else:
                            print(f"{task_header[-1]}\n {task_body[-1]}\n")    

            # If the list "editable_task_index_list" is not empty, execute the following statements
            if editable_task_index_list:
                # Print a dotted line separator
                print(separator_dotted_line + "\n")
                # Set a variable "task_number" to store the task number the user entered
                task_number = input(f"Please enter task number in the square brackets for modification - [Enter number except [OVERDUE]/[DONE], or -1 to EXIT]:   ").strip()
                # Print a new line
                print("\n")
                # If the variable "task_number" is "-1", use "break" to exit "while-loop"
                if task_number == "-1":
                    break
                # If the variable "task_number" is "-1", execute the following statements
                else:
                    # If the variable "task_number" is not a digit, print the message to notify the user of an invalid task number
                    if not task_number.isdigit():
                        print("Please enter the task number in the square brackets, i.e. [#] . Please try again.\n")
                    # If the variable "task_number" is a digit, print the message to notify the user 
                    # that the status of the invalid task number the user entered
                    else:
                        # Convert the data type of the variable "task_number" from string to the integer 
                        task_number = int(task_number)
                        # If the variable "task_number" - 1 is less than the length of the list "user_tasks"
                        if task_number -1 < len(user_tasks):
                            # Set a dictionary "task_dictionary" to store the dictionary by calling the function "create_task_dictionary"
                            # with the parameter "user_tasks" with the index variable "task_number" - 1
                            task_dictionary = create_task_dictionary(user_tasks[task_number-1])
                            # Set a variable "task_due_date" to store the value of the dictionary "task_dictionary" with its key "Due Date:"
                            task_due_date = task_dictionary["Due Date:"]
                            # Set a variable "task_complete" to store the value of the dictionary "task_dictionary" with its key "Task Complete?"
                            task_complete = task_dictionary["Task Complete?"]
                            # Set a variable "task_is_overdue" to store the status of the overdue the task
                            # by calling the function "check_task_overdue" with the parameter "task_due_date"
                            task_is_overdue = check_task_overdue(task_due_date)
                            # If the variable "task_is_overdue" is not true and the variable "task_complete" is "No",
                            # call the function "edit_my_task" with the parameters "username_input", "task_number" and 
                            # "user_tasks" with the index variable "task_number" - 1
                            if not task_is_overdue and task_complete.lower() == "No".lower(): 
                                edit_my_task(username_input, task_number, user_tasks[task_number-1])
                            # If the variable "task_is_overdue" is true or the variable "task_complete" is "Yes",
                            # print the message to notify the user that the status of the task is either overdue or marked as completed 
                            # Use "break" to exit "while-loop"
                            elif task_is_overdue or task_complete.lower() == "Yes".lower():
                                print(f"The task [{task_number}] has been overdue/marked as complete. No amendment is allowed.\n")
                                break
                        # If the variable "task_number" is not in the range of the list "user_tasks",
                        # print the message to notify the user that the task number is out of range
                        # Use "break" to exit "while-loop"
                        else:
                            editable_task_index_option_list = [editable_option + 1 for editable_option in editable_task_index_list ]  
                            print(f"You enter the task number out of the range - {editable_task_index_option_list}.\n")
                            break
            # If the list "editable_task_index_list" is empty, print the message to notify the user 
            # that all the tasks are overdue/marked as complete
            # use "break" to exit "while-loop"
            else:            
                print("All your tasks are overdue/marked as completed. No amendment is allowed.\nYou can choose to view all task.\n")
                break      
        # If the list "all_tasks" is empty, print the message to notify the user that no task is found in the text file tasks.txt 
        # Print a new line and use "break" to exit "while-loop"
        else:
            print("\n")
            print(f"No task is found in the text file {task_file}!\n")
            break
#
# END: View my task
#
########################################################################################################################
#
# START: Display statistics
#
# Create a function "display_status" to display statistics
#
def display_statistics():
    # Set a variable "is_displayed_report" to false
    is_displayed_report = False
    # Use while-loop to display the report if the condition is true
    while not is_displayed_report:            
        # Set a variable "overview_type" to store the type of the report to be displayed
        overview_type = input(f"Please select the type of the report to view - [Enter 1 to TASK OVERVIEW, 2 to USER OVERVIEW, -1 to exit]: ").strip()
        # Print a new line
        print(f"\n")
        # If the variable "overview_type" is "1", print the task overview to the user
        if overview_type == "1": 
            # Set a list "task_overview_list" to store the list of the task overview for display
            # by calling the function "get_task_overview_list"
            task_overview_list  = get_task_overview_list()
            # If the list "task_overview_list" is not empty, print the detail of the list "task_overview_list"
            if task_overview_list:
                # Print the header line to the user
                print(f"Here is the report of task overview - {username_input}\n")
                # Use for-loop to print all the elements "task_line" in the list "task_overview_list"
                for task_line in task_overview_list:
                    print(f"{task_line}")
                # Print a new line
                print("\n")
            # If the list "task_overview_list" is empty, print the message to notify the user
            else:
                print(f"Fail to load the report for task overview. Please check the current path and the location of the text file {task_overview_file}.\n")
        # If the variable "overview_type" is "2", print the user overview to the user
        elif overview_type == "2":
            # Set a list "user_overview_list" to store the list of the user overview for display
            # by calling the function "get_user_overview_list"
            user_overview_list  = get_user_overview_list()
            # If the list "user_overview_list" is not empty, print the detail of the list "user_overview_list"
            if user_overview_list:
                # Print the header line to the user
                print(f"Here is the report of task overview - {username_input}\n")
                # Use for-loop to print all the elements "user_line" in the list "user_overview_list"
                for user_line in user_overview_list:
                    print(f"{user_line}")
                # Print a new line
                print("\n")
            # If the list "task_overview_list" is empty, print the message to notify the user
            else:
                print(f"Fail to load the report for user overview. Please check the current path and the location of the text file {user_overview_file}.\n")
        # If the variable "overview_type" is "-1", use "break" to exit "while-loop"
        elif overview_type == "-1":
            break
        # If any other cases, print the message to notify the user of the invalid option for the report.
        else:
            print("You enter the invalid option for the reports - [Enter 1 to TASK OVERVIEW, 2 to USER OVERVIEW, -1 to EXIT]\n")
            # Set the variable "is_displayed_report" to false
            is_displayed_report = False
        # If the variable "overview_type" is "1" or the variable "overview_type" is "2", ask the user to generate the report again
        if overview_type == "1" or overview_type == "2":
            # Set a variable "is_displayed_again" to store the option the user entered
            is_displayed_again = input("Do you need to display the report again? - [Enter 1 to YES, 2 to NO]: ").strip()
            # Print a new line
            print("\n")
            # Set the variable "is_displayed_report" to false if the variable "is_displayed_again" is "1", 
            # otherwise set it to false
            is_displayed_report = False if is_displayed_again == "1" else True
            # Print a dotted line separator
        print(separator_dotted_line + "\n")            
        
#
# END: Display statistics       
#
########################################################################################################################
#
# START: Generate reports
#
# Create a function "generate_report" to generate reports
#
def generate_report():
    # Set a variable "is_generated_report" to false
    is_generated_report = False
    # Use while-loop to display the report if the condition is true
    while not is_generated_report:
        # Set a variable "report_type" to store the type of the report to be generated 
        report_type = input("Please select the report to be generated - [Enter 1 to TASK OVERVIEW, 2 to USER OVERVIEW, -1 to EXIT]: ").strip()
        # Print a new line
        print("\n")
        # If the variable "report_type" is "1", generate the task overview report for the user
        if report_type == "1":
            # Set a list "task_overview_list" to store the list of the task overview for generation
            # by calling the function "get_task_overview_list"
            task_overview_list = get_task_overview_list()
            # Call the function "generate_file" with the parameters "task_overview_file" and "task_overview_list" to generate the text file
            # If the return value is true, print the message to notify the user 
            if generate_file(task_overview_file, task_overview_list):
                print(f"The text file {task_overview_file} is generated successfully. - {username_input}\n")
                # Print a dotted line separator
                print(separator_dotted_line + "\n")
        # If the variable "report_type" is "2", generate the user overview report for the user
        elif report_type == "2":
            # Set a list "user_overview_list" to store the list of the user overview for generation
            # by calling the function "get_user_overview_list"
            user_overview_list = get_user_overview_list()
            # Call the function "generate_file" with the parameters "user_overview_file" and "user_overview_list" to generate the text file
            # If the return value is true, print the message to notify the user 
            if generate_file(user_overview_file, user_overview_list):
                print(f"The text file {user_overview_file} is generated successfully.- {username_input}\n")
                # Print a dotted line separator
                print(separator_dotted_line + "\n")
        # If the variable "overview_type" is "-1", use "break" to exit "while-loop"
        elif report_type == "-1":
            break
        # If any other cases, print the message to notify the user of the invalid option
        else:
            print("You enter the invalid option for the reports - [Enter 1 to TASK OVERVIEW, 2 to USER OVERVIEW, -1 to EXIT]\n")
            # Set the variable "is_generated_report" to false
            is_generated_report = False
        # If the variable "report_type" is "1" or the variable "report_type" is "2", ask the user to generate the report again
        if report_type == "1" or report_type == "2":
            # Set a variable "is_generated_again" to store the option the user entered
            is_generated_again = input("Do you need to generate the report again? - [Enter 1 to YES, 2 to NO, -1 to EXIT]: ").strip()
            # Print a new line
            print("\n")
            # Set the variable "is_generated_report" to false if the variable "is_generated_again" is "1", 
            # otherwise set it to false
            is_generated_report = False if is_generated_again == "1" else True
            # Print a dotted line separator
        print(separator_dotted_line + "\n")

#
# END: Generate report       
#
########################################################################################################################
#
# START: login function
#
def login():    
    # Create an empty list "usernames" to store a list of usernames 
    usernames = []
    # Create an empty list "passwords" to store a list of passwords 
    passwords = []
    # Use try and except block to open the text file "user.txt" as the "file" object
    try: 
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
    except:
        print(f"Please check the current directory and the location of the text file {user_file}\n")
        exit()
        
    # Ask the user to enter the username and store it in the variable "username_input"
    username_input = input("Please enter your username: ").strip()
    # Ask the user to enter the password and store in the variable "password_input"
    password_input = input("Please enter your password: ").strip()
    # Set the variable "logged" to false for the login status
    logged = False
    admin_login = False
    # Use while-loop to execute the following statements if the condition of the variable "logged" is true 
    while not logged:
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
            # If the user enters the incorrect username/password, print the error message to the user
            # Note: It does not reveal the specific type of error to the user due to security concern
            else:
                print("Username and/or password are incorrect.\n")
                # Use a break to stop the while-loop
                break
        # If the username is not found in the list "username", print the error message to the user
        # Note: It does not reveal the specific type of error to the user due to security concern
        else:
            print("Username and/or password are incorrect.\n")
            # Use a break to stop the while-loop
            break
    return [logged, admin_login, username_input]
#
# END: login function
#
########################################################################################################################
#
# ====Login Section====
'''Here you will write code that will allow a user to log in.
    - Your code must read usernames and passwords from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file.
    - Use a while loop to validate your username and password.
'''
#
########################################################################################################################
#
# START: Login Section
#
# Call a function to "print_banner" for login
print_banner()
#
#
print(f"Accounts for testing - \nusername: admin\t\tusername: boss\npassword: adm1n \tpassword: b0ss\n")
#
# Set a list "login_status" to store the login status by calling a function "login"
login_status = login()
# Set a variable "logged" to store index 0 of the list "login_status" as the login status
logged = True if login_status[0] else False
# Set a variable "admin_login" to store index 1 of the list "login_status" as the admin login status
admin_login = True if login_status[1] else False
# Set a variable "username_input" to store index 2 of the list "login_status" as the username input
username_input = login_status[2] 
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
    # Set the variable "register_user_option" to "r - Register user" if the variable "admin_login" is true,
    # otherwise it sets to false
    register_user_option = "r - register user\n" if admin_login else ""
    # Set the variable "generate_report_option to "gr - generate report"
    generate_report_option = "gr - generate report\n" if admin_login else ""
    # Set the variable "display_statistics_option" to "ds - display statistics" if the variable "admin_login" is true,
    # otherwise it sets to false    
    display_statistics_option = "ds - display statistics\n" if admin_login else ""
    #
    # ******************************************************************************************************************
    #
    # Amend the variable "menu" by using the f-string
    menu = input(f"Select one of the following Options below:\n\
{register_user_option}\
a - add task\n\
va - view all tasks \n\
vm - view my tasks\n\
{generate_report_option}\
{display_statistics_option}\
e - exit\n\
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

        # Call a function "reg_user" to register a new user
        reg_user()

########################################################################################################################
        
    elif menu == 'a':
        # pass
        '''In this block, you will put code that will allow a user to add a new task to task.txt file
        - You can follow these steps:
            - Prompt a user for the following: 
                - A username of the person to whom the task is assigned,
                - A title of a task,
                - A description of the task and 
                - the due date of the task.
            - Then get the current date.
            - Add the data to the file task.txt and
            - You must remember to include the 'No' to indicate if the task is complete.'''
        
        # Call a function "add_task" to add a new task
        add_task()

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

        # Call a function "view_all" to view all the tasks
        view_all()

########################################################################################################################

    elif menu == 'vm':
        # pass
        '''In this block, you will put code the that will read the task from the task.txt file and
         print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
         You can do it in this way:
            - Read a line from the file
            - Split the line where there is a comma and space.
            - Check if the username of the person logged in is the same as the username you have
            read from the file.
            - If they are the same print it in the format of Output 2 in the task PDF'''

        #  Call a function "view_mine" to view all the tasks
        view_mine()
        
########################################################################################################################

    elif menu == 'e':
        # Add a new line
        print('Goodbye!!!\n')
        exit()

# **********************************************************************************************************************
#
# START: Display statistics
#   
    # If the variable "menu" is "ds" and the variable "admin_login" is true, 
    # it displays the option of displaying statistics
    elif menu == "ds" and admin_login:
        display_statistics()
#
# END: Display statistics
#
# **********************************************************************************************************************
#
# START: Generate report
#   
    # If the variable "menu" is "gr" and the variable "admin_login" is true, 
    # it displays the option of generating statistics
    elif menu == "gr" and admin_login:        
        generate_report()
#   
# END: Generate report 
#
# **********************************************************************************************************************
    else:
        # Add a new line
        print("\n")
        # Add a new line
        print("You have made a wrong choice, Please Try again.\n")
