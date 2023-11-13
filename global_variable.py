#one
#problems with local variable

x = "good"
def myfunc():
    x = "better"
    print("I am feeling " + x)
myfunc()
print("I am feeling " + x)

#two
x = "good"
def myfunc():
    global x
    x = "better"
    print("I am feeling " + x)
myfunc()
print("I am feeling " + x)
