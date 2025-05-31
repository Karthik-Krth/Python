nm = {1,5,7,9,5,1,9,6, "krth"}
m = {3,89,9,98,8}

e = set() #sets are unordered
print(type(nm))
print(type(e))
print(nm)
nm.add(78)
print(nm)
nm.remove(5)
print(nm)
nm.pop()
print(nm)
print(nm.union(m))
print(nm.intersection(m))
print(nm-m)
# print(nm+m) # not possible in Sets