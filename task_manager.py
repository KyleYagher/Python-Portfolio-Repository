#=====importing libraries===========
'''This is the section where you will import libraries'''
from collections import UserList
from datetime import date
from itertools import count
from re import S
from ast import Try


#====Functions====#

#____Login function____|

def login_user(login, nested_user_obj, nested_Users_obj):

    # read in user.txt file, strip and split data to store 
    # nested list as nested users object.  
    with open('user.txt', 'r') as f:
        nested_Users_obj = [(lines.strip('\n')).split(', ') for lines in f.readlines()]
    
    # While loop that handles user inputs
    while login == False:
        print(f'''
    \n{'**' * 13}|- Task Manager -|{"**" * 13}
    \n{'  ' * 14}- User Login -
    \n{'*****' * 14}\n''')

        # Store user inputs as nested user object
        nested_user_obj = [input('Username: '), input('\nPassword: ')] 
        
        # check if nested user object matches nested users object
        # If yes change login boolean to true, if not throw 
        # error and repeat loop 
        if nested_user_obj in nested_Users_obj:
            login = True
            print("\n***Successfully Authenticated***\n")
            break
        elif nested_user_obj not in nested_Users_obj:
            print("\nmmmmh Thats not right...!!\n")
    
    return(login, nested_user_obj, nested_Users_obj)


#____Display task Menu____|

def task_menu(taskNum):
    while taskNum == 0:
        try:
            taskNum = int(input(('''
*************************************************
-  To view a specific task input the task ID!  -
*******************Task Menu*********************
*************************************************

: ''').title())) 
            return(taskNum)
            break
        
        except ValueError:
            print('\nIncorrect Selection | Please Try Again!!\n')

#____Check for duplicate users____|

def check_user(taskUser, usersList):
    '''Function that checks if a user exist in userlist and proceed based on the existing, loops if false.'''

    # Store usernames as list variable
    usersList = [item[0] for item in usersList]

        # While loop that controls the username input loop
    while True:
        taskUser = input('\nUsername:')
        
        # Condition that checks if username exists and input is 
        # not empty.
        if taskUser not in usersList and taskUser != '':

            # Prints error message if user not found or input is 
            # empty
            print(f"\nCannot assign task to '{taskUser}'. Please check and try again!!")

        # If false prints error and loops user input
        else: 
            return(taskUser)
            break

#____register users____|

def reg_user(usersList):
    pass
    '''
    -   Function that registers a new user and password. 
    -   Requests new username and checks for duplicate match.
    -   Requests new user password and password confirmation and checks match
    -   writes new username and password to user.txt file.
    '''
    pass
    # Store usernames as list variable
    usersList = [item[0] for item in usersList]
    
    print(f'''
\n{'**' * 13}|- Task Manager -|{"**" * 13}
\n{'  ' * 12}- Create a New User -
\n{'*****' * 14}\n''')


    # While loop that controls the username input loop
    while True:
        newUser = input('\nNew Username: ')

        # Condition that checks if duplicate username exists and 
        # input is not empty.
        if newUser not in usersList and newUser != '':
            
            # Nested while loop that controls the password and 
            # password confirmation input loops.
            while True:
                newPassword = input('\nUser Password: ')
                passConfirm = input('\nConfirm Password: ')

                # Nested if condition that checks if passwords 
                # and password confirmation match. Inputs stored 
                # as a formatted string variable.
                if newPassword == passConfirm:
                    creds = '\n' + newUser + ', ' + newPassword
                    break
               
                # if passwords do not match, prints an error 
                # message. 
                else:
                    print('\nPasswords do not match!')
            
            # Break for the outer loop
            break

        # If duplicate username exists or input empty prints 
        # error message.  
        else: 
            print('\nThat does not appear to be correct. Please try again!!')
    
    # Opens user.txt and appends credentials to file and print 
    # confirmation.    
    with open('user.txt', 'a') as f:    
        f.write(creds)
        print(f"\nNew User '{newUser}' successfully created!")

#____add_task____|

def add_task():
    pass
    # Declare boolean variable 'taskComplete' as No
    # Declare empty string variable 'lines'
    taskUser = ''
    taskComplete = 'No'
    lines = ''

    print(f'''
\n{'**' * 13}|- Task Manager -|{"**" * 13}
\n{'  ' * 12}- Create a New Task -
\n{'*****' * 14}\n''')

    # Request user to input username to assign to task
    # and store as variable 'taskUser'. Runs 'check_user' 
    # function to verify user exists.
    print("\nPlease input username to assign to task!!\n")
    taskUser = check_user(taskUser, usersList)

    # Request User to input task title ad store as variable
    print("\nPlease input the title of the task!!\n")
    taskTitle = 'Title'#input("Title: ")

    # Request User to input task description and store as 
    # variable
    print("\nPlease input a brief description of the task!!\n")
    TaskDescription = 'Description'#input("Description: ")

    # Request user to input task due date and store as 
    # variable
    print("\nPlease Assign a due date to the task!!\n")
    taskDD = 'Due Date'#input("Due date: ")

    # Get todays date and store as variable 'today'
    today = 'Date'#date.today()

    # Inittialize 'taskList' list variable
    # Assign task varibles as list values
    taskList = f"\n{taskUser}, {taskTitle}, {TaskDescription}, {taskDD}, {today}, {taskComplete}"

    with open('tasks.txt', 'a') as f:
        f.write(taskList)

