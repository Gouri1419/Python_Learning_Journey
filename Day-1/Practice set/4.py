'''4. Write a python program to print the contents of a directory using the os module.
 Search online for the function which does that.'''
import os

path = "."   # Current directory

contents = os.listdir(path)

print("Directory contents:")
for item in contents:
    print(item)