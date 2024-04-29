num1=int(input("Enter the first number: "))     #asked user to enter two numbers
num2=int(input("Enter the second number: "))
operations=input("Enter the operation(+,-,*,/,**,//,%): ")
match operations:
    case '+':
        print("The sum of two numbers is", num1+num2)  #adddition operator
    case '-':
        print("The difference of two numbers is", num1-num2)  #subtraction operator
    case '*':
        print("The multiplication of two numbers is", num1*num2) #multiplication operator
    case '/':
        print("The division of two numbers is", num1/num2) #division operator
    case '**':
        print("num1 raise to power num2 is", num1**num2) #exponential operator
    case '//':
        print("The floor division of two numbers is", num1//num2) #floor division operator
    case '%':
        print("modulus of two numbers is", num1%num2) #modulus operator
    case _:
        print("You have used another operator") #default case

        
        
        