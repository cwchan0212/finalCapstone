# Task 48 - Capstone Project V
# Compulsory Task
# Project Name: Book Management System
# bookstore.py
# Author: Eddy Chan, Chi-wai
# Date: 28 December 2022
# -------------------------------------------------------------------------------------------------------------- #
# Import sqlite3, time and tabulate library
import sqlite3, time

# The task requires importing tabulate library  
# use try and except block to import the library
try:
    from tabulate import tabulate    
    tabulate.PRESERVE_WHITESPACE = True
# If the user does not install the tabulate library, print the message to notify the user
# and tell him/her how to install it.
except ModuleNotFoundError as error:
    print (f"Please install the module tabulate by:\n  pip install tabulate")
    exit()

# -------------------------------------------------------------------------------------------------------------- #
# Set environment variables and setting
# -------------------------------------------------------------------------------------------------------------- #
# Set a list "field_list" to store the field names of the table
field_list = ["id", "title", "author", "qty"]
field_list = [field.upper() for field in field_list]
# Set a variable "db_file" to "ebookstore"
db_file = "ebookstore"
# Set a variable "table_name" to "books"
table_name = "books"
# Set a variable "display_width" to 120 for display purpose
display_width = 104
# Set a variable "dotted_line_separator" to a dotted line separator for display purpose
dotted_line_separator = f"{'-' * display_width}"
# Set a variable "double_dash_separator" to a dotted line separator for display purpose
double_dash_separator = f"{'=' * display_width}"
# -------------------------------------------------------------------------------------------------------------- #
# Self-defined functions
# -------------------------------------------------------------------------------------------------------------- #
# Start: print_separator
#      
# Create a function "print_separator" to print the separator
def print_separator(): 
    # Set a variable "line" to store the string of the separator
    line = f"\n# {'-' * 100} #\n"
    print(line)
#
# End: print_separator
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
# End: colored_text
# -------------------------------------------------------------------------------------------------------------- #
# Start: check_positive_string_number
#
# Create a function "check_positive_string_number" with the parameter "number" to check whether the string number is positive or negative
def check_positive_string_number(number):
    # If the parameter "number" is a digit after the removal of "+-", the counts of "+" and "-" are less than or equal to 1,
    # execute the following if/else statements
    # Set the variable "is_positive" to false as the default value
    # i.e. deal with the string that cannot be converted to int
    is_positive = -1
    if number.lstrip("+-").isdigit() and number.count("-") <=1 and number.count("+") <= 1:
        # If the parameter "number" (after converted to int) is greater than 0, set the variable "is_positive" to true,
        # otherwise set the variable "is_positive" to false
        is_positive = 1 if int(number) > 0 else 0    
    # return the variable "is_positive"
    return is_positive
#
# End: check_positive_string_number
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
        "######## ########   #######   #######  ##    ##  ######  ########  #######  ########  ######## ",
        "##       ##     ## ##     ## ##     ## ##   ##  ##    ##    ##    ##     ## ##     ## ##       ",
        "##       ##     ## ##     ## ##     ## ##  ##   ##          ##    ##     ## ##     ## ##       ",
        "######   ########  ##     ## ##     ## #####     ######     ##    ##     ## ########  ######   ",
        "##       ##     ## ##     ## ##     ## ##  ##         ##    ##    ##     ## ##   ##   ##       ",
        "##       ##     ## ##     ## ##     ## ##   ##  ##    ##    ##    ##     ## ##    ##  ##       ",
        "######## ########   #######   #######  ##    ##  ######     ##     #######  ##     ## ######## "
    ]   
    # Print a double dash separator with the variable "double_dash_separator"
    print(f"\n{double_dash_separator}\n")
    # Use for-loop to print each element "line" in the list "logo_list"
    for line in logo_list:
        # Set the variable "logo_line" to store the elements of the line with the required spaces
        logo_line = f"{' ' * ((display_width - len(line))//2) }{line}"
        # Print the colored text of the logo by calling the function "colored_text"
        print(f"{colored_text('bold', f'{logo_line}')}")
        # print(f"{' ' * ((display_width - len(line))//2) }{line}")
    # Set a variable "menu_header" to store the menu header
    menu_header = "==Management System=="
    # Set a variable "menu_header_with_space" to store the menu header with space
    menu_header_with_space = " ".join([character.upper() for character in menu_header])
    # Print the variable "menu_header_with_space" with the required spaces
    print(f"\n{' ' * ((display_width - len(menu_header_with_space))//2) }{colored_text('bold',f'{menu_header_with_space}')}")    
    # Print a double dash separator with the variable "double_dash_separator"
    print(f"\n{double_dash_separator}\n")
#
# END: print_banner
# -------------------------------------------------------------------------------------------------------------- #
# Start: create_connection
# 
# Create a function "create_connection" with the parameter "db_file"
def create_connection(db_file):
    # Set an object "db" to None
    db = None
    # Use try and catch block to create a connection
    try: 
        # Creates or opens a file "python_programming" with a SQLite3 DB
        db  = sqlite3.connect(f"{db_file}")
        # Return the "db" object
        return db
    # If it fails to create a database connection, print a message to notify the user and exit the program
    except sqlite3.OperationalError as error:
        print(f"Fail to create database connection. [{error.sqlite_errorcode} - {error.sqlite_errorname}]\n")
        exit()
#
# End: create_connection
# -------------------------------------------------------------------------------------------------------------- #
# Start: drop_table
#
# Create a function "drop_table" with the parameter "db"
def drop_table(db):
    # Set a variable "status" to false    
    status = False
    # Use try and catch block to drop existing table "python_programming_db"
    try:
        # Set a variable "sql_statement" to store the SQL statement for dropping a table
        sql_statement = (f"DROP table IF EXISTS {table_name}")
        # Set a "cursor" object
        cursor = db.cursor()
        # Execute the SQL statement to create a table
        cursor.execute(sql_statement)
        # Print the message to notify the user for dropping a table
        print(f"Drop the table {table_name} successfully.\n")
        # Set the variable "status" to true
        status = True
    # If it fails to drop the table, print a message to notify the user and exit the program
    except sqlite3.OperationalError as error:
        print(f"Fail to drop the table {table_name}. [{error.sqlite_errorcode} - {error.sqlite_errorname}]\n")
        exit() 
    # Return the variable "status"
    return status
#
# End: drop_table
# -------------------------------------------------------------------------------------------------------------- #
# Start: create_table
#
# Create a function "create_table" with the parameters "db"
def create_table(db):
    # Set a variable "status" to false
    status = False
    # Use try and catch block to create a table
    try:
        # Set a variable "sql_statement" to store the SQL statement for creating a table
        sql_statement = (f"CREATE TABLE IF NOT EXISTS {table_name} (\
        id INTEGER PRIMARY KEY,\
        title VARCHAR(50) NOT NULL,\
        author VARCHAR(50) NOT NULL,\
        qty INTEGER NOT NULL)\
        ")
        # Set a "cursor" object
        cursor = db.cursor()
        # Execute the SQL statement to create a table
        cursor.execute(sql_statement)
        # Print the message to notify the user for dropping a table
        print(f"Create the table {table_name} successfully.\n")
        # Set the variable "status" to true
        status = True
    # If it fails to create a table, print a message to notify the user and exit the program
    except sqlite3.OperationalError as error:
        print(f"Fail to create the table {table_name}. [{error.sqlite_errorcode} - {error.sqlite_errorname}]\n")
        exit()
    # Return the variable "status"
    return status
