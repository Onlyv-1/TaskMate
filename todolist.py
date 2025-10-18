#!/usr/bin/python3
# add, remove, and view tasks
# Made by OnlyV
# v1.0
# https://github.com/Onlyv-1/TaskMate


import time
import os
from colorama import init, Fore, Style

tasks = []

def clean_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def add_task(task):
    tasks.append(task)
    print("adding task...")
    time.sleep(1.3)
    print(f'Task "{task}" added.')



def remove_task(index):
    if 0 <=  index < len(tasks):
        rem = tasks.pop(index)
        print("Removing task...")
        time.sleep(1.3)
        print(Fore.RED + f'Task "{rem}" removed.'+ Style.RESET_ALL)
    else:
        print(Fore.YELLOW + f'Task "{index}" not found.'+ Style.RESET_ALL)



def list_tasks():
    print("\n" * 20)
    clean_screen()
    print("------------------------------------")
    print("\n")
    if tasks == []:
        print(Fore.YELLOW + "No tasks available.\n"+ Style.RESET_ALL)
        return
    print(Fore.BLUE +'Available tasks:\n'+ Style.RESET_ALL)
    for i,task in enumerate(tasks):
        print(Fore.BLUE +f'#{i}. {task}\n'+ Style.RESET_ALL)


while True:
    try:
        print("------------------------------------")
        print("Things you can do : ")
        print("#1. Add a task")
        print("#2. Remove a task")
        print("#3. View tasks")
        print("#4. Quit")
        print("------------------------------------")
        action = input("What do you want to do? : ").strip()


        if action == "1":
            task = input(Fore.GREEN  +"Enter the task to add: "+ Style.RESET_ALL).strip()
            add_task(task)
        elif action == "2":
            remtask = int(input(Fore.RED +"Enter the task to remove: "+ Style.RESET_ALL))
            remove_task(remtask)
        elif action == "3":
            list_tasks()
            print("------------------------------------")
        elif action == "4":
            print("Program terminated !!✌")
            break
        else:
            print("Invalid option. Please try again.")

    except KeyboardInterrupt:
        print("Program terminated !!✌")

time.sleep(3.3)


