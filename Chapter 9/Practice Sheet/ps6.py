with open("log.txt") as f :
    c = f.read().lower()

if "python" in c :
    print("The log mine Contains the word 'python'")
else :
    print("The log mine doesn't Contains the word 'python")