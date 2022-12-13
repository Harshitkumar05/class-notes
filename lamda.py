list1=[3,2,8,16,11,34,17]
# even or odd
'''def iseven(i):
    return i%2==0'''
#output=list(filter(iseven,list1))

#filter is function which take argument in functio
#output=list(filter(lambda i : i%2==0,list1))
#output=list(filter(lambda i : i>15,list1))
#map is perform all element one by one
#output=list(map(lambda i:i+2,list1))
#output=list(map(lambda i:i**2,list1))
#reduce is like fibooic function process end to end
from functools import reduce
#output=reduce(lambda a,b:a+b,list1)
#output=reduce(lambda a,b:a*b,list1)
#output=reduce(lambda a,b:a/b,list1)
#output=reduce(lambda a,b:a*2,list1)
list2 =[10,20,30,40,50]
#triple all the elements in the list
#output=list(map(lambda i :i*3,list2))
list3 =[34,88,30,22,10,15,18]
#multiplies of 5 using filter and lambda
output=list(filter(lambda i :i%5==0,list3))

print(output)