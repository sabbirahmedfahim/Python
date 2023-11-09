#One
#most important part of the while loop is to set the increase\decrease value of i
#if we miss the part, it would be an infinite loop, so serious
#the job of break and continuaty kinda different between for and while loop
'''
i= 1
while i<=10:
    print(i)
    i = i+1
'''

#Two
#it will stop when it touchs break statement
'''
i= 1
while i<=10:
    print(i)
    if(i%2==0 and i%3==0):
        break
    i = i+1
'''
#Three

i= 1
while i<=10:
    print(i)
    if(i%2==0 and i%3==0):
        continue
    i = i+1
