

'''def argument(*args):
    for i in args:
        print(i)
argument(1,2,3,4,5,6,7,8)'''
# create a function using following conditions 
# it should accept employee name and salary and display both
# if the salary is missing in the function the assign the default value 10000 to salary
# ben(90000) mike(150000) bob()


'''def employee(name,salary=10000):
    print("the name of employee",name +" "+"the salary is " , salary)

employee("Ritesh",900000)
employee("Hrashit"2000000)
employee("prashant") '''

'''a = 5
def example():
    a=10
    print(a)

example()
print(a)'''

'''a = 5
def example():
    global a
    a=10
    print(a)
example()
'''

#[32,21,64,100,13]find how many odd and Even


'''def count(listofnum):
    even=0
    odd=0

    for i in listofnum:
        if i % 2 == 0:
            even+=1
        else:
            odd += 1
    return even, odd
listofnum =[32,21,64,100,13]

even,odd = count(listofnum)
print(even)
print(odd)'''

#create a file that will display the how many items in the list
#have names more than 5 character

name =["Atul","Shubham","Anuruag","Rahul","Dev","Roy"]
more=0
less=0

for i in name:
    len(i)
    if len(i)>5:
        more+=1
        print(i)

    else:
        less+=1
    print(more)
    print(less)

