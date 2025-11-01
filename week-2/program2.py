# name = input("enter your name : ")
# print("Your name is " + name)

# old_age = input("Enter your old age : ")
# new_age = int(old_age) + 3
# print ("Your current age is " + str(new_age))

# num1 = input("Enter a number : ")
# num2 = input("Enter another number :")
# sum = int(num1) + int(num2)
# print("The sum is : " + str(sum))

# name = "Pradumn Rathour"
# print(name.lower())
# print(name.upper())
# print(name)

# name = "Pradum rathour"
# print(name.replace("Pradum rathour", "Pro player"))
# print(name)

# name = "Tony stark"
# print(" tony" in name) # for single letter as well as whole string

# age = 19 
# if age >= 18 : 
#     print("You are adult \nyou can vote")
# else :
#     print("You are not adult \nyou can't vote")  



# basic calculator

# first = input("Enter first number :")
# operator = input ("Enter a operator (+, -, *, /, %) : ")
# second = input("Enter second number : ")
 
# first = int(first)
# second = int(second)

# if operator == "+" :
#     print(first + second)
# elif operator == "-" :
#     print(first - second)
# elif operator == "*" :
#     print(first * second)
# elif operator == "/" :
#     print(first / second)
# elif operator == "%" :
#     print(first % second)        
# else :
#     print("Invlaid operation")

# num = input("Enter a number : ")
# while i <= num :
#     print(i)
#     i = i + 1

# import time
# import sys

# def type_line(line, speed=0.09):
#     """Print a line letter by letter with typing animation."""
#     for char in line:
#         sys.stdout.write(char)
#         sys.stdout.flush()
#         time.sleep(speed)
#     print()  # move to next line

# def show_lyrics(lyrics_with_delay):
 
#     time.sleep(1)
   

#     for line, delay in lyrics_with_delay:
#         type_line(line)      # animated typing
#         time.sleep(delay)    # wait before next line

# # Each line has its own custom delay (in seconds)
# lyrics_with_delay = [
#     ("Barish ke aane se,", 0.5),
#     ("Tere bheeg jane se...", 0.9),
#     ("Dhadkna dil ka dekho,", 0.6),
#     ("tere shrmane se...🎧", 1.0),
#     ("Barish ke aane se,", 0.5),
#     ("Tere bheeg jaane se...🎧", 1.0),
# ]

# # Run it
# show_lyrics(lyrics_with_delay)

# i = 1 
# while i <= 9 : 
#     print(i * "* ")
#     i += 1

# for item in range (9) :
#     print (item + 1)

# # list s in python
# items = ["Pradumn", "Rathour", "Tony", "Stark", "45", "18"]
# print(items[5])

# # list s in python
# items = ["Pradumn", "Rathour", "Tony", "Stark", "45", "18"]
# print(items[3:6])

# list s in python
# items = ["Pradumn", "Rathour", "Tony", "Stark", "45", 18]
# items.insert(2, "Banner") # to insert item at specific index (2 here)
# items.append("Ironman") # tp add item at the end of list
# items.remove("45")     # to remove item from list

# for i in items :
#     print(i)
# print(18 in items)  # to check if item is present in list or not (returns boolean)
# print(len(items))   # to get length of list
# items.clear()    # to clear the list
# print(items)

# names = ["Pradumn", "Rathour", "Tony", "Stark", "45", 18]
# for name in names :
#     if name == "Tony" :
#         break
#     print(name)

# names = ["Pradumn", "Rathour", "Tony", "Stark", "45", 18]
# for name in names :
#     if name == "Tony" :
#         continue
#     print(name)


# num = (1, 2, 3, 4, 5, 6, 7, 8, 9, 2, 2, 2) # prantheseis() are not compulsory to define tuple
# print(num.count(2))  # to count occurence of an item in tuple
# print(num.index(2))  # to get index of an item in tuple 
# print(len(num))      # to get length of tuple

# set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 2, 2, 2} # indexing and slicing not supported in set
# print(set)
# for i in set :
#     print(i)

# dictionary = { "maths": 90, "science": 80, "english": 85 } # dictionary ( stores data in key value pair )
# print(dictionary["maths"])
# # to add item in dictionary
# dictionary["history"] = 75 
# print(dictionary) 

# import math
# print(dir(math))  # to see all functions and variables in math module
# print(help(math.sqrt))  # to see how a particular function works in module  

# # to import specific function from module
# from math import sqrt
# print(sqrt(49))