#
# End: create_table
# -------------------------------------------------------------------------------------------------------------- #
# Start: insert_record
#
# Create a function "insert_record" with the parameters "db" and "value_list" 
def insert_record(db, value_list):
    # Set a variable "row_affected" to -1 and store the row(s) affected later
    row_affected = -1
    # Use try and catch block to insert record(s)
    try:
        print(f"\nTry to insert records...")
        # Set a variable "sql_statement" to store the SQL statement for inserting record(s)
        sql_statement = f"INSERT INTO {table_name} (id, title, author, qty) VALUES (?, ?, ?, ?)"
        # Set a tuple "value_tuple" to store the list "value_list" after conversion of data type
        value_tuple = tuple(value_list)
        # Set a "cursor" object
        cursor = db.cursor()
        # Execute the SQL statement with the tuple "value_tuple" to insert many record(s)
        row_affected = cursor.executemany(sql_statement, value_tuple)
        # Commit the transaction
        db.commit()
        # Set the variable "last_record_id" to store the ID of the row just inserted
        last_record_id = cursor.lastrowid
        # Resets all results - the cursor object has no reference to its original connection object
        cursor.close()
        # Return the row count of the variable "row_affected"
        return row_affected.rowcount
    # If it fails to insert record(s), print a message to notify the user and exit the program
    except sqlite3.OperationalError as error:
        print(f"Fail to insert the record(s) into the {table_name}. [{error.sqlite_errorcode} - {error.sqlite_errorname}]\n")
        exit()
#
# End: insert_record
# -------------------------------------------------------------------------------------------------------------- #
# Start: select_all_records
#       
# Create a function "select_all_records" with the parameter "db" to select all records
def select_all_records(db):
    # Set a list "record" to empty
    records = []
    # Use try and catch block to select all records
    try:
        # Set a variable "sql_statement" to store the SQL statement for selecting all records
        sql_statement = f"SELECT * FROM {table_name} ORDER BY id"
        # Set a "cursor" object
        cursor = db.cursor()
        # Execute the SQL statement with the tuple "value_tuple" to insert many record(s)
        cursor.execute(sql_statement)
        # Set the list "record" to store all the fetched records
        records = cursor.fetchall()
        # Resets all results - the cursor object has no reference to its original connection object
        cursor.close()
        # Return the list "record"
        return records
    # If it fails to select all records, print a message to notify the user and exit the program
    except sqlite3.OperationalError as error:
        print(f"Fail to select all record(s) from {table_name}. [{error.sqlite_errorcode} - {error.sqlite_errorname}]\n")
        exit() 
#
# End: select_all_records
# -------------------------------------------------------------------------------------------------------------- #
# Start: select_record_by_search_option
#  
# Create a function "select_record_by_author" with the parameter "db", "value_list" and "search_option" 
# to get the record(s) by title or author 
def select_record_by_search_option(db, value_list, search_option):
    # Set a list "records" to empty
    records = []
    # Use try and catch block to select the records by search option (i.e. title or author)
    try:
        # If the variable "search_option" is 1, set the variable "sql_statement" to search by id
        if search_option == 1: 
            sql_statement = f"SELECT * from {table_name} where id = ?"
        # If the variable "search_option" is 2, set the variable "sql_statement" to search by title
        elif search_option == 2:
            sql_statement = f"SELECT * from {table_name} where title like ?"
        # If the variable "search_option" is 3, set the variable "sql_statement" to search by author    
        elif search_option == 3:
            sql_statement = f"SELECT * from {table_name} where author like ?" 
        # If the variable "search_option" is 4, set the variable "sql_statement" to search by quantity    
        elif search_option == 4:
            sql_statement = f"SELECT * from {table_name} where qty >= ? and qty <= ?"            
        # Set a tuple "value_tuple" to store the list "value_list" after conversion of data type
        value_tuple = tuple(value_list)
        # Set a "cursor" object
        cursor = db.cursor()
        # Set the variable "row_affected" to store the row(s) affected after executed SQL statement        
        cursor.execute(sql_statement, value_tuple)
        # Set the list "record" to store all the fetched records
        records = cursor.fetchall()
        # Resets all results - the cursor object has no reference to its original connection object
        cursor.close()
        # Return the list "record"
        return records
    # If it fails to select records, print a message to notify the user and exit the program
    except sqlite3.OperationalError as error:
        print(f"Fail to select record(s) from {table_name}. [{error.sqlite_errorcode} - {error.sqlite_errorname}]\n")
        exit() 
#
# End: select_record_by_search_option
# -------------------------------------------------------------------------------------------------------------- #
# Start: select_record
#  
# Create a function "select_record" with the parameter "db" and "value_list" to get the record by id
def select_record(db, value_list):
    # Set a list "records" to empty
    records = []
    # Use try and catch block to select all records
    try:
        # Set a variable "sql_statement" to store the SQL statement for selecting the max id among the records
        sql_statement = f"SELECT * from {table_name} where id = ?"
        # Set a tuple "value_tuple" to store the list "value_list" after conversion of data type
        value_tuple = tuple(value_list)
        # Set a "cursor" object
        cursor = db.cursor()
        # Set the variable "row_affected" to store the row(s) affected after executed SQL statement        
        cursor.execute(sql_statement, value_tuple)
        # Set the list "record" to store all the fetched records
        records = cursor.fetchall()
        # Resets all results - the cursor object has no reference to its original connection object
        cursor.close()
        # Return the list "record"
        return records
    # If it fails to select all records, print a message to notify the user and exit the program
    except sqlite3.OperationalError as error:
        print(f"Fail to select all record(s) from {table_name}. [{error.sqlite_errorcode} - {error.sqlite_errorname}]\n")
        exit() 
#
# End: select_record
# -------------------------------------------------------------------------------------------------------------- #
# Start: generate_new_id
#  
# Create a function "generate_new_id" with the parameter "db" to get the new id of the record
def generate_new_id(db):
    # Set a list "records" to empty
    records = []
    # Set a variable "new_id" to -1 as the initial value of the id
    new_id = -1
    # Use try and catch block to select all records
    try:
        # Set a variable "sql_statement" to store the SQL statement for selecting the max id among the records
        sql_statement = f"SELECT MAX(id) AS max_id from {table_name}"
        # Set a "cursor" object
        cursor = db.cursor()
        # Execute the SQL statement with the tuple "value_tuple" to insert many record(s)
        cursor.execute(sql_statement)
        # Set the list "record" to store all the fetched records
        records = cursor.fetchall()
        # Resets all results - the cursor object has no reference to its original connection object
        cursor.close()
        # Return the variable "new_id" by assigning the index 0 of the list "records"
        # If no records are found, set the variable "new_id" to -1
        new_id = records[0][0] + 1 if records else -1
        # Return the variable "new_id"
        return new_id
    # If it fails to select all records, print a message to notify the user and exit the program
    except sqlite3.OperationalError as error:
        print(f"Fail to select all record(s) from {table_name}. [{error.sqlite_errorcode} - {error.sqlite_errorname}]\n")
        exit() 
#
# End: generate_new_id
# -------------------------------------------------------------------------------------------------------------- #
# Start: update_record
#  
# Create a function "update_record" with the parameters "db" and "value_list" to update the records by id
def update_record(db, value_list):
    # Set a variable "row_affected" to -1 and store the row(s) affected later
    row_affected = -1
    # Use try and catch block to update record(s) by name
    try:
        # Set a variable "sql_statement" to store the SQL statement for updating record(s) by name
        sql_statement = f"UPDATE {table_name} SET title = ?, author = ?, qty = ? WHERE id = ?"
         # Set a tuple "value_tuple" to store the list "value_list" after conversion of data type
        value_tuple = tuple(value_list)
        # Set a "cursor" object
        cursor = db.cursor()
        # Set the variable "row_affected" to store the row(s) affected after executed SQL statement
        row_affected = cursor.execute(sql_statement, value_tuple)
        # Commit the transaction
        db.commit()
        # Resets all results - the cursor object has no reference to its original connection object
        cursor.close()
        # Return the row count of the variable "row_affected"
        return row_affected.rowcount
    # If it fails to update record(s) by name, print a message to notify the user and exit the program
    except sqlite3.OperationalError as error:
        print(f"Fail to update record(s) by name in the {table_name}. [{error.sqlite_errorcode} - {error.sqlite_errorname}]\n")
        exit() 
