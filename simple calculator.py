last_calc=0
while True:
    print("Calculator Program")
    # i wanna develop this later to include more complex arithmethics
    print("1. Penjumlahan (+)")
    print("2. Pengurangan (-)")
    print("3. Perkalian (*)")
    print("4. Pembagian (/)")
    print("5. Sisa (%)")
    print("6. Perpangkatan (**)")
    print("7. Close the Program")
    print("Previous Calculation Value:", last_calc)
    choice=input("Choose between the operations above (1-7): ")
    if choice=='7':
        print("Closing program...")
        break
    if choice not in ['1','2','3','4','5','6','7']:
        print("Invalid choice, please choose a number between 1 and 7.")
        continue
    while True:
        if choice in ['1','2','3','4','5','6','7']:
            num1=(input("Enter the first number of the equation (enter RETURN to go back): "))
            if num1.upper() == "RETURN":
                break
            num2=(input("Enter the second number of the equation: "))
            try:
                num1=int(num1)
                num2=int(num2)
            except ValueError:
                print("Invalid input, please enter numbers.")
                continue
            if choice=='1':
                result=num1+num2
                print(num1,"+",num2,"=",int(result))
            elif choice=='2':
                result=num1-num2
                print(num1,"-",num2,"=",int(result))
            elif choice=='3':
                result=num1*num2
                print(num1,"*",num2,"=",int(result))
            elif choice=='4':
                if num2==0:
                    print("Division by zero is not allowed.")
                    continue
                result=num1/num2
                print(num1,"/",num2,"=",float(result))
            elif choice=='5':
                if num2==0:
                    print("Modulo by zero is not allowed.")
                    continue
                result=num1%num2
                print(num1,"%",num2,"=", float(result))
            elif choice=='6':
                result=num1**num2
                print(num1,"**",num2,"=",int(result))
            last_calc=result
            break
