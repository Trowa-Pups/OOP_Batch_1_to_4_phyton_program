#Ask the user to input ten numbers
number_list = [] #To store the numbers inputed by the user
even_counter = 0
for i in range(10): #To store the numbers inputed by the user
    number_input = int(input(f"Input your number({i + 1}): "))
    number_list.append(number_input) #To put the number inputed by the user to the list

#Print how many even numbers in ten numbers 
for number in number_list: #To grab a number in the list
    if number % 2 == 0: #To check if the number is even
        even_counter += 1 #To add to the counter

print("They are", even_counter, "even numbers")