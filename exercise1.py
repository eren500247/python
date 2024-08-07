print("Welcome To Our Letter Counter Mini Projects")

msg = input("Enter Message :")
letter = input("Enter Letter :")
counter = msg.count(letter)
print("This letter occured ", counter , "times")
percantage = counter / len(msg) * 100
print("The percentage of the letter in the message is ",percantage)