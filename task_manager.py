# Notes: 
# 1. Use the following username and password to access the admin rights 
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the 
# program will look in your root directory for the text files.

#=====importing libraries===========
import os
from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"

# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

with open("tasks.txt", 'r') as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]


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

#create function reg_user() to save username and password
def reg_user():
    '''Add a new user to the user.txt file'''
        
    while True:
        # - Request input of a new username
        new_username = input("New Username: ")
        if new_username in username_password.keys():
            print("Username had been used, please try the others.")
            continue
        else:
            break

        # - Request input of a new password
    new_password = input("New Password: ")

        # - Request input of password confirmation.
    confirm_password = input("Confirm Password: ")

        # - Check if the new password and confirmed password are the same.
    if new_password == confirm_password:
            # - If they are the same, add them to the user.txt file,
        print("New user added")
        username_password[new_username] = new_password
            
        with open("user.txt", "w") as out_file:
            user_data = []
            for k in username_password:
                user_data.append(f"{k};{username_password[k]}")
            out_file.write("\n".join(user_data))

        # - Otherwise you present a relevant message.
    else:
        print("Passwords do no match")

#create function add_task() to add a new task        
def add_task():
    # '''Allow a user to add a new task to task.txt file
    # Prompt a user for the following: 
    # - A username of the person whom the task is assigned to,
    # - A title of a task,
    # - A description of the task and 
    # - the due date of the task.'''
    while True:
        task_username = input("Name of person assigned to task: ")
        while task_username not in username_password.keys():
            print("User does not exist. Please enter a valid username")
            task_username = input("Name of person assigned to task: ")
        else:
            task_title = input("Title of Task: ")
            task_description = input("Description of Task: ")
        while True:
            try:
                task_due_date = input("Due date of task (YYYY-MM-DD): ")
                due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
                break
            except ValueError:
                print("Invalid datetime format. Please use the format specified")    
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
            "completed": False}

        task_list.append(new_task)
        with open("tasks.txt", "a") as task_file:
                task_list_to_write = []
                for t in task_list:
                    str_attrs = [t['username'],
                                t['title'],
                                t['description'],
                                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                                "Yes" if t['completed'] else "No"]
                task_list_to_write.append(";".join(str_attrs))
                task_file.write('\n'+ " ".join(task_list_to_write))
                print("Task successfully added.")
                break
#create functions view_all() to view all task in tasks.txt     
def view_all():
    '''Reads the task from task.txt file and prints to the console in the 
           format of Output 2 presented in the task pdf (i.e. includes spacing
           and labelling) 
        '''
    for t in task_list:
        disp_str = f"Task: \t\t {t['title']}\n"
        disp_str += f"Assigned to: \t {t['username']}\n"
        disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Task Description: \n {t['description']}\n"
        print(disp_str)

#create function view_mine() to view all task of particular user in tasks.txt
def view_mine():
    '''Reads the task from task.txt file and prints to the console in the 
           format of Output 2 presented in the task pdf (i.e. includes spacing
           and labelling)
        '''
    task_num = 0
    list_num = -1    
    global num_dict
    num_dict = {}
    for t in task_list:
        list_num += 1
        if t['username'] == curr_user:
            task_num += 1
            num_dict[task_num] = list_num
            disp_str = f"Task:{task_num}\n"
            disp_str = f"Task: \t\t {t['title']}\n"
            disp_str += f"Assigned to: \t {t['username']}\n"
            disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Task Description: \n {t['description']}\n"
            print(disp_str)
    global total_task
    total_task = task_num
    return total_task, num_dict

#create functions edit_task() to edit task , mark as completed, change the username and date
def edit_task(list_num,complete_or_edit): 
    if complete_or_edit == "c":
        task_list[list_num]['completed'] = True
    elif complete_or_edit == "e":
        while True:
            usernume_or_duedate = str(input('''Please selecr on of the following options:
            \n u - change the username of the person to whom the task assigned 
            \n d - change the due date of the task
            \n b - back to last menu
            \n '''))
            if usernume_or_duedate == "u":
                while True:
                    task_username = input("Name of per assigned to task: ")
                    if task_username not in username_password.keys():
                        print("User dose not exist, please enter a valid username.")
                    else:
                        task_list[list_num]["username"] = task_username
                    break
            elif usernume_or_duedate == "d":
                while True:
                    try:
                        task_due_date = input("Due date of task(YYYY-MM-DD)")
                        due_date_time = datetime.strptime(task_due_date,DATETIME_STRING_FORMAT)
                        task_list[list_num]["due_date"] = due_date_time
                        break
                    except ValueError:
                        print("Invalid datetime format. Please use the format specified.")
                        break
            elif usernume_or_duedate == "b":
                print("Save and back to last menu")
                break
            else:
                print("Error, please enter u or d")
                continue
    with open("tasks.txt","w")as task_file:
        task_list_to_write = []
        for t in task_list:
                str_attrs = [t['username'],
                    t['title'],
                    t['description'],
                    t['due_date'].strftime(DATETIME_STRING_FORMAT),
                    t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                    "Yes" if t['completed'] else "No"]
                task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))
        print("Task successfully edited.")

