#Ask the user to input numbers until they inputed an invalid input
number_list = [] #To store the numbers inputed
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
#Use mean.() to get the average
#Print the average of all numbers
