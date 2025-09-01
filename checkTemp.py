
# turn celcius to farenheit
# F = C * 1.8 + 32


# getting user input
userInput = input("Celcius: ") or 30


def celToFar(cel):

    # check if number
    try:
        float(cel)
    except ValueError:
        return False
    
    return float(cel) * 1.8 + 32


result = celToFar(userInput)


if result:
    print(result)
else:
    print("Celcius must be a number")
 