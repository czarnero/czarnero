from base64 import *
# 5x decode base16, 5x decode base32, 5x decode base64
# solves THM's Intro to Python challenge (Task 12)

flag = open("encodedflag.txt", "r").read()

for i in range(0,5):
    flag = b16decode(flag)

for i in range(0,5):
    flag = b32decode(flag)

for i in range(0,5):
    flag = b64decode(flag)  

print(flag)
