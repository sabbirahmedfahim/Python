# Divisors
# A = int(input('enter: '))
#
# for i in range(1, A+1, 1):
#     if(A%i==0):
#         print(i)
import keyword

#How many X
# A = input()
# print(len(A))

#How many X
#error code
# st = input("Meow: ")
# i = 0
# count = 0
#
# while True:
#     if(st[i]>='a' and st[i]<='z') or (st[i]>='A' and st[i]<='Z'):
#         count = count + 1
#     else:
#         break
#     i = i + 1
# print(count)

#error
# A = input()
# count = 0
# for i in range(A):
#     if(A=='\0'):
#         break
#     else:
#         count = count + 1
# print(count)

# N = int(input())
# A = map(int, input().split())
# n = len(A)
# maxx = A[0]
# for i in range(n):
#     if (A[i]>maxx):
#         maxx = A[i]
# print(maxx)

# bangladesh = int(input('Total run of Bangladesh: '))
# new_zealand = int(input('Total run of New Zealand: '))
# if bangladesh>new_zealand:
#     print(f"bangladesh wins and their total run is {bangladesh}")
# elif bangladesh==new_zealand:
#     print("match draw")
# else:
#     print(f"new_zealand win and their total run is {new_zealand}")
# print(f"bangladesh and new zealand together achieved {bangladesh+new_zealand} runs")


# Headline => import keyword
#
# msg = 'It\'s a string'
# print("msg")

# mew = 'Python'
# Mew = 'J'
# Hew = mew[1:6]
# print(f'{Mew}'+ f'{Hew}')


# for i in range(4, 15, 1):
#     if i%2==0:
#         print(f'{i} is even')
#     else:
#         print(f"{i} is odd")


# list = [3, 5, 4, 45, -56]
# n = len(list)
#
# for i in range(0, n, 1):
#     if list[i]%2!=0:
#         continue
#     else:
#         print(f"list {list}")

# def friends(friend1, friend2):
#     LJLJ = f"Hi {friend1}, you are selected"
#     ljlj = f"Hey {friend2}, sorry, best of luck"
#     print(LJLJ)
#     print(ljlj)
#
# friends("Rahim", "Karim")


# def greet(): #function definition
#     print("Hello buddy")
#
# #function calling
# greet()


# def summation(num1, num2, num3):
#     return num1+num2+num3
#
# print(summation(3,4,5))


# i = 1
# for i in range(1, 11, 1):
#     print(i)
#     if(i>7):
#         break



# for i in range(1, 13, 1):
#     if (i==5 or i==12):
#        continue
#     print(i)

# for i in range(1, 11, 1):
#     if(i>7):
#         break
#     print(i)
# #only changed the position of break keyword :D


# for i in range(1, 13, 1):
#     print(i)
#     if (i==5 or i==12):
#        continue
# #easy?



# lisr = [4, 5, 65, 6, 56]
# n = len(list)
# for i in range(0, n, 1):
#     if(list%2!=0):
#         break
#     print(f"{lisr} is even")


# for i in range(1, 11, 1):
#     if (i%2==0 and i%3==0):
#         continue
#     print(i)


# sum = 0
# for i in range(1,8,1):
#     sum = sum+i
#     if(sum>17):
#         print(sum)

# sum = 0
# for i in range(1,8,1):
#     sum = sum+i
#     print(sum)
#     if(sum>17):
#         break



# i = 0
# for i in range(1,8,1):
#     if(sum>17):
#         break
#     sum = sum + i
# print(sum)


# list = [3, 43, 3,5, 53]
# n = len(list)
# sum = 0
# for i in range(0, n, 1):
#     sum = sum + list[i]
# print(sum)


# i = 10
# while i<=10:
#     print(i)
#     i = i - 2


# i= 1
# while i<=10:
#     print(i)
#     if(i%2==0 and i%3==0):
#         break
#     i = i+1


# i= 1
# while i<=10:
#     print(i)
#     if(i%2==0 and i%3==0):
#         continue
#     i = i+1


# for i in range(1,4):
#     for j in range(1,4):
#         print(f"i = {i} and j = {j}")


# i = 1
# j = 1
# while i<=3:
#     while j<=3:
#         print(f"i = {i} and j = {j}")
#         j = j+1
#     i = i+1
#     print(f"i = {i} and j = {j}")


