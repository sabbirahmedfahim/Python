list = [1, 1, 3, 5, 84]
list1 = [1,2]
list2 = [2,1]
#here list1!=list2

list = [1, 1, 3, 5, 84]

for i in list:
    print(i)

list = [1, 1, 3, 5, 84]
n = len(list)
for i in range(0, n, 1):
    #print(i) is wrong process
    print(list[i])

#using negative index
list = [1, 1, 3, 5, 84]
n = len(list)
for i in range(n-1, -1, -1):
    #print(i) is wrong process
    print(list[i])

