while True:
    user_action = input("Would you like to add, subtract, multiply or divide? ")

    if user_action == 'add':
        
        addition1 = int(input("Enter a number "))
        addition2 = int(input("Enter another number "))
        addingResult = addition1 + addition2
        print(f"{addition1}" " + " f"{addition2}" " = " f"{addingResult}")
        
    elif user_action == 'subtract':
        subtract1 = int(input("Enter a number "))
        subtract2 = int(input("Enter another number "))
        subtractResult = subtract1 - subtract2
        print(f"{subtract1}" " - " f"{subtract2}" " = " f"{subtractResult}")
            
    elif user_action == 'multiply':
        multiply1 = int(input("Enter a number "))
        multiply2 = int(input("Enter another number "))
        multiplicationResult = multiply1 * multiply2
        print(f"{multiply1}" " x " f"{multiply2}" " = " f"{multiplicationResult}")

    elif user_action == 'divide':
        divide1 = int(input("Enter a number "))
        divide2 = int(input("Enter another number "))
        divideResult = divide1 / divide2
        print(f"{divide1}" " / " f"{divide2}" " = " f"{divideResult}")
        
    stopCalc = input("Do you want to stop calculating?(yes or no)")
    
    if stopCalc == 'yes':
        break
   
