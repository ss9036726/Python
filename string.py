def main():
    print('Hello')

    lower = "i am a lower string"
    upper = "I AM A UPPER STRING"
    cash = 20

    print(lower.upper())
    print(upper.lower())
    print(upper.capitalize())

    newString = upper.swapcase()
    print(id(upper),'and new id is ', id(newString))
    print("i am a string too".upper())
    print("I got a {} $cash".format(cash))

    print(lower.find("am"))
    print(lower.replace("am","will be"))

    userInput1 = "  I am a String   "
    userInput2 = "   I am a String2   "
    userInput3 = "I am a String3   "
    userInput4 = "  I am a String4"

    print(userInput1.strip())
    print(userInput2.strip())
    print(userInput3.strip())
    print(userInput4.split(sep=None))


if __name__ == "__main__" : main() 