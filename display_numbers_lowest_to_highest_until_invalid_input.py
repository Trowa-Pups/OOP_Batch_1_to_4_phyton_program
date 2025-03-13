#Ask the user to input numbers until they inputed an invalid input
current_number = 1
number_list = [] #To store inputed numbers by the user

while True:
    try:
        print("Input something other than a number to stop")
        
        number = int(input(f"Input number({current_number}): "))

        number_list.append(number)

        current_number += 1
        
    except ValueError:
        print("Stopped")
        break

if number_list: #To make sure list isn't empty
    number_list.sort() #Use sort() to sort numbers lowest to highest

print(number_list) #Print the numbers lowest to highest