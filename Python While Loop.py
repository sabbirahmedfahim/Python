#One
'''most important part of the while loop is to set the increase/decrease value of i
*if we miss the part, it would be an infinite loop, so serious
*the job of break and continuity kinda different between 'while and for loop'
***we have to give the initial value in while loop
'''
i= 1
while i<=10:
    print(i)
    i = i+1

#two
i = 10
while i<=10:
    print(i)
    i = i - 2

#three
i = 10
while i>=0:
    print(i)
    i = i - 2

#four
#the loop will stop when it touches break statement
#6 is printed because print function is before the condition
i= 1
while i<=10:
    print(i)
    if(i%2==0 and i%3==0):
        break
    i = i+1

#five
#it shows the continuation of while loop
'''when the loop touches continue keyword it will come back to loop. 
there are no way to increase/decrease the value of i. So it will be an infinity loop'''
i= 1
while i<=10:
    print(i)
    if(i%2==0 and i%3==0):
        continue
    i = i+1
