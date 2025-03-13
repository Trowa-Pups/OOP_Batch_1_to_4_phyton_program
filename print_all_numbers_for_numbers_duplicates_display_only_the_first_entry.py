#Ask the user to input ten numbers
number_list = [] #Create a list and have a system check if it has duplicates, and only display/print the first entry
duplicate_list = [] #To store the duplicates
for i in range(10):
    number = int(input(f"Input your number({i + 1}): "))
    if number in number_list: #To check if its a duplicate or not
        duplicate_list.append(number) #If it is a duplicate, it adds it in the duplicate list
    else:
        number_list.append(number) #If its not, it adds it in the number list

print(number_list) #Display/Print all the numbers and first entries