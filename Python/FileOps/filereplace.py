file_path = "text2.txt"

find_text = input("Enter the text to find: ")

replace_text = input("Enter the text to find: ")

try:
    with open(file_path, 'r') as file:
        content = file.read()
    updated_content = content.replace(find_text, replace_text)

    with open(file_path,'w') as file:
        file.write(updated_content)

    print(f"Replaced all occurrences of '{find_text}' with '{replace_text}'.")
except FileNotFoundError:
    print(f"Error: The file '{file_path}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")


