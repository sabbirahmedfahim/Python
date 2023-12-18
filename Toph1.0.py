# Divisors
# A = int(input('enter: '))
#
# for i in range(1, A+1, 1):
#     if(A%i==0):
#         print(i)

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

def meow(a, b):
    return b, a
x = int(input("Enter x: "))
y = int(input("Enter y: "))
twitter = meow(x, y)
print(twitter)