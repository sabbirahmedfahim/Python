# # FIND THE MISTAKE
# x = input()
# n = len(x)
# count = 0
# for i in range(0, n, 1):
#     if x[i]==A or x[i]==a or x[i]==E or x[i]==e or x[i]==I or x[i]==i or x[i]==O or x[i]==o or x[i]==U or x[i]==u:
#         count = count + 1
# print(count)


x = input()
n = len(x)
count = 0
for i in range(0, n, 1):
    if x[i]=='A' or x[i]=='a' or x[i]=='E' or x[i]=='e' \
            or x[i]=='I' or x[i]=='i' or x[i]=='O' or x[i]=='o' \
            or x[i]=='U' or x[i]=='u':
        count = count + 1
print(count)