#
# End: update_record
# -------------------------------------------------------------------------------------------------------------- #
# Start: delete_record
#  
# Create a function "delete_record" with the parameters "db" and "value_list" to delete the record by id
def delete_record(db, value_list):
    # Set a variable "row_affected" to -1 and store the row(s) affected later
    row_affected = -1
    # Use try and catch block to delete record(s) by name
    try:
        # Set a variable "sql_statement" to store the SQL statement for deleting record(s) by id
        sql_statement = f"DELETE FROM {table_name} WHERE id = ?"
        # Set a tuple "value_tuple" to store the list "value_list" after conversion of data type
        value_tuple = tuple(value_list)
        # Set a "cursor" object
        cursor = db.cursor()  
        # Set the variable "row_affected" to store the row(s) affected after executed SQL statement        
        row_affected = cursor.execute(sql_statement, value_tuple)
        # Commit the transaction
        db.commit()
        # Resets all results - the cursor object has no reference to its original connection object
        cursor.close()
        # Return the row count of the variable "row_affected"
        return row_affected.rowcount
    # If it fails to delete record(s) by name, print a message to notify the user and exit the program
    except sqlite3.OperationalError as error:
        print(f"Fail to delete record(s) by name in the {table_name}. [{error.sqlite_errorcode} - {error.sqlite_errorname}]\n")
        exit()
#
# End: delete_record
# -------------------------------------------------------------------------------------------------------------- #
# Start: print_records
#     
# Create a function "print_records" with the parameters "record_list" and "field_list" to print the recordsets
# by using the tabulet library
def print_records(record_list, field_list):
    # Print the records with the parameters "record_list" and "field_list" in the "psql" format
    print(tabulate(record_list, field_list, tablefmt='psql', showindex=False))    
#
# End: print_records
# -------------------------------------------------------------------------------------------------------------- #
# Main functions
# -------------------------------------------------------------------------------------------------------------- #
# Start: enter_book
#
# Create a function "enter_book" to add a new book
def enter_book():
    # Set a variable "new_title" to empty
    new_title = ""
    # Set a variable "new_author" to empty
    new_author = ""
    # Set a variable "new_quantity" to empty
    new_quantity = ""
    # Set a variable "is_confirmed" to empty
    is_confirmed = ""
    # Set a variable "enter_book_again" to empty
    enter_book_again = ""
    # Set a variable "is_added" to false
    is_added = False
    # Use the while-loop function to execute the following if/else statements as the condition is true
    while True:
        # If the variable "new_title" is empty, ask the user to input the new_title of the book
        if new_title == "":
            new_title = input(f"Please enter the {colored_text('blue', 'TITLE')} of the book: ").strip()
            # If the variable "new_title" is blank, print the message to notify the user for entering the title of the book
            if new_title == "":
                print(f"\n{colored_text('red', 'The title of the book should not be blank. Please try again.')}\n")
        # If the variable "new_title" is not empty, execute the following the statements
        else:
            # If the variable "new_author" is empty, ask the user to input the author of the book
            if new_author == "":
                new_author = input(f"Please enter the {colored_text('green', 'AUTHOR')} of the book: ").strip()
                # If the variable "new_author" is blank, print the message to notify the user for entering the author of the book 
                if new_author == "":
                    print(f"\n{colored_text('red', 'The author of the book should not be blank. Please try again.')}\n")
            # If the variable "new_author" is not empty, execute the following the statements
            else:
                # If the variable "quannew_quantityity" is empty, ask the user to input the quantity of the book
                if new_quantity == "":
                    new_quantity = input(f"Please enter the {colored_text('red', 'QUANTITY')} of the book: ").strip()
                    # If the variable "quantity" is blank, print the message to notify the user for entering the quantity of the book 
                    if new_quantity == "":
                        print(f"\n{colored_text('red', 'The quantity of the book should not be BLANK. Please try again.')}\n") 
                # If the variable "quantity" is not empty, execute the following the statements
                else:
                    # If the variable "quantity" is not numeric, print the message to the user for entering again
                    # if not new_quantity.isdigit():
                    if check_positive_string_number(new_quantity) == -1:                        
                        print(f"\n{colored_text('red', 'The quantity of the book is not an integer. Please try again.')}\n") 
                        # Set the variable "quantity" to empty
                        new_quantity = ""
                    elif check_positive_string_number(new_quantity) == 0:
                        print(f"\n{colored_text('red', 'The quantity of the book is not a positive integer. Please try again.')}\n")    
                        new_quantity = ""
                    # If the variable "quantity" is numeric, execute the following the statements
                    else:
                        # If the variable "is_confirmed" is empty, ask the user to confirm the book for addition
                        if is_confirmed == "":                        
                            is_confirmed = input(f"\nDo you {colored_text('cyan', 'CONFIRM')} to add this book? [Enter {colored_text('blue', '1 - YES')}, {colored_text('green', '2 - NO')}, press {colored_text('bold', 'Enter - EXIT')}]: ").strip()
                            # If the variable "is_confirmed" is empty, use "break" to exit the while-loop
                            if is_confirmed == "":
                                break
                        # If the variable "is_confirmed" is not empty, execute the following the statements
                        else:
                            # If the variable "is_confirmed" is "1", add the new book accordingly                
                            if is_confirmed == "1":
                                # If the variable "is_added" is true, set the variable "new_id" to the new id of the new book
                                # by calling the function of the generate_new_id with the parameter "db"
                                if not is_added:
                                    new_id = generate_new_id(db)
                                    # If the variable "new_id" is not empty, add the new book to the table 
                                    if new_id:
                                        # Set a list "enter_book_list" to store the elements of the attributes of the new book
                                        # i.e. new_id, title, author and quantity
                                        enter_book_list = [[int(new_id), new_title, new_author, int(new_quantity)]]
                                        # Set the variable "row_affected" to store the number of books added to the table
                                        # by calling the function "insert_record" with the parameters "db" and "enter_book_list"
                                        row_affected = insert_record(db, enter_book_list)
                                        # print the message to notify the user for adding the book successfully
                                        print(f"\n{colored_text('cyan', f'{new_title} - {row_affected} book(s) added successfully!')}\n")
                                        # Set a list "all_books" to store all the books records in the table 
                                        # by calling the function "select_all_records" with the parameter "db"
                                        all_books = select_all_records(db)
                                        # If the variable "all_books" is not empty, print the detail of all books
                                        if all_books:
                                            # Call the function "print_records" with the parameters "all_books" and "field_list" 
                                            # to print the rows to be found.
                                            print_records(all_books, field_list)
                                        # Set the variable "is_added" to true after adding the new book(s)
                                        is_added = True                                    
                            # If the variable "is_confirmed" is "2", print the message to notify the user for entering the detail 
                            # of another book
                            elif is_confirmed == "2":
                                print(f"\n{colored_text('cyan', 'Please enter the detail of another book.')}\n")
                                # Set the variable "new_title" to empty
                                new_title = ""
                                # Set the variable "new_author" to empty
                                new_author = ""
                                # Set the variable "new_quantity" to empty
                                new_quantity = ""
                                # Set the variable "is_confirmed" to empty
                                is_confirmed = ""
                                # Set the variable "is_added" to false
                                is_added = False
                            # If any other case, print the message to notify the user that entered the invalid option for a new book
                            else:
                                print(f"\n{colored_text('red', 'You enter the invalid option for entering book.')}\n")
                                # Set the variable "is_confirmed" to empty
                                is_confirmed = ""
                            # If the variable "is_added" is true, ask the user to enter another book
                            if is_added:
                                # If the variable "enter_book_again" is empty, ask the user to enter another book
                                if enter_book_again == "":
                                    enter_book_again = input(f"\nDo you need to enter {colored_text('cyan','ANOTHER')} book? [Enter {colored_text('blue', '1 - YES')}, {colored_text('green', '2 - NO')}, press {colored_text('bold', 'Enter - EXIT')}]: ").strip()
                                    # Set the variable "enter_book_again" to empty, and use "break" to exit the while-loop
                                    if enter_book_again == "":
                                        break
                                    
                                # If the variable "enter_book_again" is not empty, execute the following if/else statements
                                else:
                                    # If the variable "enter_book_again" is "1", set the variables "new_title", "new_author", "new_quantity", "is_confirmed",
                                    # "enter_book_again" are empty and "is_added" to false
                                    if enter_book_again == "1":
                                        new_title = ""
                                        new_author = ""
                                        new_quantity = ""
                                        is_confirmed = ""
                                        enter_book_again = ""
                                        is_added = False
                                    # If the variable "enter_book_again" is "2", use "break" to exit the while-loop
                                    elif enter_book_again == "2": 
                                        break
                                    # If any other cases, print the message to notify the user of the invalid option for a new book
                                    else:
                                        print(f"\n{colored_text('red', 'You enter the invalid option for entering another book. Please try again.')}\n")
                                        # Set the variable "enter_book_again" to empty
                                        enter_book_again = ""
                                        # Set the variable "is_added" to true
                                        is_added = True                                                      
