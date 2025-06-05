with open("this.txt") as f :
    c = f.read()
with open("this_copy.txt","w") as f :
   f.write(c)
