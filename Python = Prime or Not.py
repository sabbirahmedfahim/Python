#Prime number
'''
A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
In other words, a prime number can only be divided evenly by 1 and itself.
For example, 2, 3, 5, 7, 11, 13, and 17 are all prime numbers.'''
#the code is not complex but tricky
'''flag = 0
a = int(input("Enter number n = "))
for i in range(2, a, 1):
    if (a%i==0):
        flag = 1
        print(f"{a} is not prime")
        break
    #else: not work here
if (flag==0):
    print(f"{a} is prime")'''

def prime(a):
    flag = 0
    for i in range(2, a, 1):
        if (a%i==0):
            flag = 1
            print(f"{a} is not prime")
            break
    if (flag==0):
      print(f"{a} is prime")
a = int(input("Enter number a = "))
prime(a)
