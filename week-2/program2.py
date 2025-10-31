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