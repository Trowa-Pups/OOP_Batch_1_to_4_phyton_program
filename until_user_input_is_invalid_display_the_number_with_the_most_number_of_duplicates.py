#Ask the user to input numbers until they inputed an invalid input
current_number = 1
while True:
    try: 
        print("Input somnething other than a number to stop")

        number = int(input(f"Input number ({current_number})"))

    except ValueError:
        print("Stopped")
        break
    
#Create a list that has a system where it checks if inputed number has a duplicate or not 
#Check how many duplicates a number has
#Print the number with the most number of duplicates