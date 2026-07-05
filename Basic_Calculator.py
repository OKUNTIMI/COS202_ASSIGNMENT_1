print("BASIC CALCULATOR")

while True :
    print("\nVPossible Operation\n1. Addition\n2. Subtraction\n3. Division\n4. Multiplication\n5. Power\n6. Modulus\n7. Clear\n8. OFF")

    choice=int(input("Select an Operation: "))
    match choice:
        case 1:
            print("You are Perform an Addition Operation" )
            first_opr=int(input("1st Number: "))
            second_opr=int(input("2st Number: "))
            ans=first_opr + second_opr
            print("Your answer is: ",ans)
        case 2:
            print("You are Perform a Subtration Operation")
            first_opr=int(input("1st Number: "))
            second_opr=int(input("2st Number: "))
            ans=first_opr - second_opr
            print("Your answer is: ",ans)
        case 3:
            print("You are Perform a Division Operation")
            first_opr=float(input("1st Operator: "))
            second_opr=float(input("2st Operator: "))
            ans=first_opr / second_opr
            print("Your answer is: ",ans)
        case 4:
            print("You are Perform a Multiplication Operation")
            first_opr=int(input("1st Number: "))
            second_opr=int(input("2st Number: "))
            ans=first_opr *  second_opr
            print("Your answer is: ",ans)
        case 5:
            print("You are Perform an Power")
            first_opr=float(input("Base number: "))
            second_opr=float(input("Power Number: "))
            ans=first_opr ** second_opr
            print("Your answer is: ",ans)
        case 6:
            print("You are Perform a Modulus Operation")
            first_opr=int(input("1st Number: "))
            second_opr=int(input("2st Number: "))
            ans=first_opr %  second_opr
            print("Your answer is: ",ans,)
        case 7:
            print("\n"*6)
            print("Calculator Cleared")
        case 8:
            print("GOOD BYE !!!!!")
            break
            
        
        case _:
            print("\nInvalid Option, Try Again")





