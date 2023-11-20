
def main ():
    i=10
    if(i<5):
        print(i)
"""
import keyword
#Comment
#In PyCharm, and in Python in general,
# you can write comments using either the # symbol for single-line comments
# or triple double-quotes for multi-line comments (also known as docstrings).
"""
"""
This is a multi-line comment or docstring.
It can span multiple lines and is typically used
to document code elements like functions, classes, and modules.
"""
a=3
b=6
c=23
if(a==3 and b==6 and \
        c==23):
#i moved c==3 to the next line using backslash '\'
    print(a+b)

#python keyword
#some word have special meaning in python. They are called keyword
print(keyword.kwlist)