# def sample(a, b):
#     return a,b
#
# x = int(input("Enter number x = "))
# y = int(input("Enter number y = "))
#
# ans = sample(x, y)
# print(f"answer = {ans} and the type is = {type(ans)}")


# def numbers(A, B):
#     return x, y, 6
# x = int(input("Enter A: "))
# y = int(input("Enter B: "))
# realGame = numbers(x, y)
# print(realGame)

# def meow(a, b):
#     return b, a
# x = int(input("Enter x: "))
# y = int(input("Enter y: "))
# twitter = meow(x, y)
# print(twitter)


# numbers = [43, 67, 7, 78, 34, 66, 31]
# numbers.remove(34)
# print(numbers)


# 1! = 1x1 = 1
# 0! = 1
#    n! = n(n-1)(n-2)!
# => 2! = 2(2-1)(2-2)!
# => 2! = 2x0!
# 3! = 1x2x3 = 6
# 5! = 1x2x3x4x5 = 120
#
# n = n(n-1)! #sutro
# 1 = 1(1-1)!
# 1 = 1(0!)


# n = int(input("Enter the number for factorial: "))
# factorial = 1
# for i in range(1, n+1):
# #for i in range(n, 0, -1):
#     factorial = factorial*i
# print(factorial)


# n = int(input("Enter the number: "))
# flag = 0
# for i in range(2, n, 1):
#     if n%i==0:
#         flag = 1
#         print(f"{n} is not a Prime Number")
#         break
# if flag==0:
#     print(f"{n} is Prime Number")


#list of divisors
# divisors = []
# n = int(input("Enter the number for divisors: "))
# for i in range(1, n+1, 1):
#     if (n%i==0):
#         divisors.append(i)
# print(f"Divisors = {divisors}")


# st = input("Enter the number/word: ")
# rev_st = st[::-1]
#
# if(st==rev_st):
#         print(f"{st} is Palindrome")
# else:
#         print(f"{st} is not Palindrome")


# st = input("Meow: ")
# revSt = st[::-1]
# print(revSt)

# a = 3
# print(a**4)

# watermelon = int(input())
#
# if watermelon%2==0 and watermelon>2:
#         print("YES")
# else:
#         print("NO")




# number = int(input())
# number = number - 2
# print(number)

# wa = int(input())
# if(wa%2==0 and wa!=2):
#     print("YES")
# else:
#     print("NO")


# n = int(input())
# for i in range(0, n):
#     id = input()
#
#     if(id[4:7]=="115")
#         print('CSE')


# k, s, b = map(int, input().split())
# totall = s+b
#
# if(totall%k==0 and totall>k):
#     print("YES")
# else:
#     print("NO")


# A = int(input())
# B = int(input())
# print(A+B)


# A, B = map(int, input().split())
# print(A+B)

# def X(a, b):
#     return a+b
# Y = map(X, ('apple', 'banana', 'orange'), ('lemon, pineapple'))
#
# # print(Y)
# print(list(Y))

# A, B = map(int, input().split())
# sum = A + B
# print(sum)


# A = int(input())
# n = len(A)
# for i in range(0, n):
#     if A



# A = int(input())
#
# for i in range(1, A+1):
#     if A%i==0:
#         print(i)

# 1, 1, 2, 3, 5, 8, 13
# N = int(input())
# fibonacchi1 = 1
# fibonacchi2 = 1
# fibonacchiN =


# n = int(input())
# factorial = 1
# for i in range(1, n+1):
#     if n!=factorial:
#         factorial = (factorial*i) % 10000
# print(factorial)


# Input
# N = int(input())
#
# # Calculate the factorial and keep only the last 4 digits
# factorial = 1
# for i in range(1, N + 1):
#     factorial = (factorial * i) % 10000  # Keep only the last 4 digits
#
# # Print the last 4 digits of N!
# print(result)


# A = int(input())
# for i in range(0, T):
#     S = input()
#     n = len(A)
#     if A%


# A = input()
# n = len(A)
# count = 0
# for i in range(0, n):
#
#     count = 1 + i
# print(count)


# A = int(input())
# divisors = []
# n = len(A)
# for i in range(0, n):
#     divisors.append(i)
# print(maxx)

# list = [23, 34, 34, 2, 43, 4]
# n = len(list)
# maxx = list[0]
# for i in range(0, n):
#     if (maxx<list[i]):
#         maxx = list[i]
# print(f"maxima is {maxx}")