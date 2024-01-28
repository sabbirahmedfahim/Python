n = int(input())
for i in range(0, n):
    id = input()
    if(id[4:7]=="115"):
        dept = "CSE"
    elif(id[4:7]=="141"):
        dept = "EEE"
    elif(id[4:7]=="116"):
        dept = "BBA"
    elif(id[4:7]=="117"):
        dept = "LLB"
    elif(id[4:7]=="114"):
        dept = "English"
    elif(id[4:7]=="111"):
        dept = "Economics"

    if(id[2]=="1"):
        sem = "Spring"
    elif(id[2]=="2"):
        sem = "Summer"
    elif(id[2]=="3"):
        sem = "Autumn"

    print(dept, sem, '20'+id[0:2])

# Azwad's Code
##



