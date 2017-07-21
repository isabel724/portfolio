money = int(input("How much money do you want to start with?: \n"))
bet = int(input("How much money would you like to bet?: \n"))



from random import randint
color= ["red", "black"]
guess=input ("guess red or black: \n")


roll=color[randint(0,1)]

if guess== roll:
    print("Ball Roll:" + str(roll))
    print("Your:" + str(guess))
    print("You are correct!")
    money= money + bet

else:
    print("Ball Roll:" +str(roll))
    print("Your Color:" + str(guess))
    print("You are incorrect")
    money= money - bet

from random import randint
value= ["odd","even"]
guess=input("guess if number is odd or even: \n")

if guess==roll:
    print("Value:"+str(roll))
    print("Your Value:"+str(guess))
    print("You are correct!")
    money= money + bet

else:
    print("Value:"+str(roll))
    print("Your Number :"+str(guess))
    print("You are incorrect")
    money= money - bet

from random import randint
number = [1,35]
guess = input ("Guess a number between 1 and 35: \n")

guess = int(guess)

if guess == roll:
    print("Number:"+str(roll))
    print("Your:"+str(roll))
    print("You are correct!")
    money= money + bet

else:
    print("Number:"+str(roll))
    print("Your:"+str(guess))
    print("You are incorrect")
    money= money - bet

    print(money)
