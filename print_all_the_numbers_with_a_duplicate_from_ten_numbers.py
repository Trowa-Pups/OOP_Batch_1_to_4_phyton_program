#Ask the user to input ten numbers
number_list = [] #Create a list that has a system where it grabs a number in the list and check if its a duplicate of another number
for i in range(10):
    number = int(input(f"Input your number({i + 1}): "))
    number_list.append(number)

for check in number_list:
    if number_list.count(check) != 1: #To check if it is a duplicate
        print(check) #Print the numbers with duplicates