#Ask the user to input ten numbers
number_list = []
for i in range(10): #To store the numbers inputed by the user
    number_input = int(input(f"Input your number({i + 1}): "))
    number_list.append(number_input) #To put the number inputed by the user to the list
#Print how many even numbers in ten numbers 