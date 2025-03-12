#Ask the user to input ten numbers
number1 = int(input("Input your number(1): "))
number_list = []
for remaining_numbers in range(9):
    number_input = int(input(f"Input your number({remaining_numbers + 2}): "))
    number_list.append(number_input)
#Print the result of the first number minus all of the remaining numbers