#Ask the user to input ten numbers
number_list = [] #To store numbers inputed by the user
for i in range(10):
    number_input = int(input(f"Input your number({i + 1}): "))
    number_list.append(number_input) #To put the number inputed by the user to the list

#Print all the even numbers from ten numbers
for number in number_list: #To grab a number in the list
    if number % == 0: #To check if it is even
        print(number)