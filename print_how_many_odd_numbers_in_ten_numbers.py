#Ask the user to input ten numbers
number_list = []
oddnumber_counter = 0 #Counter for how many odd numbers in the list

for i in range(10): #To store the numbers inputed by the user
    number_input = int(input(f"Input your number({i + 1}): "))
    number_list.append(number_input) #To put the number inputed by the user to the list

#Print how many are odd numbers in the ten numbers
for number in number_list: #To grab a number in the list
    if number % 2 != 0: #To check if its an odd
        oddnumber_counter += 1 #To add to the counter

print("They are", oddnumber_counter, "odd numbers")