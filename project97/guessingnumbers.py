import random
print("Number Guessing Game From 1-15:-")
number=random.randint(1,15)
guess=int(input("Enter your guess:-  "))

if(guess>number):
    print("Your guess was too high, try a smaller number " ) 
    print("You only have 4 chances left!")

elif(guess<number):
    print("Your guess was too low, try a larger number ")
    print("You only have 4 chances left!")

else:
    print("Amazing! First Try!") 


guess2=int(input("Enter your guess:-  "))

if(guess2>number):
    print("Your guess was too high, try a smaller number " ) 
    print("You only have 3 chances left!")

elif(guess2<number):
    print("Your guess was too low, try a larger number ")
    print("You only have 3 chances left!")
 
else:
    print("Congratulations You won!") 

guess3=int(input("Enter your guess:-  "))

if(guess3>number):
    print("Your guess was too high, try a smaller number " ) 
    print("You only have 2 chances left!")

elif(guess3<number):
    print("Your guess was too low, try a larger number ")
    print("You only have 2 chances left!")
 
else:
    print("Congratulations You won!") 



guess4=int(input("Enter your guess:-  "))

if(guess4>number):
    print("Your guess was too high, try a smaller number " ) 
    print("You only have 1 chance left!")

elif(guess4<number):
    print("Your guess was too low, try a larger number ")
    print("You only have 1 chance left!")
 
else:
    print("Congratulations You won!") 


guess5=int(input("Enter your guess:-  "))

if(guess5>number):
    print("Your guess was too high, try a smaller number " ) 
    

elif(guess5<number):
    print("Your guess was too low, try a larger number ")
 
else:
    print("You Lost!") 


