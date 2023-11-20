#Finging maximum number
'''list = [5, 6, 10, 8, -9]
n = len(list)
maxx = list[0]

for i in range(0, n, 1):
    if (maxx<list[i]):
        maxx = list[i]

print(f"maxx number is {maxx}")'''

#Finging minimum number
'''list = [5, 6, 10, 8, -9]
n = len(list)
minn = list[0]

for i in range(0, n, 1):
    if (minn>list[i]):
        minn = list[i]

print(f"minn number is {minn}")'''

#TASK1
#function
def maxx(n):
    n = len(list)
    maxx = list[0]
    for i in range(0, n, 1):
        if (maxx < list[i]):
            maxx = list[i]
    return maxx
list = [5, 6, -10, 8, -9]
maxx = maxx(list)
print(f"maximum number is {maxx}")

#TASK2
#function
def minn(n):
    n = len(list)
    minn = list[0]
    for i in range(0, n, 1):
        if (minn > list[i]):
            minn = list[i]
    return minn
list = [5, 6, -10, 8, -9]
minn = minn(list)
print(f"minimum number is {minn}")

