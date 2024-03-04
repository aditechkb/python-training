import os

def check_if_file_exists(file_path):
    if os.path.exists(file_path):
        return 1
    else:
        return 0


def read_file_content(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        file_content = file.read()
        print(file_content)


file_path = './data/text-files/simple-txt-file.txt'
file_exists = check_if_file_exists(file_path)

if file_exists:
    read_file_content(file_path)
else:
    print ("Could not find the file at given path!")