# nm = input("enter name : ")
# dt = input("enter date : ")
# print(f"Dear {nm} you're selected on {dt} ")

letter = '''
Dear <|Name|>, 
You are selected! 
<|Date|>
'''
print(letter.replace("<|Name|>","Krth").replace("<|Date|>","23 April 2025"))
