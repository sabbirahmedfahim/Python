#factorial of n
#n! = n*n-1*n-2*n-3*...*1
#3! = 3*2*1 = 6
n = int(input("Enter the number for factorial: "))
factorial = 1
for i in range(1, n+1):
#for i in range(n, 0, -1):
    factorial = factorial*i
print(factorial)