#
# End: enter_book
# -------------------------------------------------------------------------------------------------------------- #
# Start: upate_book
#  
# Create a function "update_book" to update the detail of the book
def update_book():
    # Set the variable "update_id" to empty
    update_id = ""
    # Set the variable "update_title" to empty
    update_title = ""
    # Set the variable "update_author" to empty
    update_author = ""
    # Set the variable "update_quantity" to empty
    update_quantity = ""
    # Set the variable "update_again" to empty
    update_again = ""
    # Set the variable "is_confirmed" to empty
    is_confirmed = ""
    # Set the variable "is_updated" to false
    is_updated = False
    # Use the while-loop function to execute the following if/else statements as the condition is true
    while True:
        # If the variable "update_id" to empty, print the detail of all books
        if update_id == "":
            # Set a list "all_books" to store all the books records in the table 
            # by calling the function "select_all_records" with the parameter "db"
            all_books = select_all_records(db)
            # If the variable "all_books" is not empty, print the detail of all books
            if all_books:
                # Call the function "print_records" with the parameters "all_books" and "field_list" 
                # to print the rows to be found.
                print_records(all_books, field_list)
                # Set the variable "update_id" to store the id of the book the user entered
                update_id = input(f"\nPlease enter the {colored_text('cyan', 'ID')} of the book for {colored_text('cyan', 'UPDATE')} - [press {colored_text('bold', 'Enter - EXIT')} ]  ").strip()
                # Print a new line
                print(f"\n")
                # If the variable "update_id" is empty, use "break" to exit the while-loop
                if update_id == "":
                    break   
            # If the variable "all_books" is empty, print the message to notify the user that no book(s) found 
            # and use "break" to exit the while-loop
            else:
                print(f"{colored_text('cyan', 'No books are found in our records.')}\n")
                break
        # If the variable "update_id" to not empty, execute the following if/else statements
        else:
            # If the variable "update_id" is numeric, find the detail of the book by the variable "update_id" 
            # in the variable "all_books" 
            if update_id.isdigit():
                # If the id of the book (index 0) in the variable "all_books" is matched with the variable "update_id", 
                # set the variable "book" to store the record of the book
                book = [book for book in all_books if book[0] == int(update_id)]
                # If the variable "book" is not empty, destructure the elements and store them in the variables 
                # "id", "title", "author" and "quantity" 
                if book:
                    id, title, author, quantity = book[0]
                    # If the variable "update_title" is empty, ask the user to enter the title of the book
                    if update_title == "":
                        update_title = input(f"Please enter the {colored_text('cyan', 'TTILE')} of the book (current: {colored_text('cyan', f'{title}')}) - [press {colored_text('bold', 'ENTER - NO CHANGE')}]  ").strip()
                        # If the variable "update_title" is not empty, set the variable "update_title" to the title the user entered,
                        # otherwise set it to the variable "title"
                        update_title = update_title if update_title else title                        
                    # If the variable "update_author" is empty, ask the user to enter the author of the book 
                    if update_author == "":
                        update_author = input(f"Please enter the {colored_text('cyan', 'AUTHOR')} of the book (current: {colored_text('cyan', f'{author}')}) - [press {colored_text('bold', 'ENTER - NO CHANGE')}]  ").strip()
                        # If the variable "update_author" is not empty, set the variable "update_author" to the author the user entered,
                        # otherwise set it to the variable "author"
                        update_author = update_author if update_author else author
                    # If the variable "update_quantity" is empty, ask the user to enter the quantity of the book 
                    if update_quantity == "":
                        update_quantity = input(f"Please enter the {colored_text('cyan', 'QUANTITY')} of the book (current: {colored_text('cyan', f'{quantity}')}) - [press {colored_text('bold', 'ENTER - NO CHANGE')}]  ").strip()
                        # If the variable "update_quantity" is numeric, set the variable "update_quantity" to the quantity the user entered
                        if update_quantity.isdigit():
                            update_quantity = update_quantity
                        # If the variable "update_quantity" is empty, set the variable "update_quantity" to the variable "quantity"
                        elif update_quantity == "":
                            update_quantity = quantity
                        # If any other cases, print the message to notify the user that the invalid quantity of the book entered
                        else:
                            print(f"\n{colored_text('red', f'You enter the invalid quantity of the book. Please try again.')}\n")
                            # Set the variable "update_quantity" to empty
                            update_quantity = ""
                    # If the variable "update_quantity" is not empty, ask the user to confirm the updating the book 
                    else:
                        # If the variable "is_confirmed" is empty, ask the user to confirm the update the book
                        if is_confirmed == "":
                            is_confirmed = input(f"\nDo you {colored_text('cyan', 'CONFIRM')} to update this book? - [Enter {colored_text('blue', '1 - YES')}, {colored_text('green', '2 - NO')}, press {colored_text('bold', 'Enter - EXIT')}]: ").strip()
                            # If the variable "is_confirmed" is empty, use "break" to exit the while loop
                            if is_confirmed == "":
                                break
                        # If the variable "is_confirmed" is not empty, execute the following if/else statements
                        else:
                            # If the variable "is_confirmed" is "1", compare the current detail of the book with the updated detail of the book 
                            # that the user entered 
                            if is_confirmed == "1":
                                # If the current detail of the book is the same as the updated detail of the book, 
                                # print the message to the user for no change of the book.                                
                                if [title, author, quantity] == [update_title, update_author, update_quantity]:
                                    print(f"\n{colored_text('cyan', 'There is no change on the book.')}\n") 
                                # If the current detail of the book is not the same as the updated detail of the book,
                                # update the title / author / quantity of the book accordingly
                                else:
                                    # If the variable "is_updated" is true, print the changes in the book
                                    if not is_updated: 
                                        # Print the header of the changes in the book
                                        print(f"\n{colored_text('bold', 'The change(s) is/are as follows:')}")
                                        # If the variable "title" is not equal to the variable "update_title", 
                                        # print the change of the title of the book to the user
                                        if title != update_title: 
                                            print(f"  {colored_text('bold', 'TITLE')}:\t{title} -> {colored_text('cyan', update_title)}") 
                                        # If the variable "author" is not equal to the variable "update_author", 
                                        # print the change of the author of the book to the user
                                        if author != update_author: 
                                            print(f"  {colored_text('bold', 'AUTHOR')}:\t{author} -> {colored_text('cyan', update_author)}")
                                        # If the variable "quantity" is not equal to the variable "update_quantity", 
                                        # print the change of the quantity of the book to the user   
                                        if quantity != update_quantity: 
                                            print(f"  {colored_text('bold', 'QUANTITY')}:\t{quantity} -> {colored_text('cyan', update_quantity)}") 
                                        # Set a list "update_book_list" to store the variables "update_title", "update_author", "update_quantity" and
                                        # "update_id"                                        
                                        update_book_list = [update_title, update_author, int(update_quantity), int(update_id)]
                                        # Set the variable "row_affected" to store the number of the books updated in the table
                                        # by calling the function "update_record" with the parameters "db" and "update_book_list"
                                        row_affected = update_record(db, update_book_list)
                                        # print the message to notify the user for updating the book successfully
                                        print(f"\n{colored_text('cyan', f'{row_affected} book(s) updated successfully.')}\n")
                                    
                                # If the variable "update_again" is empty, ask the user whether enter another book or not
                                if update_again == "":
                                    update_again = input(f"\nDo you {colored_text('cyan', 'UPDATE')} another book? - [Enter {colored_text('blue', '1 - YES')}, {colored_text('green', '2 - NO')}, press {colored_text('bold', 'Enter - EXIT')}]:  ").strip()
                                    # If the variable "update_again" is empty, use "break" to exit the while-loop
                                    if update_again == "":
                                        break
                            # If the variable "is_confirmed" is "2", ask the user whether enter another book or not
                            elif is_confirmed == "2":
                                # If the variable "update_again" is empty, ask the user whether enter another book or not
                                if update_again == "":
                                    update_again = input(f"\nDo you update {colored_text('cyan', 'ANOTHER')} book? - [Enter {colored_text('blue', '1 - YES')}, {colored_text('green', '2 - NO')}, press {colored_text('bold', 'Enter - EXIT')}]:  ").strip()
                                    # If the variable "update_again" is empty, use "break" to exit the while-loop
                                    if update_again == "":
                                        break                                

                            elif is_confirmed == "":
                                break
                            # If any other cases, print the message to notify the user that the invalid option for confirming the updated book
                            else:
                                print(f"\n{colored_text('red', 'You enter the invalid option to confirm the updated book. Please try again.')}\n")
                                # Set the variable "is_confirmed" to empty
                                is_confirmed = "" 
                            # If the variable "is_confirmed" is "1" or "2", execute the following if/else statements
                            if is_confirmed == "1" or is_confirmed == "2":
                                # If the variable "udpate_again" is "1", set the variables "update_id", "update_title", "update_author", 
                                # "update_quantity", "is_confirmed", "update_again" to empty and "is_updated" to true
                                if update_again == "1":
                                    update_id = ""
                                    update_title = ""
                                    update_author = ""
                                    update_quantity = ""
                                    is_confirmed = ""
                                    update_again = ""
                                    is_updated = True
                                # If the variable "update_again" is "2" or empty, use "break" to exit the while-loop
                                elif update_again == "2" or update_again == "":
                                    print(f"\n")
                                    break
                                # If any other case, print the message to notify the user that the invalid option for updating another book
                                else:
                                    print(f"\n{colored_text('red', 'You enter the invalid option for updating another book. Please try again.')}\n")
                                    # Set the variable "update_again" to empty, "is_updated" to true
                                    update_again = ""
                                    is_updated = True                                
                                
                # If the variable "book" is not found in the variable "all_books", print the message to notify the user 
                # for the incorrect id of the book entered
                else:
                    print(f"\n{colored_text('red', 'You enter the incorrect id of the book. Please try again.')}\n")
                    # Set the variable "update_id" to empty
                    update_id = ""
            # If any other cases, print the message to notify the user of the invalid id 
            else:
                print(f"\n{colored_text('red', 'You enter the invalid id of the book. Please try again.')}\n")
                # Set the variable "update_id" to empty
                update_id = ""
