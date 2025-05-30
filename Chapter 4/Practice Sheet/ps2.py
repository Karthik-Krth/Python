marks = []

for i in range(1,7):
    sub = int(input("enter marks of each student  : "))
    marks.append(sub)

marks.sort()
print(marks)