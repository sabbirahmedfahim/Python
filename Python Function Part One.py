#function
'''A function is a named code block that performs a job a value. functions divide a large job
or returns a value. functions divide a large job or returns smaller and more manageable parts'''

#use the def keyword to define a new function
#A function consists of definition and body
#there are lots of build-in functions in python. like print

def greet(): #function definition
    print("Hello buddy")

#function calling
greet()

#here part1 and part2 are parameters
def greet(part1, part2):
    print(f"Hello {part1} and good {part2}")
greet("John", "afternoon")
#here john and afternoon are arguments
greet("Mr y", "morning")

def summation(num1, num2, num3):
    sum = num1+num2+num3
    return sum
print(summation(4,5,3))
#print(sum)

def summation(num1, num2, num3):
    sum = num1+num2+num3
    return sum
ans = summation(4,5,3)
print(ans)
