import cv2
import numpy
import timeit
import_module = "import random"
import random

x = 1
y = x+1
print(y)

print(timeit.timeit('1+3', number=50000))
print("The time taken is ",timeit.timeit(stmt='a=10;b=10;sum=a+b'))

testcode = '''
def test(): 
    return random.randint(10, 100)
'''
print(timeit.repeat(stmt=testcode, setup=import_module))


def test(): 
    return random.randint(10, 100)
starttime = timeit.default_timer()
print("The start time is :",starttime)
test()
print("The time difference is :", timeit.default_timer() - starttime)


import_module = "import random"
testcode = ''' 
def test(): 
    return random.randint(10, 100)
'''
print(timeit.repeat(stmt=testcode, setup=import_module, repeat=5))

