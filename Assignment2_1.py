numbers = []

while True :
    X = input(" Please enter your number :")
    if X == "exit" :
        result = sum(numbers)
        print("Total numbers:", result)
        break


    elif X != "exit" :
        numbers.append(int(X))



    