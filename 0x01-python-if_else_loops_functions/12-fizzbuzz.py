#!/usr/bin/python3
def fizzbuzz():
    ch = ""
    for i in range(1, 101):
        if i <= 99:
            if i % 3 == 0 and i % 5 == 0:
                ch += "FizzBuzz "
            elif i % 3 == 0:
                ch += "Fizz "
            elif i % 5 == 0:
                ch += "Buzz "
            else:
                ch += "{} ".format(str(i))
        else:
            if i % 3 == 0 and i % 5 == 0:
                ch += "FizzBuzz"
            elif i % 3 == 0:
                ch += "Fizz"
            elif i % 5 == 0:
                ch += "Buzz"
            else:
                ch += str(i)
    print("{}".format(ch), end=" ")
