def collatz(number):
    if(number % 2 == 0):
        return(number // 2)
    else:
        return(3 * number + 1)

while(True):
    num = input("Enter a number. Press enter to quit. - ")
    try:
        if(num == ""):
            break

        num = int(num)

        result = 0

        while(num != 1):
            result = collatz(num)
            num = result
            print(num)

             

    except (ValueError,NameError,TypeError):
        print("Please enter an integer")
