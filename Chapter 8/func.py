def fact(n) :
    if n== 0 or n==1 :
        return 1
    else :
        return n*fact(n-1)
    
num = int(input("Enter a number for factorial : "))

print(f"Factorial of {num} is {fact(num)}")
