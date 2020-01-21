# Print 1-255
# print1To255()
# Print all the integers from 1 to 255.

def printintegers():
    for i in range(256):
        print(i)

printintegers()


# Print Ints and Sum 0-255

def sumofintegers():
    sum =0
    for i in range (256):
        sum = sum + i
        print(i)
    return sum

print(sumofintegers())




# PrintIntsAndSum0To255()
# Print integers from 0 to 255, and with each integer print the sum so far.

def sumofintegers():
    sum =0
    for i in range (256):
        sum = sum + i
        print(i)
        print(sum)

print(sumofintegers())




# Find and Print Max
# printMaxOfList(lst)
# Given an list, find and print its largest element.

def maxoflist(x):
    y = len(x)
    max = x[0]
    for i in range(0,y,1):
        if x[i] > max:
            max = x[i]
    return max

print(maxoflist([-1,-33,-5,-6,-99,-101]))




# List with Odds
# returnOddsList1To255()
# Create an list with all the odd integers between 1 and 255 (inclusive).
#
def createoddlist():
    list1 = []
    for i in range (256):
        if i%2!=0:
            list1.append(i)
    return list1

print(createoddlist())




# Greater than Y
# ReturnListCountGreaterThanY(lst, y)
# Given an list and a value Y, count and print the number of list values greater than Y.

def greaterY(list,y):
    z = len(list)
    count = 0
    for i in range(z):
     if list[i] > y:
          print list[i]
          count = count + 1
          print(count)

greaterY([-1,33,25,-6,-99,-101],23)


# Max, Min, Average
# PrintMaxMinAverageListVals(lst)
# Given an list, print the max, min and average values for that list.

def greaterY(x):
    z = len(x)
    sum = 0
    max = x[0]
    min = x[0]
    for i in range (z):
        sum = sum + x[i]
        if x[i] > max:
            max = x[i]
        if x[i] < min:
            min = x[i]
    avg = float(sum)/z
    print(max)
    print(min)
    print (avg)

greaterY([1,2,4,3,5,3])



# Swap String For List Negative Values
# SwapStringForListNegativeVals(lst)
# Given an list of numbers, replace any negative values with the string 'Dojo'.


def replacelist(x):
    y = len(x)
    for i in range (y):
        if x[i] < 0:
            x[i] = 'Dojo'
    return x
print(replacelist([-1,33,25,-6,-99,-101]))



# Print Odds 1-255
# PrintOdds1To255()
# Print all odd integers from 1 to 255.

def printodd():
    for i in range (256):
        if i%2!=0:
            print i
printodd()

# Iterate and Print List
# PrintListVals(lst)
# Iterate through a given list, printing each value.

def printlist(x):
    y = len(x)
    for i in range(y):
        print x[i]

printlist([1,2,4,6,9])

# Get and Print Average
# PrintAverageOfList(lst)
# Analyze an Lists values and print the average.
# Square the Values
# SquareListVals(lst)
# Square each value in a given list, returning that same list with changed values.

def squarelistvals(x):
    y = len(x)
    for i in range(y):
        x[i] = x[i] * x[i]
    print x

print (squarelistvals([1,2,4,6,9]))

# Zero Out Negative Numbers
# ZeroOutListNegativeVals(lst)
# Return the given list, after setting any negative values to zero.

def replacezero(x):
    y = len(x)
    for i in range (y):
        if x[i] < 0:
            x[i] = 0
    return x
print(replacezero([-1,33,25,-6,-99,-101]))

# Shift List Values
# ShiftListValsLeft(lst)
# Given an list, move all values forward (to the left) by one index, dropping the first value and leaving a 0 (zero) value at the end of the list.


def shiftleft(x):
    y = len(x)-1
    for i in range(y):
        x[i] = x[i+1]
    x[y]  = 0
    print (x)

print (shiftleft([1,2,3,4]))
