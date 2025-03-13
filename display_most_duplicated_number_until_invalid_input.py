#Ask the user to input numbers until they inputed an invalid input
number_list = [] #Create a list that has a system where it checks if inputed number has a duplicate or not
current_number = 1

while True:
    try: 
        print("Input somnething other than a number to stop")

        number = int(input(f"Input number ({current_number}): "))

        current_number += 1

        number_list.append(number)

    except ValueError:
        print("Stopped")
        break

#Check which has the most duplicates
most_duplicates = max(number_list, key = number_list.count) #Uses max() to grab the highest number 

print("Most duplicates:", most_duplicates) #Print the number with the most number of duplicates