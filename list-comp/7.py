#7.Create a list of strings with vowels replaced by asterisks
words = ["apple", "banana", "cherry"]
a= [''.join('*' if char in 'aeiouAEIOU' else char for char in word) for word in words]
print(a)
