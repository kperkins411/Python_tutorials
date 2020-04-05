s="a toasted bean"
for c in s:
    print(f"-{c}-")
# Python program to rotate an array by 'd' elements.

def rotate(arr, d):
    return arr[d:] + arr[:d]

arr = [1, 2, 3, 4, 5, 6, 7, 8]
arr = rotate(arr, 3)
print(arr)
# prints [3 ,4, 5, 6, 7, 8, 1, 2]


a=['a','b','c','d','e','f','g','h']
b=a
d=a[:]

assert d==a and d is not a  #no assert
# assert b==a and b is not a  #will assert

assert b==a

for i,j in enumerate(range(20)):
    print(f"i is {i},j is {j}")

c=a[:5]
c[1]='q'
b[1]='z'
pass