#one
#kinda tricky codes
'''
sum = 0

for i in range(1,5):
    sum = sum + i
    print(sum)
'''

#two
#summation of 1 to 100
#why only last sum was printed?
#because print function violates identation. so it will print the last sum

sum = 0

for i in range(1,101):
    sum = sum + i
    #print(sum)
print(f"sum is equal to {sum}")