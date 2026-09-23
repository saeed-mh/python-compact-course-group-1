s1 = "hello123world4"

total = 0
count = 0

for x in s1:
    if x in "0123456789":
        total = total + int(x)
        count = count + 1

print("Sum:", total)
print("Average:", total / count)
