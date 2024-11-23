import os

NerVariable = input("Enter the variable you need to add : ")
VariableValue = input("Enter the value you need : ")

# os.environ[NerVariable]=VariableValue

db_user = os.getenv(NerVariable)
print(db_user)