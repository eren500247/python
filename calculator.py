class CalculateNum:
    def addition(self,num1,num2):
        result = num1 + num2
        print(f"The Result is {result}")
    
    def subtraction(self,num1,num2):
        result = num1 - num2
        print(f"The Result is {result}")

    def multiplication(self,num1,num2):
        result = num1 * num2
        print(f"The Result is {result}")
    
    def division(self,num1,num2):
        result = num1 / num2
        print(f"The Result is {result}") 
print("Welcome To The Python Calculator")

while True:
    c = CalculateNum()
    try:
        first_number = int(input("Enter the number : "))
        second_number = int(input("Enter the number : "))
        operator = input("Enter the Operator(+,-,*,/) : ")

        if operator == "+":
            c.addition(first_number,second_number)
        elif operator == "-":
            c.subtraction(first_number,second_number)
        elif operator == "*":
            c.multiplication(first_number,second_number)
        elif operator == "/":
            c.division(first_number,second_number)
        else:
            print("Please Enter Valid Operator (+,-,*,/)")

        print("Do you Want to Calculate Again")
        u_input = str(input("Enter (yes/no) : "))
        if u_input == "no" :
            print("Thanks You")
            print("Bye Bye!")
            break
        else:
            print("Let's play again")
    except:
        print("Enter the invalid number,Thanks")
        break


    
    
    


