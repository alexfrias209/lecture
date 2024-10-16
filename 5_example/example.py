import ipdb
import re


def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()  
        ipdb.set_trace()  
        print(content)
        lines = content.splitlines()  


        for line in lines:
            print(line)


if __name__ == "__main__":
    read_file('data.txt')





