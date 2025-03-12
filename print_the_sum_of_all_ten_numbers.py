#Ask the user to input ten numbers
number_list = [] #To store the numbers inputed by the user
for i in range(10):
    number_input = int(input(f"Input your number ({i + 1}): ")) #
    number_list.append(number_input) #To put the number inputed by the user to the list

#Print the sum of all the numbers
total_sum = sum(number_list)
print("Sum of all the numbers: ", total_sum)