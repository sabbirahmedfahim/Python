k, s, b = map(int, input().split())
total = s+b
if(total%k==0 or total>k):
    print("YES")
else:
    print("NO")

#Azwad's code