#
# End: update_book 
# -------------------------------------------------------------------------------------------------------------- #
# Start: delete_book
#                  
# Create a function "delete_book" to delete the book
def delete_book():    
    # Set the variable "delete_id" to empty
    delete_id = ""
    # Set the variable "delete_again" to empty
    delete_again = ""
    # Set the variable "is_confirmed" to empty
    is_confirmed = ""
    # Use the while-loop function to execute the following if/else statements as the condition is true
    while True:
        # If the variable "delete_id" is empty, print the detail of all books
        if delete_id == "":
            # Set a list "all_books" to store all the books records in the table 
            # by calling the function "select_all_records" with the parameter "db"
            all_books = select_all_records(db)
            # If the variable "all_books" is not empty, print the detail of all books
            if all_books:
                # Call the function "print_records" with the parameters "all_books" and "field_list" 
                # to print the rows to be found.
                print_records(all_books, field_list)
                # Set the variable "delete_id" to store the id of the book the user entered
                delete_id = input(f"\nPlease enter the {colored_text('cyan', 'ID')} of the book for {colored_text('cyan', 'DELETION')} - [press {colored_text('bold', 'ENTER - EXIT')}]  ").strip()
                # If the variable "delete_id" is empty, use "break" to exit the while-loop
                if delete_id == "":
                    break
            # If the variable "all_books" is empty, print the message to notify the user that no book(s) found 
            # and use "break" to exit the while-loop
            else:
                print(f"{colored_text('cyan', 'No books are found in our records.')}\n")
                break
        # If the variable "delete_id" is not empty, execute the following if/else statements
        else:
            # If the variable "delete_id" is numeric, find the book record by the variable "delete_id" 
            # in the variable "all_books"
            if delete_id.isdigit():
                book = [book for book in all_books if book[0] == int(delete_id)]
                # If the variable "book" is not empty, ask the user to confirm the deleted book
                if book:
                    # If the variable "is_confirmed" is empty, ask the user the confirm the deleted book
                    if is_confirmed == "":
                        is_confirmed = input(f"\nDo you confirm to {colored_text('cyan', 'DELETE')} this book? - [Enter {colored_text('blue', '1 - YES')}, {colored_text('green', '2 - NO')}, press {colored_text('bold', 'Enter - EXIT')}]: ").strip()
                        # If the variable "is_confirmed" is empty, use "break" to exit the while-loop
                        if is_confirmed == "":
                            break
                    # If the variable "is_confirmed" is not empty, execute the following if/else statements
                    else:
                        # If the variable "is_confirmed" is "1", delete the book by the variable "delete_id"
                        if is_confirmed == "1":                            
                            # Set a list "delete_book_list" to store the variable "delete_id"
                            delete_book_list = [delete_id]
                            # Set the variable "row_affected" to store the number of the books deleted into the table
                            # by calling the function "delete_record" with the parameters "db" and "delete_book_list"
                            row_affected = delete_record(db, delete_book_list)
                            # If the variable "row_affected" is not empty, print the number of book(s) deleted successfully
                            if row_affected:
                                # print the message to notify the user for updating the book successfully
                                print(f"\n{colored_text('cyan', f'{row_affected} book(s) deleted successfully.')}\n")
                                # is_confirmed = ""
                            # If the variable "delete_again" is empty, ask the user to delete another book or not
                            if delete_again == "":
                                # Set the variable "delete_again" to store the user's option for deleting another book
                                delete_again = input(f"\nDo you {colored_text('cyan', 'DELETE')} another book? - [Enter {colored_text('blue', '1 - YES')}, {colored_text('green', '2 - NO')}, press {colored_text('bold', 'Enter - EXIT')}]: ").strip()
                                # If the variable "delete_again" is empty, use "break" to exit while-loop
                                if delete_again == "":
                                    break
                            else:
                                # If the variable "delete_again" is "1", set the variables "delete_id", "is_confirmed" and "delete_again"
                                if delete_again == "1":
                                    delete_id = ""
                                    is_confirmed = ""
                                    delete_again = ""                                    
                                # If the variable "delete_again is "2" or empty, use "break" to exit the while-loop
                                elif delete_again == "2" or delete_again == "":
                                    break
                                # If any other cases, print the message to notify the user that the invalid option for deleting another book
                                else:
                                    print(f"\n{colored_text('red', 'You enter the invalid option for deleting another book. Please try again.')}\n")
                                    # Set the variable "delete_again" to empty
                                    delete_again = ""
                        # If the variable "is_confirmed" is "2", set the variable "delete_id" to empty
                        elif is_confirmed == "2":
                            delete_id = "" 
                            is_confirmed = ""
                        # If any other cases, print the message to notify the user that the invalid option for confirmation
                        else:
                            print(f"\n{colored_text('red', 'You enter the invalid option for confirmation. Please try again.')}\n")
                            # Set the variable "is_confirmed" to empty
                            is_confirmed = ""
                # If the variable "delete_id" is not found in the variable "all_book", print the message to notify the user that
                # the incorrect id of the book entered
                else:
                    print(f"\n{colored_text('red', 'You enter the incorrect id of the book.')}\n")
                    # Set the variable "delete_id" to empty
                    delete_id = ""
            # If any other cases, print the message to notify the user that the invalid id of the book entered 
            else:
                print(f"\n{colored_text('red', 'You enter the invalid id of the book.')}\n")
                # Set the variable "delete_id" to empty
                delete_id = ""