#____view_all____|

def view_all():
    pass
    # Declare list variable 'lines' and count variable 'num'
    lines = []
    num = 0

    with open('tasks.txt', 'r+') as f:
        # Open file and store content in list variable
        for line in f:
            lines.append(line.replace('\n', '').split(', '))

            # Display application lines
            print('_____' * 14)

            while num < len(lines):
                # loop over list variable and Display Task 
                # data in required format
                print(f'''\nTask: \t\t\t {lines[num][1]}
                    \nAssigned To: \t\t {lines[num][0]}
                    \nDate Assigned: \t\t {lines[num][4]}
                    \nDue Date: \t\t {lines[num][3]}
                    \nTask Complete? \t\t {lines[num][5]}
                    \nTask Description:''')
                print(f'\n{lines[num][2]}')
                num += 1

            # Display application lines
            print('_____' * 14)    

#____view_mine____|



def view_mine(currentUser):
    '''
    - Function that displays a minified
      version of the users task list as well as
      an expanded view. Also includes a task 
      menu where the user can mark tasks 
      complete or edit existing tasks. 
    '''
    pass

    # Declare empty list variables and counter
    taskList = []
    userTasks = []
    taskCount = 0

    # Reade in the tasks file and stores as a
    # dicttionary variable.
    with open('tasks.txt', 'r+') as f:
        content = f.readlines()
        content = dict(list(enumerate(content, 1)))  

        # Iterates over the dictionay and extracts 
        # the tasks data to display the minified view.
        # Also stores current user tasks and in list 
        # variable
        print('_____' * 14)

        for keys, tasks in content.items():
            if currentUser in tasks:
                taskCount += 1
                tasks = (tasks.strip()).split(',')
                print('_____' * 14)
                print(f'''
                \nID: {'-' * 29}>  {taskCount}\n
                \nTask: {'-' * 27}> {tasks[1]}\n
                \nDue Date: {'-' * 23}> {tasks[4]}
                ''')
                print('_____' * 14)
                taskList += [tasks]

            else:
                otherTasks = (tasks.strip()).split(',')
                userTasks += [tasks] 

        print('_____' * 14, '\n')


        while True:
            '''
            - While loop that handles the user 
              input to view the exapanded task.
            '''

            try:
                taskNum = int(input('\nView task by ID: '))
            except ValueError:
                print('\nIncorrect selection | Please Try Again!!\n')
            except IndexError:
                print('\nIncorrect selection | Please Try Again!!\n')


            if taskNum != -1:

                try:
                    index = taskNum - 1

                    print('_____' * 14) 

                    print(f'''
                        \nID: {'.' * 31} {taskNum}
                        \nTask: {'.' * 29}{taskList[index][1]}
                        \nAssigned To: {'.' * 22} {taskList[index][0]}
                        \nDate Assigned: {'.' * 20}{taskList[index][4]}
                        \nDue Date: {'.' * 25}{taskList[index][3]}
                        \nTask Complete: {'.' * 20}{taskList[index][5]}
                        \nDescription: {'.' * 57}\n
                        ''')
                    print(f'{taskList[index][2]}'.strip())

                    print('_____' * 14)
                    break

                except taskNum == -1:
                    break
            else:
                print('\nIncorrect Task number selected | Please Try again!!\n')
        
        while True:
            '''
            - While loop that handles the task menu
              optopns user input.
            '''

            try:
                taskNum = input(f'''
                    \n{'**' * 13}|- Task Manager -|{'**' * 13}
                    \n{' ' * 4}Mark Complete : 'X' \tEdit Task : 'E' \tmain menu : -1
                    \n{'*' * 70}
                    \n: ''').title()
            except ValueError:
                print('\nIncorrect selection | Please Try Again!!\n')
            except IndexError:
                print('\nIncorrect selection | Please Try Again!!\n')

            # Conditions that handle the user input 
            # types for editing tasks.
            if taskNum == 'X':
                taskList[index][5] = ' Yes'
                    
            elif taskNum == 'E':
                taskUser = ''
                
                try:
                    if taskList[index][5] ==' Yes':
                        print('\nCannot edit a completed task | Please check!')
                        break

                    else:
                        print(f'''\n{'**' * 13}|- Edit Task -|{'**' * 13}\n''')
                        taskList[index][0] =      check_user(taskUser, usersList)

                        taskList[index][4] = input("Due date: ")
                                                     
                except:
                    print('Cannot edit a completed task')

            elif taskNum == '-1':
                break
        
        # Initialize string and count variables .
        data = ''
        pos = 0

        # Merge current user task data  with global 
        # user task data.
        content = userTasks + taskList
        
        while pos < len(content):
            '''
            - While loop that prepares the data for 
              writing to file. Stored in a string 
              variable
            '''
            data += f"{content[pos][0]}, {content[pos][1]}, {content[pos][2]}, {content[pos][3]}, {content[pos][4]}, {content[pos][5]}\n"
            pos += 1

    # Write data to file.
    with open('tasks.txt', 'w') as f:       
        f.write(data.rstrip('\n'))
        

