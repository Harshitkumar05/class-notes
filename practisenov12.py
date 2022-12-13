# lamda function
a= int(input("Enter a  firstnumber:"))
b= int(input("Enter a second number"))
c=input("enter operator")
x =lambda a,b:a+b
num=x(a,b)
print("Addition" num)

x = lambda a,b:a*b
num=x(a,b)
print("Subtraction" num)

x = lambda a,b:a/b
num=x(a,b)
print("divide" num)
if c=="+":
    def sum(a,b):
        print(a+b)
    sum(a,b)


'''colors = ["red","blue","red","black"]
car=["fortuner","thar", "Scorpio"]
numbers=[1,4,5,5,4,5]
'''
'''newlist = []
for i in car:
    if "a" in i:
        newlist.append(i)
    print(newlist)
# shorter way
newlist = [x for x in car if x ="fortuner"]
print(newlist)
    '''

#
#colors[0:2] ="yellow","pink"
'''colors.insert(2,"indigo")
colors.append("green")
colors.extend(car)
colors.remove("red")
colors.pop(1)

print(colors)'''
'''for x in car:
    print(x)'''

'''num  =[1,2,3,4,5]
#write a program to turn every item of list into its square
#output[1,4,9,16,25]
sqr = [x*x for x in num]
print(sqr)'''

#num = [1,2,3,4,5,2,6]
'''num2 = num.copy()
print(num)'''
# in the above list, find value2,if it present,replaceit with 200,only update the first occurance

'''for i in num:
    if i==2:
        a=num.index(2) 
        num[a]= 200
        break
print(num)'''     
# concinate the list
'''list1=["x" "y"]
list2=[1,2,3,4,]'''
'''list3=[list1+list2]
print(list3)'''

'''for x in list2:
    list1.append(x)
print(list1)'''
# rivision
