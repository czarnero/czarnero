from base64 import *
# 5x decode base16, 5x decode base32, 5x decode base64
# solves THM's Intro to Python challenge (Task 12) but allows for any file to be read, not just encodedflag.txt

user_input = input("Enter filename ")
flag = open(user_input, "r").read()

for i in range(0,5):
    flag = b16decode(flag)

for i in range(0,5):
    flag = b32decode(flag)

for i in range(0,5):
    flag = b64decode(flag)  

print(flag)
