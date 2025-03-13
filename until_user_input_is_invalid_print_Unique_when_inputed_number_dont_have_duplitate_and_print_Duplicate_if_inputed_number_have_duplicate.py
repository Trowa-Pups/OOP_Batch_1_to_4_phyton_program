#Ask the user to input numbers until they inputed an invalid input
number_list = [] #To store inputed numbers by the user
current_number = 1 #To see the current number the user inputed
while True: 
    try:
        print("Input something other than a number to stop")

        number = int(input(f"Input number ({current_number}): "))
        
        #Check if the number has duplicated or not
        #Print Unique if number has no duplicate, and print Duplicate if number has duplicate
        if number in number_list: #Checks if the number if the number is already in the list
            print("Duplicate")    #Changed it to that because its less complicated and does the same job

        else:
            print("Unique")

        current_number += 1  

        number_list.append(number) #To put it in the list
        #I moved this because when i input a number, it puts it in the list first before checking
        #So, everytime i input a number, the system already sees that the number is already there , so it prints "Duplicate" everytime

    except ValueError:
        print("Stopped")
        break

