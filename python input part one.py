'''It takes input as string. We have to convert it according to our required date type'''

a = input("enter a number:")
print(type(a))

a = int(input("enter a number:"))
print(type(a))

#taking multiple inputs at a time
#i have to use space after inputing values***
a, b, c = input("Enter the number:").split()
print(a, b, c)
print(b)
print(int(a)-int(c))

