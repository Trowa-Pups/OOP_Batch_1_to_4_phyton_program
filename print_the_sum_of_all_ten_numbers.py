#Ask the user to input ten numbers
numbers = [] #To store the numbers inputed by the user
for i in range(10):
    number_input = int(input(f"Input your number ({i + 1}): "))
    numbers.append(number_input)

#Print the sum of all the numbers