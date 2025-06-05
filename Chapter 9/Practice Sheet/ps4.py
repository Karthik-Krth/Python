with open("donkey.txt","r") as f :
    c = f.read().lower()
    
l = c.replace("donkey","######")
        
with open("donkey.txt","w") as f :
    f.write(l)