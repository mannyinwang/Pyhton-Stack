def a ():
    return 5
print(a()) # Prints 5

def ab():
    return 5
print(ab()+ab()) # Prints 5 + 5 = 10

def b():
    return 5
    return 10
print(b()) # Prints only 5

def bc():
    return 5
    print(10)
print(bc()) # Prints just 5 and not the 10

def c():
    return (5)
x = c()
print(x) # Prints 5

# def cd(a,b):
#     print(a+b)
# print(cd(1,2) + cd(2,3)) # pops up an error because the function does not return any value.

def d(b,c):
    return str(b) + str(c)
print(d(2,5)) # Result is 25

def de():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(de()) # prints the valube of b which is 100 and returns 10

def e(a,b):
    if a < b:
        return 7
    else:
        return 14
    return 3
print(e(2,3)) # returns 7
print(e(5,3)) # retruns 14
print(e(2,3)+e(5,3)) # retruns 7+14= 21

def ef(b,c):
    return b+c
    return 10
print(ef(3,5)) # returns 3+5=8

b = 500
print(b)
def z():
    b = 300
    print(b)
print(b)
z()
print(b) # prints 500, then prints another 500, then runs the function and prints 300 and finally prints 500

b = 500
print(b)
def y():
    b = 300
    print(b)
    return b
print(b)
y()
print(b) # prints 500, then prints another 500, then runs the function and prints 300 and finally prints 500

b = 500
print(b)
def w():
    b = 300
    print(b)
    return b
print(b)
b = w()
print(b) # prints 500, prints 500, prints 300 and prints 300

def s():
    print(1)
    p()
    print(2)
def p():
    print(3)
s() # Prints 1,3 and the 2

def m():
    print(1)
    x = n()
    print(x)
    return 10
def n():
    print(3)
    return 5
y = m()
print(y) # prints 1,3,5 and then 10


