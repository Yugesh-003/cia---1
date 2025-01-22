# Sum of natural numbers up to num

print("Calculate sum of n natural numbers")

n = int(input("Enter 'n' : "))

if n < 0:
   print("Input error. Enter a positive number")
else:
   sum = 0
   # use while loop to iterate until zero
   while(n > 0):
       sum += n
       n -= 1
   print("The sum is", sum)