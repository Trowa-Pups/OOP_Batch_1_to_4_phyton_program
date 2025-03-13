#Ask the user to input until they inputed an invalid input
current_number = 1 
while True:
    try:
        print("Input something other than a number to stop")
        number = int(input(f"Input number ({current_number}): "))
        current_number += 1
    
    except ValueError:
        print("Stopped")
        break
#Check if the number has duplicated or not
#Print Unique if number has no duplicate, and print Duplicate if number has duplicate