#create functions choose_task() to choose which task have to edit
def choose_task():
    while True:
        try:
            task_number = int(input("Please enter the task number to select the task or input -1 to return to the main menu: "))
            if task_number == -1:
                break
            elif task_number == 0:
                print("Task number cannot be 0")
            elif task_number <= total_task:
                list_num = num_dict[task_number]
                if task_list[list_num]['completed'] == True:
                    print("Task marked as complete and cannot be edit")
                    continue
                else:
                    while True:
                        complete_or_edit = str(input('''Please selecr on of the following options:
                        \n c - mark the task as complete \n e - edit the task: \n''')).lower()
                        if complete_or_edit == "c" or complete_or_edit == "e":
                            edit_task(list_num,complete_or_edit)
                            break
                        else:
                            print("Error, Please enter 'c' or 'e': ")
                            continue
            else:
                print("Task number not available.")
        except:
            print("Invalid input, please try again.")

#create function generate_report() to write all the information in task_overview.txt
def generate_report():
    overwrite = "n"
    try:
        with open("task_overview.txt", "r")as task_overview_file:
            task_overview_file.read()
    except:
        overwrite = "y"
    else:
        while True:
            print("task_overview.txt or user_overview already exist")
            overwrite = str(input("Please enter'y'to overwrite the file or enter'n'to back to menu(y/n): ")).lower()
            if overwrite == "y" or overwrite == "n":
                break
            else:
                print("Invalid input.")
    finally:
        if overwrite == "y":
            total_task = 0
            completed_task = 0
            uncompleted_task = 0
            uncompleted_overdue_task = 0
            task_overview_str = ""
            total_user = 0
            user_str = ""

            for t in task_list:
                total_task += 1
                if t["completed"] == True:
                    completed_task += 1
                else:
                    uncompleted_task += 1
                    if t['due_date'] > datetime.today():
                        uncompleted_overdue_task += 1
            
            for user in username_password:
                total_user += 1
                user_total_task = 0
                user_completed_task = 0
                user_uncompleted_task = 0
                user_uncompleted_overdue_task = 0
                for t in task_list:
                    try:
                        if t['username'] == user:
                            user_total_task += 1
                            if t["completed"] == True:
                                user_completed_task += 1
                            else:
                                user_uncompleted_task += 1
                                if t['due_date'] > datetime.today():
                                    user_uncompleted_overdue_task += 1
                    except:
                        pass
                    if user_total_task == 0:
                        user_str += f'''{user}This user has no task\n'''
                    else:
                        user_str += f'''{user}\n{user_total_task}tasks assigned to{user}\n
                        {user_total_task/total_task*100}%of the total number of tasks that 
                        have been assigned to {user}\n
                        {user_completed_task/user_total_task*100}% of the tasks assigned to {user}
                        that have been completed\n
                        {user_uncompleted_task/user_total_task*100}% of the task assigned to {user}
                        that must still be completed\n
                        {user_uncompleted_overdue_task/user_total_task*100}% of the tasks assigned to 
                        {user} that have not yet been completed and overdue\n\n'''

                        user_overview_str = f'''
                        {total_user} users registered with task_manager.py
                        {total_task} tasks that have been generated and tracked using task_manager.py\n'''
                        user_overview_str += user_str

                        with open("task_overview.txt","w")as task_overview_file:
                            if total_task == 0:
                                task_overview_str = "There is no task."
                            else:
                                task_overview_str = f'''
                                {total_task} tasks have been generated and tracked using the task_manager.py
                                {completed_task} completed tasks
                                {uncompleted_task} uncomplete tasks
                                {uncompleted_overdue_task} tasks that haven't been completed and that are over due
                                {uncompleted_task/total_task*100}% tasks that are incompleted
                                {uncompleted_overdue_task/total_task*100}% tasks that are over due'''
                            task_overview_file.write(task_overview_str)

                            with open("user_overview.txt","w")as user_overview_file:
                                user_overview_file.write(user_overview_str)
                else:
                    pass

#create function display_stat() to print all the information about task_overview.txt 
def display_stat():
    '''If the user is an admin they can display statistics about number of users and tasks.'''
    num_users = len(username_password.keys())
    num_tasks = len(task_list)

    print("-----------------------------------")
    print(f"Number of users: \t\t {num_users}")
    print(f"Number of tasks: \t\t {num_tasks}")
    print("-----------------------------------")    
        
    try:
        with open("task_overview.txt","r")as task_overview_file:
            print(task_overview_file.read())
        with open("user_overview.txt","r")as user_overview_file:
            print(user_overview_file.read())
    except:
        print("Something wrong with file handling.")

#print menu and ask user input to call out functions
while True:
    # presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    print()
    menu = input('''Select one of the following Options below:
r - registering a user
a - adding a task
va - view all tasks
vm - view my task
gr - generate reports
ds - display statistics
e - exit
: ''').lower()
    if menu == 'r':
        reg_user()
    elif menu == 'a':
        add_task()
    elif menu == 'va':
        view_all()
    elif menu == 'vm':
        my_total_task, number_dict = view_mine()
        choose_task()
    elif menu == 'gr':
        generate_report()
        print("Report has been generate.")
    elif menu == 'ds' and curr_user == 'admin': 
        display_stat()
    elif menu == 'e':
        print('Goodbye!!!')
        exit()
    else:
        print("Error, Please Try again")