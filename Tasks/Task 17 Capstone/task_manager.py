# Notes: 
# 1. Use the following username and password to access the admin rights 
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the 
# program will look in your root directory for the text files.

#=====importing libraries===========
import os
from datetime import datetime, date

# CONSTANTS
DATETIME_STRING_FORMAT = "%Y-%m-%d"
ERR_MARK = "\t!!!\t"
ERR_MSG = f"{ERR_MARK}Please enter a valid option{ERR_MARK}"


#___________FUNCTIONS_SECTION_____________
def prnt_task(t):
        disp_str = f"Task: \t\t {t['title']}\n"
        disp_str += f"Assigned to: \t {t['username']}\n"
        disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Task Description: \n {t['description']}\n"
        print(disp_str)


def get_due_date():
    while True:
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
            break

        except ValueError:
            print("Invalid datetime format. Please use the format specified")
    return due_date_time


    #_____MENU OPTIONS_____
def reg_user():
    '''Add a new user to the user.txt file'''


    def w_user():
        """Writes a new user to user.txt"""
        with open("user.txt", "w") as out_file:
            user_data = []
            for k in username_password:
                user_data.append(f"{k};{username_password[k]}")
            out_file.write("\n".join(user_data))


    def pass_check():
        """Check if new_password matches confirm_password"""
        if new_password == confirm_password:
        # - If they are the same, add them to the user.txt file,
            print("New user added")
            username_password[new_username] = new_password
            w_user()
        else: # Password Mismatch
            print("Passwords do not match")

           
    # - Request input of a new username
    unique = False
    while unique == False:
        new_username = input("New Username: ")
        # - Make sure username doesn't already exist
        with open("user.txt","r") as user_file:
            for line in user_file:
                if new_username in line.split(";"):
                    print("\tThis user already exists.\n\tUsername must be unique.")
                    unique = False
                    break
                else:
                    unique = True

    # - Request input of a new password
    new_password = input("New Password: ")

    # - Request input of password confirmation.
    confirm_password = input("Confirm Password: ")

    # - Check if new_password and confirm_password are the same.
    pass_check()


def add_task():
    '''Allow a user to add a new task to task.txt file
        Prompt a user for the following: 
            - A username of the person whom the task is assigned to,
            - A title of a task,
            - A description of the task and 
            - the due date of the task.'''
    while True:
        task_username = input("Name of person assigned to task: ")
        if task_username not in username_password.keys():
            print("User does not exist. Please enter a valid username")
            continue
        else:
            break
    task_title = input("Title of Task: ")
    task_description = input("Description of Task: ")
    due_date_time = get_due_date()
    # Then get the current date.
    curr_date = date.today()
    ''' Add the data to the file task.txt and
        Include 'No' to indicate if the task is complete.'''
    new_task = {
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": False
    }

    task_list.append(new_task)
    with open("tasks.txt", "w") as task_file:
        task_list_to_write = []
        for t in task_list:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))
    print("Task successfully added.")
    

def view_all():
    '''Reads the task from task.txt file and prints to the console in the 
    format of Output 2 presented in the task pdf (i.e. includes spacing
    and labelling) 
    '''
    for t in task_list:
        prnt_task(t)


