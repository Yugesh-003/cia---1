#3.Create a list of even numbers squared and odd numbers cubed from 1 to 10
numbers = [x**2 if x % 2 == 0 else x**3 for x in range(1, 11)]
print(numbers)
