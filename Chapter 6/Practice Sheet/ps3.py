spam = ["Make a lot of money", "buy now", "subscribe this", "click this"]


comment = input("Enter comment: ").lower()

# for i in spam :
#     if i in comment :
#         fnd = True
#         break

# if fnd :
#     print("Alert! This is a Spam Comment")
# else :
#     print("This comment is safe")

if any(i in comment for i in spam):
    print("Alert! This is a Spam Comment")
else:
    print("This comment is safe")



