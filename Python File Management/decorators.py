
import math
import time

def time_calculator(func):
    def inner(*args,**kwargs):
        start_time = time.time()
        time.sleep(1)
        func(*args,**kwargs)
        finish_time = time.time()
        print(f'Fonksiyon {func.__name__} islemin suresi {finish_time-start_time} saniye')
    return inner
@time_calculator
def usalma(a,b):
    print(math.pow(a,b))

@time_calculator
def faktoriyel(number):
    print(math.factorial(number))

@time_calculator
def toplama(a,b):
    print(a+b)

@time_calculator
def bolme(a,b):
    print(a/b)

usalma(2,3)
faktoriyel(3)
toplama(6,9)
bolme(25,5)