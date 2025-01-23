#5.Create a list of numbers that are divisible by both 3 and 5 from 1 to 100
num = [x for x in range(1, 101) if x % 3 == 0 and x % 5 == 0]
print(num)