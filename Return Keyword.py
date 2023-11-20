#Return function
'''def sample(a, b):
    return a,b

x = int(input("Enter number x = "))
y = int(input("Enter number y = "))

ans = sample(x, y)
print(f"ans = {ans} and the type is = {type(ans)}")'''

def sample(a, b):
    return [a,b,7]

x = int(input("Enter number x = "))
y = int(input("Enter number y = "))

ans = sample(x, y)
p = [1]
print(f"ans = {ans} and the type is = {type(ans)}")
