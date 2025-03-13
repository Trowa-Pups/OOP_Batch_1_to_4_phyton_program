#Ask the user to input until they inputed an invalid input
number_list = []
current_number = 1 
while True:
    try:
        print("Input something other than a number to stop")
        number = int(input(f"Input number ({current_number}): "))
        current_number += 1
        number_list.append(number)

        #Check if the number has duplicated or not
        for check in number_list: 
            if number_list.count(check) == 1:
    
    except ValueError:
        print("Stopped")
        break

#Print Unique if number has no duplicate, and print Duplicate if number has duplicate