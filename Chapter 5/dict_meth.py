marks = {
    "krth" : 100 ,
    "raju" : 78 ,
    "harun" : 96
}

# print(marks,type(marks))
print(marks.items())
print(marks.keys())
print(marks.values())

marks.update({"raju":85 , "madhav" : 92})
print(marks.items())
print(marks.get("krth"))

