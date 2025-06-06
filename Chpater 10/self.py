class info :
    Age = 19      # class Attribute
    lang = "Python" # class Attribute
    def getAge(self):
        print(f"Age of the user is {self.Age}")
    @staticmethod
    def GM ():
        print("Good Morning")

k = info()
k.name = "Krth" 
k.Age = 22
# print(k.name,k.lang,k.Age)
k.GM()
k.getAge()  # same as  info.getAge(k) so it passes a agruement
