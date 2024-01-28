n = int(input())
numbers = list(map(int, input().split())) #i have to understand the line
maxx = numbers[0]
for i in range(0, n):
    if (maxx<numbers[i]):
        maxx = numbers[i]
print(maxx)


