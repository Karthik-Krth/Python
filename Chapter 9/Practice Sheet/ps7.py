
with open("log.txt") as f :
    lines = f.readlines()

found = False
lineno = 1
for line in lines :
    if "python" in line.lower() :
        print(f"The log mine Contains the word 'python' at line {lineno}")
        found = True
        break
    lineno += 1
    
if not found :
    print(f"The log mine doesn't Contains the word 'python'")