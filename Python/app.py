# print("Hello world")
# age = 25
# age = 30
# price = 19.12
# first_name = "abhi"
# is_online = True
# ------------------

# print("Patient Check In")
# first_name = "john Smith"
# age = 20
# new_patient = True

# print("Name:",first_name)
# print("Age :",age)
# print("New Patient :",new_patient)

# -----------------------

# Input function

# First_Name = input("What is your name? ")
# print("Hello " + First_Name)

# -------------------------

# Type conversion

# birth_year = input("Enter your DOB : ") 
# age = 2024 - int(birth_year)
# print("You are ",age, "years old")

# ------------------
# CALCULATOR

# first = float(input("Input first number : "))
# second = float(input("Input second number : "))

# sum = first + second

# print("SUM = ",sum)

# --------------------------
# STRINGS

# course = "imma noob"
# print(course.upper())
# print(course)
# print(course.lower())
# print(course)

# print("noob" in course)



# print(course.replace('noob','pro'))


# =============================
# Arithmetic operators

# print(10//3)
# print(10/3)
# print(10**3)

# x = 10
# # x = x+3
# x += 3
# print(x)

# y = (10 + 3) * 2
# print(y)

# z = 3 > 2
# print(z)


# --------------------------------
# Logical operators

# price = 5
# print(price > 10 and price <30)

# print(price > 10 or price <30)

# --------------------------

# IF STATEMENTS

# temp = int(input("Input the temprature today :"))
# if temp > 30:
#     print("its a hot day")
#     print("Drink")
# elif temp > 20:
#     print("Its a nice day")
# else:
#     print("Its very cold")
# print("Done")


# Exercise

# weight = float(input("Input the weight :"))
# unit = input("(K)g or (L)bs : ")

# if unit.upper() == "K":
#     converted = weight * 2.204
#     print("Your weight in Lb : ",converted)
# elif unit.upper() == "L":
#     converted = weight / 2.204
#     print("Your weight in Kg : ",converted)



# ----------------------------------
# WHILE LOOPS


# i = 1
# while i <= 10:
#     print(i * "*")
#     i=i+1


# ----------------------

# LISTS

# names = ["shattu", "ammu", "serah"]
# print(names)
# print(names[2])
# print(names[-2])
# names[0] = "Shattboi"
# print(names)
# print(names[0:2])

# ----------------------

# LISTS METHODS

# numbers = [1,2,3,4,5]
# numbers.append(6)
# print(numbers)

# numbers.insert(0,10)
# print(numbers)

# numbers.remove(3)
# print(numbers)

# print(1 in numbers)
# print(len(numbers))


# ----------------------------------
# FOR LOOPS

# numbers = [1,2,3,4,5]
# print(numbers)

# for item in numbers:
#     print(item)


# ----------------------------------
# RANGE FUNCTION

# numbers = range(5, 20, 2)
# print(numbers)

# for item in numbers:
#     print(item)


# -----------------------------
# TUPLES

numbers = (1,2,3,4,3,5)
print(numbers[0])
numbers.count(3)
numbers.index(3)