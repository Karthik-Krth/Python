marks = []

for i in range (1,4):
    sub = int(input(f"enter each sub {i} marks : "))
    marks.append(sub)

per = sum(marks)/3

if per >= 90:
    print("Grade is Ex")
elif per >= 80:
    print("Grade is A")
elif per >= 70:
    print("Grade is B")
elif per >= 60:
    print("Grade is C")
elif per >= 50:
    print("Grade is D")
else :
    print("Fail")
