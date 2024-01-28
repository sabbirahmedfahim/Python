#one
num1 = input("Enter number 1:")
num2 = input("Enter number 2:")

num1 = int(num1)
num2 = int(num2)

print(num1+num2

#two
#if elif else case
num1 = int(input("Enter number 1:"))
num2 = int(input("Enter number 2:"))

if num1> num2:
    print("num1 is greater than num2")
elif num1< num2:
    print("num1 is smaller than num2")
else:
    print("num1 is equal to num2")

#three
#think different
num1 = int(input("Enter number 1:"))
num2 = int(input("Enter number 2:"))

if num1> num2:
    print(f"{num1} is greater than {num2}")
elif num1< num2:
    print(f"{num1} is smaller than {num2}")
else:
    print(f"{num1} is equal to {num2}")

#four
#Now let, num2 = 0 and see the funny mistake :p
num1 = input("Enter number 1:")
num2 = input("Enter number 2:")

num1 = int(num1)
num2 = int(num2)

if num1> num2 and num2>0:
    print(f"{num1} is greater than {num2}")
elif num1< num2:
    print(f"{num1} is smaller than {num2}")
else:
    print(f"{num1} is equal to {num2}")

#five
#i really do not need to write extra two lines. here is shortcut
num1 = int(input("Enter number 1"))
num2 = int(input("Enter number 2"))
if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num2 > num1:
    print(f"{num2} is greater than {num1}")
else:
    print(f"{num2} is equal to {num1}")

#what if we could not use loop
print("1")
print("2")
print("3")

#six
#For loop
#If we do not specify a range, the value of 'i' starts at zero
for i in range (5):
    print(i)

#seven
#For loop
#do not forget to  give ':' sign after the range
for i in range (2,6,1):
    print(i)

#eight
#For loop
#in python, we cannot check the condition using = , instead, we use ==
#can 0 be an even number?
"""Zero is considered an even number in both mathematics and 
 using i % 2 == 0 to identify even numbers correctly includes zero."""

for i in range(20):
    if i%2==0:
        print(f"{i} is even")
#nine
#TASK
#odd and even
for i in range(20):
    if i%2==0:
        print(f"{i} is even")
    else:
        print (f"{i} is odd")