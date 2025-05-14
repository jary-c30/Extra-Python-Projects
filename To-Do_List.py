#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 12 2025

@author: jary
"""

print("Welcome to your to-do list\n1. Add and Item\n2. Remove an Item\n3. View To-Do list\n4. Toggle Task\n5. Swap Task\n6. Exit")

option = input("please input an option: ")

list1 = []
taskTracker = []

while option.isdigit():
    if option == "1":
        task = input("\nAdd an item: ")
        list1.append(task)
        taskTracker.append(0)

    elif option == "2":
        c = 1
        print("")
        for i in list1:
            print(f"{c}. {i}")
            c = c + 1

        remove = input("choose an item to remove: ")

        remove2 = (int(remove)) - 1
        remove3 = list1[remove2]
        list1.remove(remove3)
        print(f"\n{remove3} Removed!")

    elif option == "3":
        if len(list1) == 0:
            print("\nTo-Do list empty")
            enter = input("press enter to continue.")

        else:
            c = 1
            print("")
            for i in list1:
                if taskTracker[c - 1]:
                    print(f"{c}. {i}: done")
                else:
                    print(f"{c}. {i}: not done")
                c = c + 1

            enter = input("press enter to continue.")

    elif option == "4":
        c = 1
        print("")
        for i in list1:
            if taskTracker[c - 1]:
                print(f"{c}. {i}: done")
            else:
                print(f"{c}. {i}: not done")
            c = c + 1

        toggle = input("choose an item to toggle: ")
        toggle2 = (int(toggle)) - 1
        toggle3 = list1[toggle2]
        taskTracker[toggle2] = 1
        print(f"\n{toggle3} set to done")

    elif option == "5":
        c = 1
        print("")
        for i in list1:
            if taskTracker[c - 1]:
                print(f"{c}. {i}: done")
            else:
                print(f"{c}. {i}: not done")
            c = c + 1

        swap = input("choose an item to move: ")
        swap2 = input("choose a position to move to: ")
        temp = list1[int(swap) - 1]
        list1[int(swap) - 1] = list1[int(swap2) - 1]
        list1[int(swap2) - 1] = temp
        print(f"\n{temp} moved")
        temp = taskTracker[int(swap) - 1]
        taskTracker[int(swap) - 1] = taskTracker[int(swap2) - 1]
        taskTracker[int(swap2) - 1] = temp

    elif option == "6":
        option = ""

    if option.isdigit():
        print("\n1. Add and Item\n2. Remove an Item\n3. View To-Do list\n4. Toggle Task\n5. Swap Task\n6. Exit")
        option = input("please input an option: ")
