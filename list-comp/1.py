#1.Find all of the numbers from 1-1000 that are divisible by 7
num = [x for x in range(1, 1001) if x % 7 == 0]
print(num)