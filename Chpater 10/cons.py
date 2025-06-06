class info :
    Age = 19      # class Attribute
    lang = "Python" # class Attribute

    def __init__(self,name,Age,lang): #dunder method which is automatically called 
        self.name = name
        self.Age = Age
        self.lang = lang
        print("This is Information class")


    def getAge(self):
        print(f"Age of the user is {self.Age}")


    @staticmethod
    def GM ():
        print("Good Morning")

k = info("krth",20,"R")
print(k.name,k.Age,k.lang)

