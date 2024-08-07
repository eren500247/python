num1 = int(input("Enter the number 1 : "))
num2 = int(input("Enter the number 2 : "))
num3 = int(input("Enter the number 3 : "))

total = num1 + num2 + num3

if num1 == num2 == num3:
    result = total * 3
    print("The 3x result is ",result)
else:
    print("The total result is ",total)

