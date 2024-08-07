userInput = int(input("Enter Year : "))

if userInput % 4 == 0 :
    if userInput % 100 != 0 :
        print(f"{userInput} is a leap year")
    else :
        if userInput % 400 == 0 :
            print(f"{userInput} is a leap year") 
        else :
            print(f"{userInput} is not a leap year")
else : 
    print(f"{userInput} is not a leap year.")