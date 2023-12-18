#taking input using loop and store it in container i.e list
list = []

for i in range(5):
    list.append(input("Enter the elements:"))
print(list)

#print(list)
list = []
for i in range(5):
    list.append(input("Enter number: "))
for i in range(5):
    print(f"Output is {list[i]}")