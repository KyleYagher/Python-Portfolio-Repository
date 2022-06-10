#=====importing libraries===========
'''This is the section where you will import libraries'''
from datetime import date
from re import S

#====Login Section====
'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file.
    - Use a while loop to validate your user name and password.
'''
# Declare empty list variable 'credentials' and
# set boolean variable 'login' and 'extendMenu' to 'False'
credentials = []
login = False
extendMenu = False

with open('user.txt', 'r') as f:
    # Process input file and store content in list variable
    for line in f:
        credentials.append(line.replace('\n', ''))
        
while login == False:
    # While boolean remains false repeat user inputs and
    # Declare string variable 'currentUser'
    # store as 'userInput' string variable
    print('''\nWelcome to Task Manager :)
            \nPlease input your Username and Password!!\n''')
    currentUser = input('UserName: ')
    userInput = f"{currentUser}, {input('Password: ')}"
    
    # check if input string matches string in list
    # If yes change boolean to true, if not throw error message
    if userInput in credentials:
        login = True
        print("\n***Successfully Authenticated***\n")

    elif userInput not in credentials:
        print("\nmmmmh Thats not right...!!\n")

while login == True:

    if currentUser == 'admin':
        print('\n')
        # presenting the menu to the admin user and 
        # making sure that the user input is coneverted to lower case.
        menu= input(f'''Select one of the following Options below:
r   - Registering a user
a   - Adding a task
va  - View all tasks
vm  - view my task
s   - Admin Stats    
e   - Exit
: ''').lower()
        print('\n')

    elif currentUser != 'admin':
        print('\n')
        # presenting the menu to the user and 
        # making sure that the user input is coneverted to lower case.
        menu= input(f'''Select one of the following Options below:
r   - Registering a user
a   - Adding a task
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
        
        # Declare 'lines' string variable
        lines = ''

        # User to input new username and store as variable 'newUser'
        newUser = input("Please input new username: ")

        #User to input new password and store as variable 'newPassword'
        newPassword = input(f"Please input a password for {newUser}: ")

        #User to confirm password input
        passconfirm = input(f"Please confirm password for {newUser}: ")

        if newPassword == passconfirm:
            #If passwords match add inputs to list variable
            credentials = [f'{lines}\n' + f'{newUser}, {newPassword}']

            with open('user.txt', 'r+') as f:
                for line in f:
                    lines += line
                #Iterate over list variable and write output to file
                for creds in credentials:
                    f.write(creds)

        else:
            #If passwords do not match print error message
            print("Passwords do not match, Please Try again!!")

    elif menu == 'r' and currentUser != 'admin':
        #Throw error if Current user not an Admin
        print("You're barking up the wrong tree \nPlease ensure you are assogned to the appropriate UserGroup!!")

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

        # Declare boolean variable 'taskComplete' as No
        # Declare empty string variable 'lines'
        taskComplete = 'No'
        lines = ''

        # Request user to input username to assign to task and store as variable
        print("\nPlease input username to assign to task!!\n")
        taskUser = input("Username: ")

        # Request User to input task title ad store as variable
        print("\nPlease input the title of the task!!\n")
        taskTitle = input("Title: ")

        # Request User to input task description and store as variable
        print("\nPlease input a brief description of the task!!\n")
        TaskDescription = input("Description: ")

        # Request user to input task due date and store as variable
        print("\nPlease Assign a due date to the task!!\n")
        taskDD = input("Due date: ")

        # Get todays date and store as variable 'today'
        today = date.today()

        # Inittialize 'taskList' list variable
        # Assign task varibles as list values
        taskList = [f"{lines} \n" + f"{taskUser}, {taskTitle}, {TaskDescription}, {taskDD}, {today}, {taskComplete}"]

        with open('tasks.txt','r+') as f:
            # Open file and store content in string variable
            for line in f:
                lines += line
            # Iterate over list variable and write output to file
            for task in taskList:
                f.write(task)

    elif menu == 'va':
        pass
        '''In this block you will put code so that the program will read the task from task.txt file and
         print to the console in the format of Output 2 presented in the L1T19 pdf file page 6
         You can do it in this way:
            - Read a line from the file.
            - Split that line where there is comma and space.
            - Then print the results in the format shown in the Output 2 in L1T19 pdf
            - It is much easier to read a file using a for loop.'''

        # Declare list variable 'lines' and count variable 'num'
        lines = []
        num = 0

        with open('tasks.txt', 'r+') as f:
            # Open file and store content in list variable
            for line in f:
                lines.append(line.replace('\n', '').split(', '))

                # Display application lines
                print('___' * 25)

                while num < len(lines):
                    # loop over list variable and Display Task data in required format
                    print(f'''\nTask: \t\t\t {lines[num][1]}
                            \nAssigned To: \t\t {lines[num][0]}
                            \nDate Assigned: \t\t {lines[num][4]}
                            \nDue Date: \t\t {lines[num][3]}
                            \nTask Complete? \t\t {lines[num][5]}
                            \nTask Description:\t\t\n {lines[num][2]} \n''')
                    num += 1

                # Display application lines
                print('___' * 25)
    
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

        # Declare empty list variable 'lines'
        lines = []

        with open('tasks.txt', 'r') as f:
            # Open files and store in list variable
            for line in f:
                lines.append(line.replace('\n', '').split(', '))

            # Display application lines
            print('___' * 25)

            for taskList in lines:

                # Iterate over list and display tasks assigned to current user
                if currentUser in taskList:
                    print(f'''\nTask: \t\t\t {taskList[1]}
                            \nAssigned To: \t\t {taskList[0]}
                            \nDate Assigned: \t\t {taskList[4]}
                            \nDue Date: \t\t {taskList[3]}
                            \nTask Complete? \t\t {taskList[5]}
                            \nTask Description:\t\t\n {taskList[2]} \n''')

            # Display application lines  
            print('___' * 25)
        
    elif menu == 's':
        pass
        '''In this block I display a menu option only visible to 'admin' users.
            - Number of tasks in the system
            - Number of users registered on tyhe sustem'''

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