'''class laptop:
    def __init__(self,name,processor):# this is parameter
        self.name=name # this is object function
        self.processor=processor
    
    def printout(self):
        print("my laptop name is :",self.name,"and the processor is :",self.processor)

        

laptop1=laptop("Asus","i5")
laptop2=laptop("HP","i5")'''


#laptop1.printout()
#laptop2.printout()

'''class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def printout(self):
        print("my name is :",self.name,"and my age is :",self.age)

person1=person("Harshit","18")
person2=person("Ritesh","19")

person1.printout()
person2.printout()
print(id(person1))#heap memory
print(id(person2))'''

'''class person:
    def __init__(self):
        self.name="Harshit"#name is instant variable  depend upon object
        self.age=18

    # def updatename(self,name):
    #     self.name=name

    def compareAge(self,other):
        if(self.age==other.age):
            return True
        else:
            return False
person1=person()
person2=person()
person1.age=22
#person1.updatename("Alok")
#print(person1.name)
if person1.compareAge(person2):
    print("they are of same age")
else:
    print("they are diffrent age")'''

'''class car:
    wheels =4


    def __init__(self,brand,mil):
        self.brand=brand
        self.mil=mil
car1=car("BMW",10)
car2=car("Tesla",8)
car.wheels=3 # it is depend upon only class not in object

print(car1.brand,car1.mil,car1.wheels)
print(car2.brand,car2.mil,car2.wheels)'''

# class Methods

class Student:
    numberofsubject=5
    
    def __init__(self,marks1,marks2,marks3):
        self.web=marks1
        self.python=marks2
        self.math=marks3
    #def avg(self):
     #   print((self.web+self.python+self.math)/3)
    # def getmarks(self): # this method getter or Accessor
    #     return self.math
    # def setmarks(self,marks):
    #     self.math=marks  #mutators
    @classmethod
    def classMethodExample(cls):
        return cls.numberofsubject
 
student1=Student(5,4,8)
student2=Student(6,5,7)
student3=Student(7,5,9)
print(Student.classMethodExample)
# student1.avg()
# student2.avg()
student3.avg()



    
        


#print(id(laptop1))
#print(id(laptop2))
