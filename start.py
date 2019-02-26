import hashlib as ha
import urllib.request as webopener
import os
import math
hash_ = ha.md5()
def get_files(dir):
    return [f for f in os.listdir('.') if os.path.isfile(f)]
    
def string(file_path):
    f = open(file_path, 'r')
    print("file is : ",f.read())

def prepare_data(upd = None):
    f = open("sig.data", "r")
    lines = [line.rstrip('\n') for line in f]
    upd = [hex(v) for v in upd]
    if upd : lines = lines + upd
    lines = list(dict.fromkeys(lines))
    lines.sort()
    
    fr = open("vsig.defdb", "wb")
    # if upd :
    #     for inte in upd:
    #         fr.write(tobytearray(inte, leng=16))
    # else:
    for l in lines:
        num = int( l, 16)
        fr.write(tobytearray(num, leng=16))

def file_hash(f):
    with open(f, "rb") as fi:
        cont = fi.read()
        return ha.md5(cont).hexdigest()
    return hash_.hexdigest()

def scan(dir_path):
    files = get_files(dir_path)
    
    # print("Files : ", files)
    db = open("./virus_sig.csv", "r")
    vfiles = []
    # print(db)
    for f in files:
        md5_hash = int(file_hash(f), 16)
        # for l in db:
        
        # print("f : ", f , ", md5_hash : ", hex(md5_hash))
        with open("./vsig.defdb", "rb") as db:
            l = db.read(16)
            g = toint(l)
            while l:
                # print("f : ", f ,"g : ", g, ", md5_hash : ", md5_hash)
                    
                if md5_hash == g:
                    # print("g : ", g, ", md5_hash : ", md5_hash)
                    print(f, " : ", "virus............")
                    # print(os.stat(f).st_size)
                    fname = os.path.split(f)[1]
                    # print("--> ", fname)
                    vfiles.append({'fname': fname.split(".")[0], 'path': f ,'extension': fname.split(".")[1] ,'size': os.stat(f).st_size})
                    # print(vfiles)
                l = db.read(16)
                g = toint(l)

    return vfiles

def length(n, base = 2):#return no. of bits in number
    return int(math.log2(n) / math.log2(base) + 1)
def tobytearray(n, leng = None):#convert integer 'n' to bytearray of spcefied length
    leng = leng if leng else length(n, 256)
    arr = bytearray(leng)
    for i in range(leng - 1, -1, -1):
        arr[i] = n & 0xff
        n >>= 8
    return arr
def toint(b_arr):#converts bytearray to integer
    n = 0
    for byt in b_arr:
        n = (n << 8) + byt
    return n


def update():#updates the virus signature definition
    url = 'https://drive.google.com/file/d/1psL8EFDN-EOV8X5bhn-C5CIC8ARwN5DY/view?usp=sharing'
    url = 'https://drive.google.com/uc?export=view&id=1psL8EFDN-EOV8X5bhn-C5CIC8ARwN5DY'
    content = webopener.urlopen(url).read()
    # print(content)
    i = 0
    upd = []
    for _ in range(len(content) // 16):
        # print(content[i:i+16])
        # print("i : ",i,"con : ", hex(toint(content[i:i+16])))
        # with open("virus_sig.csv", "a") as f:
        upd.append(toint(content[i:i+16]))
        i = i + 16
    prepare_data(upd)

      

if __name__ == "__main__":
    li = get_files("~/rushikesh/antivirus")
    # for f in li:
    #     print("F : ", f)
    #     print(file_hash(f))
    # prepare_data()
    g = scan("~/rushikesh/antivirus")
    print(g)
    update()