#
# End: delete_id
# -------------------------------------------------------------------------------------------------------------- #
# Start: search_book
#  
# Create a function "search_book" to search the book 
def search_book():
    # Set the variable "search_option" to empty
    search_option = ""
    # Set the variable "search_id" to empty
    search_id = ""
    # Set the variable "search_title" to empty
    search_title = ""
    # Set the variable "search_author" to empty
    search_author = ""
    # Set the variable "search_minimum_quantity" to empty
    search_minimum_quantity = ""
    # Set the variable "search_maximum_quantity" to empty
    search_maximum_quantity = ""
    # Set the variable "search_again" to empty    
    search_again = "" 
    # Set the variable "is_searched" to false (i.e. complete of searching books)
    is_searched = False
    # Use the while-loop function to execute the following if/else statements as the condition is true 
    while True:        
        # If the variable "search_option" to empty, ask the user the enter the search option
        if search_option == "":
            # Set the variable "search_option" to empty, and ask the user the enter the search option
            search_option = input(f"Please enter your {colored_text('cyan', 'SEARCH')} option - [Enter {colored_text('blue', '1 - ID')}, {colored_text('green', '2 - TITLE')}, {colored_text('yellow', '3 - AUTHOR')}, {colored_text('red', '4 - quantity')}, press {colored_text('bold', 'ENTER - EXIT')}]  ").strip()
            # Print a new line
            print("\n")
            # If the variable "search_option" is empty, use "break" to exit the while-loop
            if search_option == "":
                break
        # If the variable "search_option" is not empty, execute the following if/else statements
        else:            
            # If the variable "search_option" is numeric, execute the following if/else statements
            if search_option.isdigit():
                
# ************************************************************************************************************** #
#   Search Option 1: Search by ID - It is an exact match search            
#
                # If the variable "search_optiom" is "1" ask the user the enter the id of the book
                if search_option == "1":
                    # If the variable "search_id" is empty, ask the user to enter the title of the book
                    if search_id == "":
                        print(f"{colored_text('bold', 'Note: It is an exact match. The id of the book must be matched with that in our record.')}\n")
                        search_id = input(f"\nPlease enter the {colored_text('cyan', 'ID')} of the book - [press {colored_text('bold', 'ENTER - EXIT')}]  ").strip()
                        # If the variable "search_id" is empty, use "break" to exit the while-lop
                        if search_id == "":
                            break
                        # If the variable "is_searched" is true, print the search results of the books
                        if not is_searched:
                            # Set a variable "search_id_list" to store the concatenated variable "search_id"
                            search_id_list = [f"{search_id}"]
                            # Set a list "search_book_list" to store the book by calling the function "select_record_by_search_option"
                            # with the parameter "db", "search_id_list" and "search_option"
                            search_book = select_record_by_search_option(db, search_id_list, int(search_option))
                            # If the variable "search_book" is not empty, print the search results to the user
                            if search_book:
                                # Print the number of books found
                                print(f"\n{colored_text('cyan', f'{len(search_book)} book(s) found.')}\n")
                                # Call the function "print_records" with the parameters "search_book" and "field_list" 
                                # to print the rows to be found.
                                print_records(search_book, field_list)                               
                            # If the variable "search_book" is empty, print the message to notify the user that
                            # No books are found
                            else:
                                print(f"\n{colored_text('cyan','No books are found.')}\n")  
                            # Set the variable "is_searched" to true after searching the book
                            is_searched = True
#                            
#                            
# ************************************************************************************************************** #
#  Search Option 2: Search by TITLE - It is a wildcard search
#             
                # If the variable "search_option" is "2", ask the user to enter the title of the book
                elif search_option == "2":
                    # If the variable "search_title" is empty, ask the user to enter the title of the book
                    if search_title == "":
                        print(f"{colored_text('bold', 'Note: It is a wildcard search. One or more characters of the title of the book are matched with that in our record.')}\n")
                        search_title = input(f"Please enter the {colored_text('cyan', 'TITLE')} of the book - [press {colored_text('bold', 'ENTER - EXIT')}]  ").strip()
                        # Print a new line
                        print(f"\n")
                        # If the variable "search_title" is empty, use "break" to exit the while-lop
                        if search_title == "":
                            break
                        # If the variable "is_searched" is true, print the search results of the books
                        if not is_searched:
                            # Set a variable "search_title_list" to store the concatenated variable "search_title"
                            search_title_list = [f"%{search_title}%"]
                            # Set a list "search_book_list" to store the book by calling the function "select_record_by_search_option"
                            # with the parameter "db", "search_title_list" and "search_option"
                            search_book = select_record_by_search_option(db, search_title_list, int(search_option))
                            # If the variable "search_book" is not empty, print the search results to the user
                            if search_book:
                                # Print the number of books found
                                print(f"\n{colored_text('cyan', f'{len(search_book)} book(s) found.')}\n")
                                # Call the function "print_records" with the parameters "search_book" and "field_list" 
                                # to print the rows to be found.
                                print_records(search_book, field_list)                                
                            # If the variable "search_book" is empty, print the message to notify the user that
                            # No books are found
                            else:
                                print(f"\n{colored_text('cyan','No books are found.')}\n") 
                            # Set the variable "is_searched" to true after searching the book   
                            is_searched = True           
