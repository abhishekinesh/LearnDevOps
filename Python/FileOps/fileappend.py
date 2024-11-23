try:
    content=input("Type the string to append : ")
    with open("text2.txt",'a') as file:
        file.write(content + '\n')
except Exception as e:
    print("An error occured: {e}")