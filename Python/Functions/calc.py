num1 = float(input("Type the first number : "))
num2 = float(input("Type the second number : "))

def addition(num1,num2):
    sum = num1+num2
    # print("Sum of the numbers is : ",sum)
    return sum

def substarction(num1,num2):
    diff = num1-num2
    # print("Difference of the numbers is : ",diff)
    return diff

def multiplication(num1,num2):
    mult = num1*num2
    # print("Multiplicated value of the numbers is : ",mult)
    return mult

def division(num1,num2):
    division = num1/num2
    # print("Divided value of the numbers is : ",division)
    return division


print("Sum is : ",addition(num1,num2))
print("Diff is : ",substarction(num1,num2))
print("Mult is : ",multiplication(num1,num2))
print("Divide is : ",division(num1,num2))