#Write a Python program to check whether a given key already exists in a dictionary.
dic = {'Name':'Ram','Age':23}

key = input("Enter a key :")

if key in dic:
    print("Key already exist.")
else:
    print("Key does not exist.")
