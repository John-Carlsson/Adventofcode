#Task one

with open('data1.txt', 'r', encoding='UTF-8') as file:
            lines = file.readlines()

count = 0
for i in range(len(lines)-1):
    if int(lines[i+1]) > int(lines[i]):
        count +=1
print(count)

# Task two
# compare a three unit window
i = 3
next = 0
count = 0
a,b,c = 0,0,0
while i != len(lines):
    prev = a+b+c
    a = int(lines[i-2])
    b = int(lines[i-1])
    c = int(lines[i])
    next = a+b+c
    if next > prev:
        count += 1
    i += 1
print(count)
