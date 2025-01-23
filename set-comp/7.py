#7.Create a set of unique characters from a list of words
words = ['apple', 'banana', 'cherry']
unique= {char for i in words for char in i}
print(sorted(unique))
