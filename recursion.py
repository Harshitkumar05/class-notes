
#line by line 996 by scientist
'''def hello():
    print("hello world")
    hello()

hello()'''

#line by number 1000 number

'''import sys

sys.setrecursionlimit(1000)

def hello():
    print("hello world")
    hello()

hello()'''


# factorial questions
# to find factorial 10

'''def fact(n):
    if n == 0:
        return 1
    return n *fact(n-1)

num = fact(10)
print(num)'''

#make a funtion return sq of number

'''def sqr(x):
    return x**2
square=sq(5 )
print(square)'''
#lamda function
# to create more time cut this code

x= lambda a,b : a*b 
num=x(5,10)

print(num)

# return with lamda

'''def name(x):
    return lambda a :a+x

num = name(10)
print(num(5))'''

'''def name(x):
    return lambda b: b**x
num = name(64)
print(num(8))'''