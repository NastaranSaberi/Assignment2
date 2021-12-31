import random
number_of_dice = random.randint(1 , 6)


if number_of_dice == 6 :
        print("Excellent\U0001F60D\n You can try your luck again!")
        number_of_dice = random.randint(1 , 6)
        print(number_of_dice)
    
else :
        print(number_of_dice,"\n","Unfortunately you lost\U0001F611 ")
        