"""
import libraries





initialise un_input variable
initialise pw_input variable
declare count variable = 0
initialise menu_input variable
initialise new_user variable
initialise new_pass variable
initialise confirm variable
initialise a_task_title variable
initialise a_task_desc variable
initialise a_task_due variable
initialise a_task_split variable

initialise username list
initialise password list
initialise current_line list
declare menu_options list [r, a, va, vm, e]
initialise assign_to list
initialise task_title list
initialise task_desc list
initialise task_due list
initialise task_split list
declare months list ['none','Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']





open user.txt in 'r+' mode
    for every line in user.txt
        current_line = line split at ", "
        username.append current_line[0]
        password.append current_line[1]

open tasks.txt in 'r+' mode
    for every line
        task_split = line split at ', '
        assign_to.append(task_split[0])
        task_title.append(task_split[1])
        task_desc.append(task_split[2])
        task_due.append(task_split[3])





while un_input is not in username
    count += 1
    if count = 1
        get username from user
    else
        print error message
        get username from user

reset count

while pw_input is not in password
    count += 1
    if count = 1
        get password from user
    else
        print error message
        get password from user





while menu_input.lower() is not in menu_options
    if un_input = admin
        print(
            Please select one of the following options:

            r  - register user
            a  - add task
            va - view all tasks
            vm - view my tasks
            s  - statistics
            e  - exit
            
            : )

    else
        print(
            Please select one of the following options:

            a  - add task
            va - view all tasks
            vm - view my tasks
            e  - exit
            
            : )

        get menu_input from user





if menu_input = r and un_input = admin
    get user input for new_user
    get user input for new_pass
    get user input for confirm

    while confirm != new pass
        get user input for confirm
        
    new_user += ', ' + str(new_pass)
    append new_user to user.txt 

elif menu_input = a
    get input for assign_to[0]
    get input for task_title[0]
    get input for task_desc[0]
    get input for task_due[0]

    write data to tasks.txt
    assign_to, task_title, task_desc, task_due = []

elif menu_input = va
    for i in range(0, length(assign_to))
        print assign_to[i], task_title[i], task_desc[i], task_due[i]

elif menu_input = vm
    for i in range(0, length(assign_to))
        if assign_to[i] = un_input
            print assign_to[i], task_title[i], task_desc[i], task_due[i]

elif menu_input = s and un_input = admin
    print length of task_title
    print length of username

elif menu_input = e
    print 'Exiting Task Manager'

else
    print error message
"""



#====Importing libraries====

import datetime
from datetime import date



#====Initialisations/Declarations====

un_input = ''
pw_input = ''
count = 0
menu_input = ''
new_user = ''
new_pass = ''
confirm = ''
a_task_title = ''
a_task_desc = ''
a_task_due = ''
a_task_split = ''
today = date.today()

task_split = []
username = []
password = []
current_line = []
menu_options = ['r', 'a', 'va', 'vm', 's', 'e']
assign_to = []
task_title = []
task_desc = []
date_set = []
task_due = []
done = []
# List below used to format the datetime numeric month value to a string equivalent
months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']




#====Initial Data Read Section====

# Reading in user.txt file
with open ('user.txt','r+') as e:
    for line in e:
        # Splits user and password and appends into lists
        current_line = line.split(", ")
        username.append(current_line[0])
        password.append(current_line[1].replace('\n',''))

# Reading in tasks.txt file
with open ('tasks.txt','r+') as f:
    for line in f:
        # Splits each line in tasks.txt into a list 
        task_split = line.split(', ')
        # Assigning each different type of data to its own list
        assign_to.append(task_split[0])
        task_title.append(task_split[1])
        task_desc.append(task_split[2])
        date_set.append(task_split[3])
        task_due.append(task_split[4])
        done.append(task_split[5].replace('\n',''))




#====Login Section====
print('''

       ---------/============\---------
-------= = = = <-TASK MANAGER-> = = = =------- 
       ---------\============/---------

''')
while un_input not in username:
    count += 1
    #If loop runs for first time, no error message shown
    if count == 1:
        un_input = input("Please enter your username: ")
    else:
        un_input = input("Incorrect username, please try again: ")

count = 0

