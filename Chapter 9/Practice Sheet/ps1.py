with open("poems.txt") as f:
    c = f.read()
    if "twinkle" in c :
        print("Twinkle is present in poems file")
    else :
        print("Twinkle is not present in poems file")