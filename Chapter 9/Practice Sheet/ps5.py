cen_lst = ["shit","bad","bosdike","kuthhe"]

with open("censor_free.txt") as f :
    c = f.read().lower()

for i in cen_lst: 
    c = c.replace(i,"*"*len(i))
    
with open("censor_free.txt","w") as f :
    f.write(c)