﻿# finalCapstone
Notes: 
1. Use the following username and password to access the admin rights 
# username: admin
# password: password
2. Ensure you open the whole folder for this task in VS Code otherwise the 
 program will look in your root directory for the text files.

This code reads usernames and password from the user.txt file to allow a user to login.
If no user.txt file, write one with a default account
create function reg_user() to save username and password
create function add_task() to add a new task     
Allow a user to add a new task to task.txt file
Prompt a user for the following: 
A username of the person whom the task is assigned to,
A title of a task,
A description of the task and the due date of the task.
Add the data to the file task.txt and Include 'No' to indicate if the task is complete.

create functions view_all() to view all task in tasks.txt     
Reads the task from task.txt file and prints to the console in the format of Output 2 presented in the task pdf (i.e. includes spacing and labelling) 

create function view_mine() to view all task of particular user in tasks.txt
Reads the task from task.txt file and prints to the console in the format of Output 2 presented in the task pdf (i.e. includes spacing and labelling)

create functions edit_task() to edit task , mark as completed, change the username and date

create functions choose_task() to choose which task have to edit
        
create function generate_report() to write all the information in task_overview.txt

create function display_stat() to print all the information about task_overview.txt 
If the user is an admin they can display statistics about number of users and tasks.

print menu and ask user input to call out functions
presenting the menu to the user and making sure that the user input is converted to lower case.
