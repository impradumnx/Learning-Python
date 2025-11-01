# basic calculator to perform (+ , - , * , / , %)

num1 = input("Enter first number : ")
operator = input ("Enter a operator (+, -, *, /, %) : ")
num2 = input("Enter second number : ")
if operator == "+" :
    print ("The addition is :" , int(num1) + int(num2))  
elif  operator == "-" :
    print ("The subtraction is :" , int(num1) - int (num2))
elif operator == "*" :
    print ("The multiplication is :" , int(num1) * int (num2))
elif operator == "/" :
    print ("The division is : " , int(num1) / int (num2))
elif operator == "%" :
    print ( "The reaminder is : " , int(num1) % int (num2))
else :
    print ("Invalid operation") 