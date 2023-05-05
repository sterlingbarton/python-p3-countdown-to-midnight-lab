# your code goes here!
import time


def countdown(i):
    while i >= 1:
        print(f'{i} SECOND(S)!')
        i -= 1
    print("HAPPY NEW YEAR!")


def countdown_with_sleep(n):
    while n >= 1:
        print(f'{n} SECOND(S)!')
        n -= 1
        time.sleep(1)
    print("HAPPY NEW YEAR!")
