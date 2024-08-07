list_quiz = [100, 30, 2, 15, -4, 3, 40, -9, 10]
#1
last_4  = list_quiz[-4:]
print(last_4)
#2
max_val = max(list_quiz)
print(max_val)
#3
sorted_list = sorted(list_quiz)
print(sorted_list)
#4
added_list = list_quiz + sorted_list
print(added_list)

#tuple exercise
tuple_exer = (1, 6, 4, 10, 2, 100, 4, "hi", 104.2, 4)
tuple_four_count = tuple_exer.count(4)
print(tuple_four_count)
