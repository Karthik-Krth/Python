marks = []


sub = int(input(f"enter each sub marks : "))
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



# def get_grade(marks):
#     grade_map = {
#         range(90, 101): "Ex",
#         range(80, 90): "A",
#         range(70, 80): "B",
#         range(60, 70): "C",
#         range(50, 60): "D"
#     }
    
#     for r, grade in grade_map.items():
#         if int(marks) in r:
#             return grade
#     return "F"

# marks = float(input("Enter the marks: "))
# print("Grade:", get_grade(marks))
