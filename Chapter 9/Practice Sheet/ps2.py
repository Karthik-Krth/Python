import random

def game( ):
    print("You are playing the game ")
    #Fetching the hi score from the file 
    with open("hi_score.txt") as f :
        hi_sc = f.read()
    if hi_sc != "":
        hi_sc = int(hi_sc)  #as txt in fil with in str so we changed it to int
    else :
        hi_sc = 0

    sc = random.randint(1,99)
    print(f"Your Score : {sc}")
    if (sc > hi_sc ) :
        #Write the hi_Sc into the file 
        with open("hi_score.txt","w") as fl :
            fl.write(str(sc)) #as file only stotes txt we converted int into str
    

game()
        