#____Login Section____|

'''
- Here you will write code that will allow a user to login.
- Your code must read usernames and password from the user.txt file
- You can use a list or dictionary to store a list of usernames and passwords from the file.
- Use a while loop to validate your user name and password.
'''
login = False
currentUser = ''
nested_user_obj = []
nested_users_obj = []
loginAuth = login_user(login, nested_user_obj, nested_users_obj)
login = loginAuth[0]
currentUser = loginAuth[1][0]
usersList = loginAuth[2]


while login == True:

    if currentUser == 'admin':
        print(f'''
\n{'**' * 10}|- Welcome to Task Manager -|{"**" * 10}
\n{' ' * 27}- Main Menu -
\n{'*' * 69}\n''')

        # Present the menu to the admin user and 
        # making sure that the user input is coneverted to lower case.
        menu= input(f'''Select one of the following Options below:\n
r   - Registering a user

a   - Adding a task

va  - View all tasks

vm  - view my task

s   - Admin Stats    

e   - Exit

: ''').lower()
        print('\n')

    elif currentUser != 'admin':
        print(f'''
\n{'**' * 10}|- Welcome to Task Manager -|{'**' * 10}
\n{' ' * 27}- Main Menu -
\n{'*' * 69}\n''')
        # presenting the menu to the user and 
        # making sure that the user input is coneverted to lower case.
        menu= input(f'''Select one of the following Options below:\n
r   - Register a user

a   - Add a task

va  - View all tasks

vm  - view my task

e   - Exit

: ''').lower()
        print('\n')
        

    if menu == 'r'and currentUser == 'admin':
        pass
        '''In this block you will write code to add a new user to the user.txt file
        - You can follow the following steps:
            - Request input of a new username
            - Request input of a new password
            - Request input of password confirmation.
            - Check if the new password and confirmed password are the same.
            - If they are the same, add them to the user.txt file,
            - Otherwise you present a relevant message.'''
        reg_user(usersList)

    elif menu == 'r' and currentUser != 'admin':
        #Throw error if Current user not an Admin
        print('''
        \t  - You're barking up the wrong tree\n
        \t- Please consult with admin for help!!!'''.title())

    elif menu == 'a':
        pass
        '''In this block you will put code that will allow a user to add a new task to task.txt file
        - You can follow these steps:
            - Prompt a user for the following: 
                - A username of the person whom the task is assigned to,
                - A title of a task,
                - A description of the task and 
                - the due date of the task.
            - Then get the current date.
            - Add the data to the file task.txt and
            - You must remember to include the 'No' to indicate if the task is complete.'''
        add_task()
        
    elif menu == 'va':
        pass
        '''In this block you will put code so that the program will read the task from task.txt file and
         print to the console in the format of Output 2 presented in the L1T19 pdf file page 6
         You can do it in this way:
            - Read a line from the file.
            - Split that line where there is comma and space.
            - Then print the results in the format shown in the Output 2 in L1T19 pdf
            - It is much easier to read a file using a for loop.'''
        view_all()
    
    elif menu == 'vm':
        pass
        '''In this block you will put code the that will read the task from task.txt file and
         print to the console in the format of Output 2 presented in the L1T19 pdf
         You can do it in this way:
            - Read a line from the file
            - Split the line where there is comma and space.
            - Check if the username of the person logged in is the same as the username you have
            read from the file.
            - If they are the same you print the task in the format of output 2 shown in L1T19 pdf '''
        view_mine(currentUser)

    elif menu == 's':
        pass
        '''
        -   In this block I display a menu option only visible to 'admin' users.
            *   Number of tasks in the system
            *   Number of users registered on the system
        '''

        # Create count variables
        taskCount = 0
        userCount = 0

        # Process task filess and count each line
        with open('tasks.txt', 'r') as f:
            for lines in f:
                taskCount += 1

        with open('user.txt', 'r') as f:
            for lines in f:
                userCount += 1

        # Display application lines
        print('___' * 25)

        #Display nuumber of tasks and users
        print(f'''\nNumber of Registered Tasks: \t\t {taskCount}
                \nNumber of Registered Users: \t\t {userCount}
                ''')

        # Display application lines  
        print('___' * 25)
    
    elif menu == 'e':
        print('Goodbye!!!')
        exit()
    
    else:
        print("You have made a wrong choice, Please Try again")