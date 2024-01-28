#finding divisors
n = int(input("Enter number = "))

for i in range(1, n+1, 1):
    if(n%i==0):
        print(i)
import math

#divisors in list
divisors = []
n = int(input("Enter number = "))

for i in range(1, n+1, 1):
    if(n%i==0):
        divisors.append(i)
print(f"divisors = {divisors}")

#sqrt
divisors = []
n = int(input("Enter number = "))
s_n = int(math.sqrt(n))
for i in range(1, s_n+1, 1):
    if(n%i==0):
        divisors.append(i)
        divisors.append(int(n/i))
print(f"divisors = {divisors}")


