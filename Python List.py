'''A list is an *ordered* collection of items.
Python uses the square brackets [] to indicate a list'''
#python list is ordered so can simply store marks, wishlist, data's that doesn't messed up like sets

'''list = [] #empty list
numbers = [12, 'green' ,345, 5, 4]'''

#use can use string, float, integer at the same list

#coordinates explained
'''coordinates = [[1,2], [4,32], [56,3], [4,6]]
print(coordinates)'''

#how to access in list
'''coordinates = [[1,2], [4,32], [56,3], [4,6]]
print(coordinates[2])'''

#how to access inside of coordinates in list
#keep in mind index of list starts with 0
#negative index starts from 1
'''coordinates = [[1,2], [4,32], [56,3], [4,6,9]]
print(coordinates[2][1])
print(coordinates[-1][2])'''

#modifying elements in a list

'''numbers = [2, 3, 43, 4, 3]
numbers[0] = 5
numbers[2] = 'Hello'
numbers[1] = numbers[1] + 2

print(numbers)'''

#adding elements to the list
#The append() method appends an element to the end of a list.
#The insert() method adds a new element at ANY POSITION in the list


'''numbers = [1, 2, 3, 4, 5]
numbers.append(50)
numbers.append(60)
print(numbers)'''


'''numbers = [1, 5, 7, 4, 3]
numbers.insert(2, 50)
numbers.insert(5, 60)
print(numbers)'''

# removing elements from a list
#del follows index to remove any elements from list
'''numbers = [2, 5, 6, 4, 8]
del numbers[0]
print(numbers)'''

#pop function removes the last element from the list
numbers = [2, 5, 6, 4, 8]
numbers.pop()
numbers.pop()
print(numbers)

#in remove function we will not input the index, mention the element from the list!
numbers = [2, 5, 6, 4, 8]
numbers.remove(8)
print(numbers)

