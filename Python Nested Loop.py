'''A nested loop refers to a loop within a loop, an inner loop within
the body of an outer one'''

'''for i in range(1,4):
    for j in range(1,4):
        print(f"i = {i} and j = {j}")
    print()'''
#after four rotation the value of j will be 4, consequently the code leave second while loop

i = 1
j = 1
while i<=3:
    while j<=3:
        print(f"i = {i} and j = {j}")
        j = j+1
    i = i+1
    print()
