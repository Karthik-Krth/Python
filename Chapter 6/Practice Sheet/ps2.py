s1 = int(input("Enter subject 1 marks : "))
s2 = int(input("Enter subject 2 marks : "))
s3 = int(input("Enter subject 3 marks : "))

total = s1+s1+s3

per = (total/3)

if s1>=33 and s2>=33 and s3 >= 33  and per >=40 :
    print("Congrats ! You Passes and your Percentage is ",per)
else :
    print("Sorry ! You failed , percentage : ",per)