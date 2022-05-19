print("Calculator App")
operation=input("Enter the operation ")
firstnumber=int(input("Enter the first number "))
secondnumber=int(input("Enter the second number "))

if(operation=='+'):
    print("You're answer is:- ",firstnumber+secondnumber)

elif(operation=='-'):
    print("You're answer is:- ",firstnumber-secondnumber)

if(operation=='*'):
    print("You're answer is:- ",firstnumber*secondnumber)

elif(operation=='/'):
    print("You're answer is:- ",firstnumber/secondnumber)
