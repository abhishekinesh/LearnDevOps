# update server.conf file when "max_connection" = 200

# function called updateserverconfig


import os

connection_value = input("Enter the connection needed : ") 

def update_config(file_path, key, value):
    with open(file_path,'r') as file:
        lines = file.readlines()
        print("Lines has been read")
    
    with open(file_path,'w') as file:
        for line in lines:
            if key in line:
                file.write(key + "=" + value +"\n")
            else:
                file.write(line)
        
update_config("server.conf","MAX_CONNECTIONS",connection_value)