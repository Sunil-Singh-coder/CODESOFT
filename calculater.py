def get_number(prompt):
    while True:
       try:
           return int(input(prompt))
       except:
           print("Invelid input")

def get_operator(prompt):
    while True:
        opr =input(prompt)
        if opr in ['+','-','*','/']:
            return opr
        print("please Enter valid opertion")

def calculater(num1,num2,opr):
    if opr == '+':
       print(f"The sum of {num1} and {num2} is {num1 + num2}")
    elif opr == '-':
        print(f"The difference of {num1} and {num2} is {num1 - num2}")
    elif opr == '*':
        print(f"The product of {num1} and {num2} is {num1 * num2}")
    elif opr == '/':
        if num2 == 0:
          print("Error: Cannot divide by zero!")
        else:
          print(f"The quotient of {num1} and {num2} is {num1 / num2}")



print("welcome to simple calculater ")     
print("you can easily perform (+)  ,  (-)  , ( * )  ( / )")

while True:
    num1=get_number("Enter your first number")
    num2=get_number("Enter your second number")
    opr = get_operator("Enter your operator")
    result=calculater(num1,num2,opr)
    calculate_again=input("Do you want to calculate again ").lower()
    if calculate_again != "yes":
        break


                 
