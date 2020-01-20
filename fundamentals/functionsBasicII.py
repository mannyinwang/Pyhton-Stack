# Countdown
def countDown(a):
    b = []
    for i in range(a,0,-1):
        b.append(i)
    b.append(0)
    return b
print(countDown(5))

# Print and Return
def pAndR(a):
    print(a[0])
    return(a[1])
print(pAndR([2,3]))

#  First plus Length
def FandL(a):
    b = len(a)
    return b + a[0]
print(FandL([10,2,3,4,5,6]))

# Values greater than second
def greaterThanSecond(a):
    b = [] 
    c = len(a)
    count = 0
    if (len(a) < 2):
        return False
    else:
        for i in range(c):
            if (a[i] > a[1]):
                b.append(a[i])
                count = count + 1
    print(count)
    return b
print(greaterThanSecond([5]))
            
#This Length, That Value
def valAndLen(size, value):
    b = []
    for i in range(size):
        b.append(value)
    return b
print(valAndLen(4,10))