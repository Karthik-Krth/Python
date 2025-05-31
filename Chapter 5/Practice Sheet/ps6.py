d = {}

for i in range (1,5):
    nm = input("Enter name of the student : ")
    favlang = input("Enter your  favorite language : ")
    d.update({nm : favlang})
print(d)