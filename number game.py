import random
score = 0
n = random.randint(0,9)
x = int(input("tries = "))
if x > 10 or x < 1:
    print ("Are you kidding me?!")
else:
    while (x>0):
        score+=1
        a = int(input("Take a number : "))
        if a == n:
            print("Correct!\nYou won after : {} attempts".format(score))
            break
        else :
            print("Wrong *_*")
        x-=1
    if a!=n :
        print("You lost, The number is: {}, LOL".format(n))