#                            
#                            
# ************************************************************************************************************** #
#  Search Option 3: Search by AUTHOR - It is a wildcard search
#                                   
                # If the variable "search_option" is "3", ask the user to enter the author of the book          
                elif search_option == "3":
                    # If the variable "search_author" is empty, ask the user to enter the author of the book
                    if search_author == "":
                        print(f"{colored_text('bold', 'Note: It is a wildcard search. One or more characters of the author of the book are matched with that in our record.')}\n")
                        search_author = input(f"Please enter the {colored_text('cyan', 'AUTHOR')} of the book - [press {colored_text('bold', 'ENTER - EXIT')}]  ").strip()
                        # If the variable "search_author" is empty, use "break" to exit the while-lop
                        if search_author == "":
                            break                       
                        # If the variable "is_searched" is true, print the search results of the books
                        if not is_searched:
                             # Set a variable "search_author_list" to store the concatenated variable "search_author"
                            search_author_list = [f"%{search_author}%"]
                            # Set a list "search_author_list" search_author_list" and "search_option"
                            search_book = select_record_by_search_option(db, search_author_list, int(search_option))
                            # If the variable "search_book" is not empty, print the search results to the user
                            if search_book:
                                # Print the number of books found
                                print(f"\n{colored_text('cyan', f'{len(search_book)} book(s) found.')}\n")
                                # Call the function "print_records" with the parameters "search_book" and "field_list" 
                                # to print the rows to be found.
                                print_records(search_book, field_list)

                            # If the variable "search_book" is empty, print the message to notify the user that
                            # No books are found
                            else:
                                print(f"\n{colored_text('cyan','No books are found.')}\n")
                            # Set the variable "is_searched" to true after searching the book 
                            is_searched = True                            
#                            
#                            
# ************************************************************************************************************** #
#  Search Option 4: Search by QUANTITY - It is a range search
#                                   
                # If the variable "search_option" is "4" ask the user the enter the quantity range of the book
                elif search_option == "4":
                    # If the variable "search_minimum_quantity" is empty, ask the user to enter the minimum quantity of the books
                    if search_minimum_quantity == "":
                        # Print the message to notify the user about the search type
                        print(f"{colored_text('bold', 'Note: This is a range search. The minimum quantity and maximum quantity of the book(s) are required.')}\n")
                        # Set the variable "search_minimum_quantity" to store the minimum quantity of the books the user entered
                        search_minimum_quantity = input(f"\nPlease enter the {colored_text('cyan', 'MINIMUM')} quantity of the book - [press {colored_text('bold', 'ENTER - EXIT')}]  ").strip()
                        # If the variable "search_minimum_quantity" is empty, use "break" to exit the while-loop function
                        if search_minimum_quantity == "":
                            break
                    # If the variable "search_minimum_quantity" is not empty, validate the minimum quantity of the book the user entered
                    else:
                        # If the minimum quantity of the book is -1, print the message to notify the user that it is not an integer
                        # Call the function "check_positive_string_number" with the parameter "search_minimum_quantity" for validation
                        # Set the variable "search_minimum_quantity" to empty
                        if check_positive_string_number(search_minimum_quantity) == -1:
                            print(f"\n{colored_text('red', 'You enter the minimum quantity of the book(s) is not an integer. Please try again.')}\n")
                            search_minimum_quantity = ""
                        # If the minimum quantity of the book is 0, print the message to notify the user that it is not a positive integer
                        # Call the function "check_positive_string_number" with the parameter "search_minimum_quantity" for validation
                        # Set the variable "search_minimum_quantity" to empty
                        elif check_positive_string_number(search_minimum_quantity) == 0:
                            print(f"\n{colored_text('red', 'You enter the minimum quantity of the book(s) is not a positive integer. Please try again.')}\n")
                            search_minimum_quantity = ""
                        # If any other cases, ask the user to enter the maximum quantity of the books
                        else:
                            # If the variable "search_maximum_quantity" is empty, ask the user to enter the maximum quantity of the books
                            if search_maximum_quantity == "":
                                # Set the variable "search_maximum_quantity" to store the maximum quantity of the books the user entered
                                search_maximum_quantity = input(f"\nPlease enter the {colored_text('cyan', 'MAXIMUM')} quantity of the book - [press {colored_text('bold', 'ENTER - EXIT')}]  ").strip()
                                # If the variable "search_maximum_quantity" is empty, use "break" to exit the while-loop function
                                if search_maximum_quantity == "":
                                    break
                            # If the variable "search_maximum_quantity" is not empty, validate the maximum quantity of the book the user entered    
                            else:
                                # If the maximum quantity of the book is -1, print the message to notify the user that it is not an integer.
                                # Call the function "check_positive_string_number" with the parameter "search_maximum_quantity" for validation
                                # Set the variable "search_maximum_quantity" to empty
                                if check_positive_string_number(search_maximum_quantity) == -1:
                                    # Print the message to notify the user about the search type
                                    print(f"\n{colored_text('red', 'You enter the maximum quantity of the book(s) is not an integer. Please try again.')}\n")
                                    search_maximum_quantity = ""
                                # If the maximum quantity of the book is 0, print the message to notify the user that it is not a positive integer.
                                # Call the function "check_positive_string_number" with the parameter "search_maximum_quantity" for validation
                                # Set the variable "search_maximum_quantity" to empty
                                elif check_positive_string_number(search_maximum_quantity) == 0:
                                    print(f"\n{colored_text('red', 'You enter the maximum quantity of the book(s) is not a positive integer. Please try again.')}\n")
                                    search_maximum_quantity = ""
                                # If any other cases, compare the values of the minimum quantity and maximum quantity of the books the user entered
                                else:
                                    # If the variable "search_minimum_quantity" is greater than the variable "search_minimum_quantity", 
                                    # print the message to notify the user that the minimum number should be less than the maximum number                                    
                                    if int(search_minimum_quantity) > int(search_maximum_quantity):
                                        print(f"{colored_text('red', 'The maximum quantity of the book(s) is greater than the maximum quantity of the book(s).')}\n")
                                        # Set the variable "search_minimum_quantity" to empty
                                        search_minimum_quantity = ""
                                        # Set the variable "search_maximum_quantity" to empty
                                        search_maximum_quantity = ""
                                    # If the variable "search_minimum_quantity" is not greater than the variable "search_minimum_quantity", 
                                    # search the books by the minimum quantity and maximum quantity of the books  
                                    else:
                                        # If the variable "is_searched" is true, print the search results of the books
                                        if not is_searched:
                                            # Set the list "quantity_range_list" to store the variable "search_minimum_quantity" and "search_maximum_quantity" 
                                            quantity_range_list = [int(search_minimum_quantity), int(search_maximum_quantity)]
                                            # Set a list "search_book_list" to store the book by calling the function "select_record_by_search_option"
                                            # with the parameter "db", "search_id_list" and "search_option"                                            #
                                            search_book = select_record_by_search_option(db, quantity_range_list, int(search_option))
                                            # If the variable "search_book" is not empty, print the search results to the user                        
                                            if search_book:
                                                # Print the number of books found
                                                print(f"\n{colored_text('cyan', f'{len(search_book)} book(s) found.')}\n")
                                                # Call the function "print_records" with the parameters "search_book" and "field_list" 
                                                # to print the rows to be found.
                                                print_records(search_book, field_list)
                                            # If the variable "search_book" is empty, print the search results to the user
                                            else:
                                                print(f"\n{colored_text('cyan','No books are found.')}\n")       
                                            # Set the variable "is_searched" to true after searching the book
                                            is_searched = True
                # If the variable "search_option" is not "1", 2", "3" or "4", set the variable "search_option" to empty
                else:
                    print(f"\n{colored_text('red', 'You enter the invalid search option [Enter 1 / 2 / 3 / 4]. Please try again.')}\n")
                    # Set the variable "search_option" to empty
                    search_option = ""
                # If the variable "variable" is true, ask the user to search for other books or not
                if is_searched:
                # # If the variable "search_option" is "2" "3" or "4", ask the user to search again or not
                # if search_option == "1" or search_option == "2" or search_option == "3" or search_option == "4" :
                    # If the variable "search_again" is empty, ask the user to enter the option for searching for another book
                    if search_again == "": 
                        search_again = input(f"\nDo you search {colored_text('cyan', 'ANOTHER')} book? - [Enter {colored_text('blue', '1 - YES')}, {colored_text('green', '2 - NO')}, press {colored_text('bold', 'Enter - EXIT')}]: ").strip()
                        # Print a new line
                        print("\n") 
                        # If the variable "search_again" is empty, use "break" to exit while-loop
                        if search_again == "":
                            break
                    # If the variable "search_again" is not empty, execute the following if/else statements
                    else:
                        # If the variable "search_again" is "1", set the variables "search_option", "search_title" and "search_author", "search_again", 
                        # "search_minimum_quantity",  "search_maximum_quantity" to empty
                        # # Set the variable "is_searched" to false (initialised)
                        if search_again == "1":
                            search_option = ""
                            search_id = ""
                            search_title = ""
                            search_author = ""
                            search_minimum_quantity = ""
                            search_maximum_quantity = ""
                            search_again = ""                            
                            is_searched = False                            
                        # If the variable "search_again" is "2" or empty, use "break" to exit the while-loop
                        elif search_again == "2" or search_again == "":
                            break
                        # If any other cases, print the message to notify the user that the invalid option for searching again
                        else:
                            print(f"\n{colored_text('red', 'You enter the invalid search again option. Please try again.')}\n")
                            # Set the variable "search_again" to empty
                            search_again = ""               

            # If any other cases, print the message to notify the user that the invalid search option
            else:
                print(f"\n{colored_text('red', 'You enter the invalid search option. Please try again.')}\n")
                # Set the variable "search_option"
                search_option = ""
