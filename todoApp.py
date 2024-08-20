taskList:list = []

def addTask(task):
    taskList.append(task)

def deleteTask(task):
    taskInt = int(task)
    taskList.pop(taskInt-1)
    print(f'Task "{task}" has successfully been removed. ')

def viewTasks():
    for index, task in enumerate(taskList, start=1):
        print(f"{index} {task}")



while True:

    options:list = ["view tasks", "delete task", "add task", "exit"]
    print("Available options: ")
    for index, option in enumerate(options, start=1):
        print(f"{index}. {option}")

    user_input:str = input("What would you like to do?: ")


    if user_input == "add task" or user_input == "3":
        task:str = input("What task would you like to add?: ")
        addTask(task)
    elif user_input == "delete task" or user_input == "2":
        viewTasks()
        task:int = input("Which number task would you like to delete?: ")
        deleteTask(task)
    elif user_input == "view tasks" or user_input == "1":
        if taskList[0] == None:
            print("There are no tasks to display. ")
        else:
            viewTasks()

    elif user_input == "exit" or user_input == "4":
        quit()
        




