# @MrGhost hope I am of help :)
# NOTE: if you run all the code together you will get a mess
# so run each question saperetly by commenting out the rest
# i havent used print in some questions to see the result print it

# Define a list named List1 that contains 6 random elements
# (the first element must be your first name and the third element
# must be your last name).



#1-2 since it says "random" i figured i would put integer and float too you can add boolean too
List1 = ["firstName", "secondName", "thirdName", 3423, 324.34, True]
print(List1)

#3----------------------------Next Question--------------------------

# printing third element
print(List1[2])

#4----------------------------Next Question--------------------------

# printing the list and the last element
# can be done seperetly
# 0 is first -1 is last you can...
print(List1, List1[-1])

# ...also do this
# this gets the length of the list which is 6
# and since indexing stats from 0 we have to minus by one
# to get 5 and print the last one
print(List1[len(List1)-1])

# or just do this
print(List1[5])

#5----------------------------Next Question--------------------------
List1[2] = 7

#6----------------------------Next Question--------------------------
List1[1] = 13

#7----------------------------Next Question--------------------------
# my second element is string so this is what i do
# i will make the second one to string because we cant add string and int together
# if your third value is integer then make sure your other value is integer too
List1[0] = List1[1] + List1[2]

#8----------------------------Next Question--------------------------
# Define a new list named V where V = [ 1, 2, 3], then replace the last
# element with the list V. (list inside a list).
V = [1, 2, 3]

# explained above
V[-1] = V

#9----------------------------Next Question--------------------------
# in mean: "if 2 is in" V return True and
# if an if statement is equal to True then it runs
if 2 in V:
    print("there is 2 in list V")

#10----------------------------Next Question--------------------------
# same as above but negative
if "Hello" not in V:
    print("there is not hello in list V")

#11---------------------------Next Question--------------------------
# Using slicing method, print the values from 1 to 3 of the List1.
# I dont know what does it mean by slicing method but I used For-Loop

for Num in range(3):
    print(List1[Num])

# or you can do this
print(List1[0])
print(List1[1])
print(List1[2])

#12----------------------------Next Question--------------------------
# Using slicing method, add the elements [5, 6, 7, 8]
# instead of the second and the third element.

# in hear does he mean to put a list inside a list? meaning
# replace 2 and three with [5, 6, 7, 8]

# or does it want me to insert? I will do the insert
# and which list should I insert to? V or List1. I'll do List1

List1[1] = 5
List1[2] = 6
# syntax: list_name.insert(index, element)
List1.insert(3, 7)
List1.insert(4, 8)

# if those two is not what is needed then this might be it
List1[1] = [5, 6, 7, 8]
List1[2] = [5, 6, 7, 8]

#13----------------------------Next Question--------------------------
# Using slicing method, delete the elements from 2 to 4.
del List1[1]
del List1[2]
del List1[3]

# or
List1.pop(1)
List1.pop(2)
List1.pop(3)

#14----------------------------Next Question--------------------------
List1.append(6000)

#15----------------------------Next Question--------------------------
List1.pop(-1)

#16----------------------------Next Question--------------------------
print(List1.pop(2))

#17----------------------------Next Question--------------------------
print(len(List1))

#18----------------------------Next Question--------------------------
# Define a new list V3, then combine the List1 with V3.
V3 = ["somestuff"]
V3 = [*V3, *List1]

# or
V3 = V3 + List1

#19----------------------------Next Question--------------------------
# Write a program that asks the user for a number.
# Depending on whether the number is even or odd,
# print out an appropriate message to the user.
userInput = input("Enter An Number: ")
#            \/ this is called remainder operetor i think
#            \/ it returns the remainder of (userInput devided by 2)
if int(userInput) % 2 == 0:
    print("the number is even")
# you can just put an else here
elif int(userInput) % 2 != 0:
    print("the number is odd")

#20----------------------------Next Question--------------------------
# Write a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells
# them the year that they will turn 90 years old.

userAge = input("Enter Your Age:")
userName = input("Enter Your Name: ")

currentYear = 2020
untilNinty = 90 - int(userAge)
print("you will be 90yo in " + str(untilNinty) + " more years which is " + str(currentYear + untilNinty))

#21----------------------------Next Question--------------------------
for i in range(1, 6):
    print()
    for j in range(i):
        # this end='' means dont go to new line
        # and the j+1 so it doesnt start with 0
        print(j+1, end="")
