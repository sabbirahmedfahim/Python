#swap function
'''
a = int(input("Enter number a: "))
b = int(input("Enter number b: "))

a = b
b = a
print(a,b) #so the method is not works
'''

'''a = int(input("Enter number a: "))
b = int(input("Enter number b: "))

temp = a
a = b
b = temp
print(a,b)

#what if we do swaping using function'''
def swap(x, y):
    temp = x
    x = y
    y = temp
    return x, y

a = int(input("Enter number a= "))
b = int(input("Enter number b= "))
a, b = swap(a, b)

print(a,b)

#easy method
def swap(x, y):
    x,y = y, x
    return x, y

a = int(input("Enter number a= "))
b = int(input("Enter number b= "))
ans = swap(a, b)

print(ans)

