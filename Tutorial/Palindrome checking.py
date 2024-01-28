#Palindrome checking
'''If the reversed number is the same as the original
number, then the number is a palindrome'''
# 1001
# 1001
# noon

#One
st = input("st = ")
n = len(st)

rev_st = st[::-1]
if(st==rev_st):
    print("Palindrome")
else:
    print("Not Palindrome")

#Two
st = input("st = ")
n = len(st)
flag = 0

for i in range(0, int(n/2), 1):
    if(st[i]!=st[n-i-1]):
        flag = 1
        print("Not Palindrome")
        break
if(flag==0):
    print("Palindrome")