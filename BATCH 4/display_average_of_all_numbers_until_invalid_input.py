#Ask the user to input numbers until they inputed an invalid input
import statistics
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

print(statistics.mean(number_list)) #Use mean.() to get the average and Print the average of all numbers
