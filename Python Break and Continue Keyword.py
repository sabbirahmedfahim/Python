#One
#see how it  works easily
'''
for i in range(1, 11, 2):
    print(i)
'''

#Two
#here break is mainly under the if statement. i am not saying that it is crossed for loop
#it is the game of true or false, for explanation see Three
'''num = 8
for i in range(1, 11, 1):
    if(i>8):
        break
    print(i)
'''

#Three
#the code shows that why identation is important
#it also tells us the story why the output is stopped in 9
'''i = 1
for i in range(1, 11, 1):
    print(i)
    if(i>8):
        break
'''

#Four
#the continuation mentioned here, is not for lines, it is the continuation of the loop!
'''
i = 1
for i in range(1, 11, 1):
    if(i==4):
        continue
    print(i)
'''

#Five
#using if and continue statement in for loop to find even numbers
'''
i = 1
for i in range(1, 11, 1):
    if(i%2==1):
        continue
    print(i)
'''

#Six
#think different
#we used and operator :) try using or
'''
i = 1
for i in range(1, 11, 1):
    if(i%3==0 and i%2==0):
        continue
    print(i)
'''
#Seven
#Quiz
sum = 0
for i in range (1, 7, 1):
    sum = sum + i

    #print(sum)
    if(sum>17):
        break
print(sum)
