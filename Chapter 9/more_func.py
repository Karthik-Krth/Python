f = open("file.txt")
# lns = f.readlines()
# print(lns,type(lns))

# l1 = f.readline()  #line 1
# print(l1,type(l1))
# l1 = f.readline()  #line 2
# print(l1,type(l1))
# l1 = f.readline()  #line 3
# print(l1,type(l1))
# l1 = f.readline()  #line 4
# print(l1,type(l1))
# l1 = f.readline()  #line 5
# print(l1,type(l1),l1=="")

l = f.readline()
while l != "" :
    print(l)
    l = f.readline()

f.close()