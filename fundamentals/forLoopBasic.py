# print all integers from 0 - 255
for i in range(256):
    print(i)

# Print multiples of 5s
for i in range(1001):
    if i % 5 == 0:
        print(i)

# counting the dojo way 
for i in range(101):
    if i % 10 ==0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)

# Whoa, thats sucker is huge
# Add Odd integers from 0 to 500000 and the print the sum
sum = 0
for i in range(500000):
    if i % 2 != 0:
        sum = sum + i
print (sum)

# Print positive numbers from 2018 counting down by 4
for i in range(2020,0,-4):
    if i % 4 == 0:
        print(i)

# Flexible Counter - Set three variables: lowNum, highNum, mult. 
lowNum = 5
highNum = 49
mult = 7
for i in range(lowNum,highNum,1):
    if i % mult == 0:
        print(i)
