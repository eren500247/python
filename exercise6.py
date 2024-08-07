# Exercise 6
def triangle_star(u_input):
    for i in range(1,u_input+1):
        print("*"*i)
user_input = int(input("Enter the number you want : "))
triangle_star(user_input)

# for i in range(1,user_input+1):
#     print("*"*i)

# for i in range(1,user_input+1):
#     str_a = ""
#     for j in range(i): 
#         str_a += "*"
#     print(str_a)   

# for i in range(1,user_input+1):
#     for j in range(i):
#         print("*",end="")
#     print("\n")


# Exercise 5
# my_list = [1, 5, 2, 7, 8, 9, 200, 155]

# # user_input = int(input("Enter the Number : "))

# # for i in my_list:
# #     if i == user_input:
# #         print(f"Your Number {user_input} is found at index {my_list.index(i)}")

# # for x,y in enumerate(my_list):
# #     if user_input == y:
# #         print(f"Your Number {user_input} is found at index {x}")
# user_input =input("Enter the Number : ")
# try:
#     number = int(user_input)
#     if number in my_list:
#         index = my_list.index(number)
#         print(f"Your Number {number} is found at index {index}")
#     else:
#         print(f"Your Number {number} is not found in the list")
# except:
#     print("Plese Enter Invalid Number!")