#one
"""A String is a data  structure in Python that represents
a sequence of characters.
It is a immutable data type.
that means if we sum 8 and 8 as string the output will be
 88 rather than 16 because string in immutable
"""

#two
"""
msg = "It's a string
"""
'''here double-quotation  used because in our qoute we used  a 
single quatation and things could be messed up if we do not use
double quatation instead'''

#three
"""
msg = 'some examples : "ex1", "ex2" etc'
"""
#note that under the quotation the whole line is called as string

#four
"""
msg = 'It\'s a string'
"""
'''using backslash we can cope with same single quotation used inside
and outside of parenthesis'''

#five
#row string
"""
msg = r'c:\python\bin'
print(msg)
"""

#six
"""
msg = "Hello \
World"
print(msg)
"""

#seven
#creating multiple strings using triple
#single quotation
"""
msg = '''
        Hello
        Mr
        Code'''
print(msg)
"""

#eight
#format string
#run the code and search for mistakes :D
"""name = "john"
msg = "hello {name}"
print(msg)"""

#nine
#f stands for format string
"""name = "john"
msg = f"hello {name}"
print(msg)"""

#ten
#concatenating Python strings
"""msg = "Good " "Morning"
print(msg)"""


#eleven
#concatenating Python strings
#used a space after words except last word
"""msg = "Good " + "Morning " + "Sabbir"
print(msg)"""

#twelve
#accessing string elements
#think :D
"""
str = "Python String"
print(str[0]) #P
print(str[2]) #t
print(str[-2]) #n
"""

#getting the length of a string
"""
str = "Hello"
print(len(str))
"""

#getting the length of a string
#even it will count the space inside the braket
"""str = "Hello "
print(len(str))"""

#thirteen
#Slicing strings
#remember the ratio how works
"""str = "Python String"
print(str[1:3])"""

#Slicing strings
#remember the ratio how works. interesting
"""str = "Python String"
print(str[1:-3])"""

#fourteen
#Python strings are immutable
"""In Python, strings are immutable, 
meaning their contents cannot be changed directly; 
instead, operations on strings create new string objects."""

"""str = "Python"
str[0] = 'J'"""
#we cannot do it. their contents cannot be changed directly

#instead, operations on strings create new string objects.
#remember i used third braket after str 107th line
str = "Python"
#str[0] = 'J'
str1 = 'J' + str[1:6]
print(str1)