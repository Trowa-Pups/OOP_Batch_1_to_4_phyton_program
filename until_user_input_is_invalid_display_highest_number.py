#Ask the user to input numbers until they inputed an invalid input
current_number = 1
while True:
    try:
        print("Input something other than a number to stop")
    
        number = int(input(f"Input number ({current_number}): "))

        current_number += 1
    except ValueError:
        print("Stopped")
        break

#Create a list and check what number in the list has the highest value
#Print the highest number