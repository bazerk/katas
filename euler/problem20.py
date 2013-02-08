
total = 1
for x in range(1, 101):
    total *= x
print sum(int(digit) for digit in str(total))
