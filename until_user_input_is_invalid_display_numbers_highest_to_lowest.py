#Ask the user to input numbers until they inputed an invalid input
number_list = []
current_number = 1
while True:
    try:

        print("Input something other than a number to stop")

        number = int(input(f"Input number ({current_number}): "))

        number_list.append(number)
    
        current_number += 1

    
    except ValueError:
        print("Stopped")
        break

if number_list:
    number_list.sort(reverse = True)#Use sort.() to sort numbers highest to lowest, reverse = True to make it sort highest to lowest

#Print the numbers highest to lowest