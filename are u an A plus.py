# n = int(input())
# count = 0
# for i in range(0, n):
#     marks = list(map(int, input().split()))
#     if 80<= marks[i] <=100:
#         count = count + 1
# print(count)

#it is a Quiz
n = int(input())
count = 0
marks = list(map(int, input().split()))
for i in range(0, n):
        if marks[i]>79 and marks[i]<101:
            count = count + 1
print(count)

# bangla = int(input("Bangla: "))
# if bangla>=80 and bangla<=100:
#     print("banglay A+")
# elif bangla>=70 and bangla<=79:
#     print("banglay A")
# english = int(input("English: "))
# if english>=80 and english<=100:
#     print("english A+")
# elif english>=70 and english<=79:
#     print("English A")


