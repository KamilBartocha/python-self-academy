import os
text = "Yooooooooo\nThis is some text\nHave a good one!\n"
path = os.getcwd()
file_path = path + "/020_example_file.txt"

#--- Writing---
with open(file_path,'w') as file:
    file.write(text)

with open(file_path, 'a') as file:
    file.write("Adding(append) line to file")

# ---Reading---

with open(file_path) as file:
    print(file.read())

try:
    with open("1.txt") as file:
        print(file.read())
except FileNotFoundError as er:
    print(f"File was not found,{er}")