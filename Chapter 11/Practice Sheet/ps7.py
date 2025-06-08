class String :
    def __init__(self,l):
        self.l = l

    
    def __len__(self):
        return len(self.l)


a = String([7,8,10,7,7])
print(len(a))
# print(len(a.l)) also prints length of the list