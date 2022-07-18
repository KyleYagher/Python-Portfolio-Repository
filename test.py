from collections import UserList


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
                taskList.append(tasks.split(','))
                
                while True:

                    print('_____' * 14)
                    print(f'''
                    \nID: {'-' * 29}>  {taskCount}\n
                    \nTask: {'-' * 27}> {tasks.split(',')[1]}\n
                    \nDue Date: {'-' * 23}> {tasks.split(',')[4]}
                    ''')
                    print('_____' * 14)

                    break

            elif currentUser not in tasks:

                userTasks.append((tasks.replace).split(','))

        print('_____' * 14, '\n')
        print(taskList)
        print(userTasks)

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
                taskList[index][5] = ' Yes\n'
                break
                    
            elif taskNum == 'E':
                #taskUser = ''
                
                try:
                    if taskList[index][5] ==' Yes':
                        print('\nCannot edit a completed task | Please check!')
                        break

                    else:
                        print(f'''\n{'**' * 13}|- Edit Task -|{'**' * 13}\n''')
                        taskList[index][0] = 'kylo'    #check_user(taskUser, usersList)

                        taskList[index][4] = 'date'#input("Due date: ")
                        break
                                                     
                except:
                    print('Cannot edit a completed task')

            elif taskNum == '-1':
                break
        
        # Initialize string and count variables .
        data = ''
        pos = 0

        # Merge current user task data  with global 
        # user task data.
        taskMerge = taskList
        taskMerge.extend(userTasks)
        print(taskMerge)
        for x in range(0, len(taskMerge)):
            for y in taskMerge[x]:
                '''
                - While loop that prepares the data for 
                  writing to file. Stored in a string 
                  variable
                '''
                
                if y == ' No' or y ==' Yes':
                    print('True', y)
                    data += f'{y}'
                        
                    
                else:
                    print('False', y)
                    data += f'{y}\n'
                
                            
        print(data.format())
    #print(data)

    # Write data to file.
    #with open('tasks.txt', 'w') as f:
        #f.write(data)
        

currentUser = 'admin'
view_mine(currentUser)