# Check if matching password is inputted using index() function
while pw_input != password[username.index(un_input)]:
    count += 1

    #If loop runs for first time, no error message shown
    if count == 1:
        pw_input = input("Please enter your password: ")
    else:
        pw_input = input("Incorrect password, please try again: ")



#====Menu Input Section====

while menu_input.lower() != 'e':

    # Checks input against list of acceptable answers
    while menu_input.lower() not in menu_options:
        # Presents different menu if user is logged in as 'admin'
        if un_input == 'admin':
            menu_input = input("""

--- MAIN MENU (Administrator mode) ---

Please select one of the following options:
______________________________________________

r  - register user
a  - add task
va - view all tasks
vm - view my tasks
s  - statistics
e  - exit
______________________________________________
: """)

        else:
            # Regular user menu
            menu_input = input("""

--- MAIN MENU ---

Please select one of the following options:
______________________________________________

a  - add task
va - view all tasks
vm - view my tasks
e  - exit
______________________________________________
: """)



    #====Menu Tasks====

    # Register user
    if menu_input.lower() == 'r' and un_input == 'admin':

        print('\n--- Register User ---\n')

        new_user = str(input('Please enter a new username to be registered: '))
        new_pass = str(input('Please enter a new password for the new user: '))
        confirm = str(input('Please confirm the new password: '))

        while confirm != new_pass:
            confirm = str(input('Incorrect, please retry to confirm the new password: '))
            
        with open ('/Users/aaron/OneDrive - University of West London/Drive/HyperionDev SE/Task 21 - Capstone 2/user.txt','a+') as g:
            g.write(f'\n{new_user}, {new_pass}')
        username.append(new_user)
        password.append(new_pass)

        print('''User Registration Complete
______________________________________________
______________________________________________''')

        menu_input = ''




    # Add task
    elif menu_input.lower() == 'a':

        print('\n--- Add Task ---\n')

        a_assign_to = str(input('Please assign the task to a user: '))
        a_task_title = str(input('Please enter the task title: '))
        a_task_desc = str(input('Please enter the task description: '))
        a_task_due = str(input('Please assign the due date of the task: '))

        with open ('/Users/aaron/OneDrive - University of West London/Drive/HyperionDev SE/Task 21 - Capstone 2/tasks.txt','a+') as h:
            h.write(f'\n{a_assign_to}, {a_task_title}, {a_task_desc}, {today.day} {months[today.month-1]} {today.year}, {a_task_due}, No')

        assign_to.append(a_assign_to)
        task_title.append(a_task_title)
        task_desc.append(a_task_desc)
        date_set.append(f'{today.day} {months[today.month-1]} {today.year}')
        task_due.append(a_task_due)
        done.append('No')

        print('''\nTask Successfully Added
______________________________________________
______________________________________________''')

        menu_input = ''




    # View all tasks
    elif menu_input.lower() == 'va':

        print('\n--- All Tasks ---\n')

        for i in range(0, len(assign_to)):
            print(f'''--Task {i+1}--
       User:    {assign_to[i]}
      Title:    {task_title[i]}
Description:    {task_desc[i]}
   Date Set:    {date_set[i]}
   Due Date:    {task_due[i]}
   Complete?    {done[i]}\n''')
        
        print('''______________________________________________
______________________________________________''')

        menu_input = ''




    # View my tasks
    elif menu_input.lower() == 'vm':
        
        count = 0
        print('\n--- My Tasks ---\n')

        for i in range(0, len(assign_to)):
            # Checks if username is equal to the assigned user for the task
            if assign_to[i] == un_input:
                count += 1
                print(f'''--Task {count}--
       User:    {assign_to[i]}
      Title:    {task_title[i]}
Description:    {task_desc[i]}
   Date Set:    {date_set[i]}
   Due Date:    {task_due[i]}
   Complete?    {done[i]}\n''')
   
        if count < 1:
            print('''No Tasks

______________________________________________
______________________________________________''')

        menu_input = ''



    # Statistics
    elif menu_input.lower() == 's':

        print('\n--- Statistics ---\n')
        # Prints number of tasks and usernames
        print(f'Number of tasks: {len(assign_to)}')
        print(f'Number of users: {len(username)}')

        print('''______________________________________________
______________________________________________''')

        menu_input = ''



    # Exit
    elif menu_input.lower() == 'e':

        print('\nExiting Task Manager')

        print('''______________________________________________''')