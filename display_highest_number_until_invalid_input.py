#Ask the user to input numbers until they inputed an invalid input
number_list = [] #Create a list and check what number in the list has the highest value
current_number = 1
while True:
    try:
        print("Input something other than a number to stop")
    
        number = int(input(f"Input number ({current_number}): "))

        current_number += 1

        number_list.append(number)
        
    except ValueError:
        print("Stopped")
        break

if number_list: # Make sure the list isn't empty
    print("Highest Number:", max(number_list))#Print the highest number