#
# End: search_book 
# -------------------------------------------------------------------------------------------------------------- #
# Start: bookstore -> create connection
#  
# Set the object "db" to create a connection by calling the function "create_connection" with the parameter "db_file"
db = create_connection(db_file)
# If the object "db" is empty, print the message to the user for failing to create a connection and 
# exit the program
if not db:
    print(f"Fail to create connection. ")
    exit()
#
# End: bookstore -> create connection
# -------------------------------------------------------------------------------------------------------------- #
# Start: bookstore -> initialise the table "books"
#  
# Reset the setting of the database "ebookstore"
# If the object "db" is not None, execute the following SQL statements
if db:
    # Print the message to load the default setting of the database
    print(f"\nLoad the default setting of the database...\n")
    # Set the sleep time to 2 seconds
    time.sleep(2)   
    # If the returns of the functions "drop_table" and "create_table" are true, proceed with the execution of the SQL statements
    if drop_table(db) and create_table(db):
        # Set a list "field_list" to store the field names of the table
        field_list = ["id", "title", "author", "qty"]
        # Set a list "books" to store 5 rows of records
        books = [
            [3001, "A Tale of Two Cities", "Charles Dickens", 30],
            [3002, "Harry Potter and the Philosopher's Stone", "J.K. Rowling", 40],
            [3003, "The Lion, the Witch and the Wardrobe", "C. S. Lewis", 25],
            [3004, "The Lord of the Rings", "J.R.R Tolkien", 37],
            [3005, "Alice in Wonderland", "Lewis Carroll", 12]
        ]

        # Print the rows to be inserted into the table
        print(f"Populate the table with the given books into the {table_name} table:")
        # Call the function "print_records" with the parameters "books" and "field_list" 
        # to print the rows to be inserted.
        print_records(books, field_list)
        # Set the variable "row_affected" to store the row count of the records after inserting the record(s)
        # by calling the function "insert_record" with the parameters "db" and "books"
        row_affected = insert_record(db, books)
        # Print the number of records that are added successfully. 
        print(f"{row_affected} record(s) added successfully.\n")
        
        # Add extra books for testing purposes
        new_books = [
            [3006, "Python Crash Course", "Eric Matthes", 10],
            [3007, "Head-First Python", "Paul Barry", 20],
            [3008, "Invent Your Own Computer Games with Python", "Al Sweigart", 30],
            [3009, "Learn Python 3 the Hard Way", "Zed A. Shaw", 40],
            [3010, "Real Python Course", "Real Python Team", 50]            
        ]
        # Set the sleep time to 2 seconds 
        # Populate the table with the given records
        time.sleep(2)   
        # Print the new rows to be inserted into the table
        print(f"The following {colored_text('yellow', 'NEW')} rows into the {table_name} table for testing purpose:")
        # Call the function "print_records" with the parameters "books" and "field_list" 
        # to print the rows to be inserted.
        print_records(new_books, field_list)
        # Set the variable "row_affected" to store the row count of the records after inserting the record(s)
        # by calling the function "insert_record" with the parameters "db" and "books"
        row_affected = insert_record(db, new_books)       
        # Print the number of records that are added successfully. 
        print(f"Another {colored_text('yellow', row_affected)} record(s) added successfully.\n\n")

#       
# End: bookstore -> initialise the table "books"
# -------------------------------------------------------------------------------------------------------------- #
# Start: bookstore -> main body
#  
# Set a variable "is_print_banner" as true, print the banner the first time
is_print_banner = True
# Use the while-loop function to execute the following if/else statements as the condition is true
while True:
    # If the variable "is_print_banner" is true, print the banner by calling a function "print_banner"
    if is_print_banner:  
        print_banner()
        # Set a variable "note" to store the note for the user
        note = f"Note: All data will be restored to the default setting".upper()
        # Print the variable "note" with the required spaces
        print(f"{' ' * ((display_width - len(note)) // 2) } {colored_text('blink', f'{note}')}\n")
        # f"{colored_text('blink', note)}"
    # Set a variable "menu" to store the menu option the user entered
    # 4 majors function: Enter book, update book, delete book and search books
    menu = input(f"\nSelect one of the following options:\n\
1. Enter book \n\
2. Update book \n\
3. Delete book \n\
4. Search books \n\
0. Exit\n\
:   ").strip()
    
    # Print a new line
    print(f"\n")
    # If the variable "menu" is "1", call the function "enter_book"
    if menu == "1":
        enter_book()
    # If the variable "menu" is "2", call the function "update_book"
    elif menu == "2":
        update_book()
    # If the variable "menu" is "3", call the function "delete_book"
    elif menu == "3":
        delete_book()
    # If the variable "menu" is "4", call the function "search_book"
    elif menu == "4":
        search_book()
    # If the variable "menu" is empty, print the message "Bye" and use "break" to exit the while-loop
    elif menu == "0":
        print(f"\n{colored_text('cyan', 'Bye!')}\n")
        break
    # If any other cases, print the message to notify the user for entering the invalid menu option.
    else:
        print(f"\n{colored_text('red', 'You enter the invalid menu option.')}\n")
    # Set the variable "is_print_banner" to false if the operation is done
    is_print_banner = False
#
# End: bookstore -> main body
# -------------------------------------------------------------------------------------------------------------- #
# 
#  