def view_mine(): # vm for short
    '''Reads the task from task.txt file and prints to the console in the 
    format of Output 2 presented in the task pdf (i.e. includes spacing
    and labelling)'''

    def vm_list():
        """Displays an enumerated list of tasks for logged-in user"""
        print("\nView My Tasks: ")
        # Enumerates task list for scalable options menu
        for enum, task in enumerate(task_list):
            if task['username'] == curr_user:
                print(f"[{enum}]\t-> {task["title"]}")
        print("[-1]\t-> Go Back")

    
    def vm_select():
        """Selects a task to interact with"""
        while True:
            vm_list()
            user_input = input("Input task-number: ")
            # Input handling
            user_input = menu_input_check(user_input, range(-1, len(task_list)))
            if user_input == "error":
                continue
            elif user_input == -1:
                break
            else:
                read_edit_mark(task_list[user_input])


    def read_edit_mark(task):
        while True:
            print("\nView My Tasks>Options: ")
            print("[1]\t-> Read\n[2]\t-> Edit\n[3]\t-> Toggle Complete\n[-1]\t-> Go Back")
            user_input = input("Enter an option-number: ")
            user_input = menu_input_check(user_input, range(-1, 4))
            if user_input == 1:
                prnt_task(task)
            elif user_input == 2:
                task_edit_menu(task)
            elif user_input == 3:
                toggle_complete(task)
            elif user_input == -1:
                break # Go Back


    def task_edit_menu(task):
        """Menu for editing options"""
        def change_user(task):
            """Changes tasks assignee"""
            while True:
                print("\nView My Tasks>Options>Edit>Change Assignee: ")
                print(f"Current user assigned is: {task["username"]}")
                change = input("New Assignee: ")
                if change in username_password:
                    task["username"] = change
                    print(f"Assignee changed to {change}.")
                    break
                else:
                    print("User does not exist. Remember Case Sensitivity.")
                    continue


        def change_task_date(task):
            """Changes tasks date"""
            print("\nView My Tasks>Options>Edit>Change Due Date: ")
            print(f"\nCurrent due date is: {task["due_date"]}")
            task["due_date"] = get_due_date()
            print("Due date of task updated.")

            
        # task_edit_menu MAIN BODY
        while True:
            print("\nView My Tasks>Options>Edit: ")
            print("[1]\t-> Change Assignee\n[2]\t-> Change Due Date\n[-1]\t-> Go Back")
            user_input = input("Enter an option-number: ")
            user_input = menu_input_check(user_input, range(-1,3))
            if user_input == 1:
                change_user(task)
            elif user_input == 2:
                change_task_date(task)
            elif user_input == -1:
                break # Go Back
            else:
                print(ERR_MSG)
    

    def toggle_complete(task):
        """Toggles task 'complete' attribute"""
        if task["completed"] == True:
            task["completed"] == False
            print("\nTask marked as INCOMPLETE.")

        elif task["completed"] == False:
            task["completed"] == True
            print("\nTask marked as COMPLETE.")


    # - __VM_MAIN_BODY__ - #
    
    vm_select()


# Misc Methods Section
def num_input_check(num_input):
    """Checks if user input is convertable to int or float"""
    # Checks if input is int first to prevent every int being assigned float
    if num_input.strip("-").isnumeric():
        return int(num_input)
    elif num_input.replace(".","").isnumeric():
        return float(num_input)
    else:   # Returns input. Otherwise input would become NoneType
        return num_input
    
def menu_input_check(user_input, menu_len):
    """Standardisation of input menus"""
    user_input = num_input_check(user_input)
    if type(user_input) != int:
        print(f"{ERR_MARK}Please enter a number{ERR_MARK}")
        return "error"
    elif user_input not in menu_len:
        print(f"{ERR_MARK}Please enter a number from the options listed{ERR_MARK}")
        return "error"
    else:
        return user_input

#___________MAIN_BODY_____________
# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

# - Builds list of raw task data
with open("tasks.txt", 'r') as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]
# - Organises task data into a dictionary
task_list = []
for t_str in task_data:
    curr_t = {}

    # Split by semicolon and manually add each component
    task_components = t_str.split(";")
    curr_t['username'] = task_components[0]
    curr_t['title'] = task_components[1]
    curr_t['description'] = task_components[2]
    curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
    curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
    curr_t['completed'] = True if task_components[5] == "Yes" else False
# - Adds each task dict to task_list
    task_list.append(curr_t)


#====Login Section====
'''This code reads usernames and password from the user.txt file to 
    allow a user to login.
'''
# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password

logged_in = False
while not logged_in:

    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user not in username_password.keys():
        print("User does not exist")
        continue
    elif username_password[curr_user] != curr_pass:
        print("Wrong password")
        continue
    else:
        print("Login Successful!")
        logged_in = True

#====MENU SECTION====
while True:
    # presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my tasks
ds - Display statistics
e - Exit
: ''').lower()

    if menu == 'r':
        reg_user()
        
    elif menu == 'a':
        add_task()
        
    elif menu == 'va':
        view_all()

    elif menu == 'vm':
        view_mine()
    
    elif menu == 'ds' and curr_user == 'admin': 
        '''If the user is an admin they can display statistics about number of users
            and tasks.'''
        num_users = len(username_password.keys())
        num_tasks = len(task_list)

        print("-----------------------------------")
        print(f"Number of users: \t\t {num_users}")
        print(f"Number of tasks: \t\t {num_tasks}")
        print("-----------------------------------")    

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong user_input, Please Try again")