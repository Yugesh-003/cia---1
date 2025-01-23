#9.Create a set of even numbers from 1 to 50 that are not divisible by 4
end= {x for x in range(1, 51) if x % 2 == 0 and x % 4 != 0}
print(sorted(end))
