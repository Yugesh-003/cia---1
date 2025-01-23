#to delete a list of keys from a dictonary

sample_dict = {"name":"Kelly","age":25,"salary":8000,"city":"newyork"}

keys = ["name","salary"]

for i in keys:
    if i in sample_dict:
        del sample_dict[i]
print(sample_dict)