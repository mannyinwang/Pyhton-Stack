# # Biggie Size
# def bigSize (a):
#     list_length = len(a)
#     for i in range(list_length):
#         if a[i] > 0:
#             a[i] = "big"
#     return a
# print(bigSize([-1,3,5,-5]))

# # Count Positives
# def countPositive(a):
#     list_length = len(a)
#     count = 0
#     for i in range(list_length):
#         if a[i] >= 0:
#             count = count + 1
#     a[list_length -1] = count
#     return a
# print(countPositive([-1,1,1,1]))

# # Sum Total
# def sumTotal(a):
#     sum = 0
#     for i in range(len(a)):
#         sum = sum + a[i]
#     return sum
# print(sum([1,2,3,4]))

# # Average
# def averageNumber (a):
#     sum = 0
#     avg = 0
#     for i in range(len(a)):
#         sum = sum + a[i]
#     avg = sum/len(a)
#     return avg
# print(averageNumber([1,2,3,4]))

# # Length
# def lengthList(a):
#     count = 0
#     for i in a:
#         count = count + 1
#     return count
# print(lengthList([]))

# # Minimum
# def mini(a):
#     min = a[0]
#     for i in range(len(a)):
#         if a[i] < min:
#             min = a[i]
#     return min
# print(mini([5,2,6,3,4]))

# # Maximum
# def maxi(a):
#     max = a[0]
#     for i in range(len(a)):
#         if a[i] > max:
#             max = a[i]
#     return max
# print(maxi([5,2,6,3,4]))

# # Ultimate Analysis
# def ultimateAnalysis (a):
#     min = a[0]
#     max = a[0]
#     sum = 0
#     avg = 0
#     newBook = {}
#     for i in range(len(a)):
#         if a[i] > max:
#             max = a[i]
#         if a[i] < min:
#             min = a[i]
#         sum = sum + a[i]
#     avg = sum /len(a)
#     newBook = {"sumTotal":sum, "Average":avg, "Maximum":max, "Minimum":min, "Length":len(a)}
#     return newBook
# print(ultimateAnalysis([37,2,1,-9]))

# Reverse list
def reverseList(a):
    b = len(a)
    temp = a[0]
    for i in range(round(b/2)):
        a[i] = a[len(a)-1-i]
        a[len(a)-1-i] = temp
        temp = a[i+1]
    return a
print(reverseList([1,2,3,4,5,6,7]))


