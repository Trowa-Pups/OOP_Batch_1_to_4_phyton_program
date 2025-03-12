#Ask the user to input two numbers
number1 = int(input("Please input your first number: "))
number2 = int(input("Please input your second number: "))
#Print all the numbers between the two numbers
for number in range(number1 + 1, number2): #number1 + 1, because it also prints number1
    print(number)