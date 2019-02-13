import hashlib as hash
import os

def get_files(dir):
    return [f for f in os.listdir('.') if os.path.isfile(f)]
    
def string(file_path):
    f = open(file_path, 'r')
    print("file is : ",f.read())
if __name__ == "__main__":
    li = get_files("~/rushikesh/antivirus")
    for f in li:
        string(f)