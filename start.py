import hashlib as ha
import urllib.request as webopener
import os
hash_ = ha.md5()
def get_files(dir):
    return [f for f in os.listdir('.') if os.path.isfile(f)]
    
def string(file_path):
    f = open(file_path, 'r')
    print("file is : ",f.read())

def prepare_data():
    f = open("sig.data", "r")
    lines = [line.rstrip('\n') for line in f]
    lines.sort()
    fr = open("virus_sig.csv", "w+")
    for l in lines:
        fr.write(str(l) + "\n")
if __name__ == "__main__":
    li = get_files("~/rushikesh/antivirus")
    for f in li:
        print("F : ", f)
        with open(f, "rb") as fi:
            for chnk in iter(lambda: fi.read(4096), b""):
                hash_.update(chnk)
        print(hash_.hexdigest())
    prepare_data()


