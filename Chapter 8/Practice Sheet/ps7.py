def new_list(lst,r):
    return [i.strip() for i in lst if i.strip() != r]

lst = ["  apple ","  banana","grapes   ","orange  "]
r = "apple"
print(f"Updated list : {new_list(lst,r)}")
