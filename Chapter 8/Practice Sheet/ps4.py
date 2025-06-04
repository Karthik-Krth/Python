def sum(n) :
    if n == 1 or n== 0 :
        return n
    else :
        return  n + sum(n-1)
    
num = int(input("Enter a number : "))
print(f"Sum of first {num} Natural numbers is {sum(num)}")
