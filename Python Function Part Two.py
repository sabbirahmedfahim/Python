#finding the length of string
'''st = "Hello"
print(len(st))'''

'''
Understanding null character
st[0] = "H"
st[1] = "e"
st[2] = "l"
st[3] = "l"
st[4] = "0"
st[5] = "\0" #null character
"hello john" #space is not a null character.'''

def length(s):
    count = 0
    for i in s:
        if (i=='\0'):
            break
        else:
            count = count + 1
    return count
ans = length('Hello World')
print(ans)
def length(s):
    count = 0
    for i in s:
        if (i=='\0'):
            break
        else:
            count = count + 1
    return count
ans = length('Hello World')
print(f"The length of string is {ans}")
