#!/usr/bin/env python3

def happy_new_year():
 i = 10
 while i >= 1:
    print(i)
    i-=1
    print ("Happy New Year!")
    pass

def square_integers(int_list):

   return ([num * num for num in int_list])
    

def fizzbuzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
    # for num in range(1,101):
    #     print(f"fizzbuzz {num}" if num % 3 == 0 and num % 5 == 0 else f"fizz {num }")
# happy_new_year()
# square_integers()
# fizzbuzz()

