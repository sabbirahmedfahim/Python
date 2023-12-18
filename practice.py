#One
#apply_twice
'''def apply_twice(func, arg):
    return func(func(arg))
def add_five(x):
    return x + 5
print(apply_twice(add_five, 10))'''

#two
#Quiz
'''def testyz(func, arg):
    return func(func(arg))

def mult(x):
    return x*x

print(testyz(mult, 2))'''

'''def zoom(x, y):
    temp = x+2*y
    return temp/(2*x+y)
uuu = zoom(5,10)
print(uuu)'''

#Three
#lambda
'''def manush(good, okey):
    return good(okey)

h = manush(lambda x: 2*x*x, 5)
print(h)'''

#Four
#lambda
'''def manush(ami):
    return lambda x: 2*x*ami
output = manush(2)
print(output(3))'''

#Five
#lambdas
'''def my(x):
    return lambda y: y**2 + 5*x + 4
zvari = my(1)
print(zvari(2))'''

'''a = ( lambda x : x*x) (8)
print(a)'''

#Six
#map
'''def lol(x):
    return x+5
nums = [11, 23, 35, 24, 46, 45]
result = list(map(lol, nums))
print(result)'''

'''nums = [11, 23, 35, 24, 46, 45]

result = list(map(lambda x: x+5, nums)'''

#Seven
#filter
'''nums = [11, 23, 35, 24, 46, 45]
hmmm = list(filter(lambda x: x%2==0, nums))
print(hmmm)'''

A = int(input())
for i in range(1, A):
    if(A%i==0):
        print(i)