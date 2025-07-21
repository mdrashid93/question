#class and instance attribute in python
# class attribute belonging to class itself
# class sampleclass:
#     count=0 #class attribute
#     def increase(self):
#         sampleclass.count+=1

# #calling increase on object
# sample1=sampleclass()
# sample1.increase()
# print(sample1.count)

# #calling increase on one more object
# sample2=sampleclass()
# sample2.increase()
# print(sample2.count)


# #vars() and dir()
# #instance attributes.\
# class emp:
#     def __init__(self):
#         self.name="md"
#         self.salary=50000
    
#     def show(self):
#         print(self.name)
#         print(self.salary)

# e1=emp()
# print("dictionary form:",vars(e1))
# # print(dir(e1))


# #python program to demonnstrate initiating a class
# class Dog:
#     #a simple class attribute
#     attr1="mammal"
#     attr2="dog"
#     #a simple method
#     def fun(self):
#         print("i am a",self.attr1)
#         print("i am a",self.attr2)
    
#     def greet(self):
#         print("hope u r doing well")
# #driver code
# #object initiating
# md=Dog()
# #accssing class attribute and method througn objects
# print(md.attr1)
# print(md.attr2)
# md.fun()
# md.greet()


# class Animal:
#     def __init__(self,name):
#         #storing the name of the animal
#         self.name=name
#     def sound(self):
#         #this method should be implemented by subclasses
#         raise NotImplementedError("subclass must implemented this method")

# class Dog(Animal):
#     def sound(self):
#         #dog specific sound 
#         return "woof!"
# #creating instance
# #animal instance with generic name
# a=Animal("generic name")
# #dog instance with name "buddy"
# d=Dog("buddy")
# #accessing attribute and methods
# print(a.name)
# print(d.name)
# print(d.sound())



# class Shape:
#     def __init__(self,color):
#         self.color=color
    
#     def area(Self):
#         raise NotImplementedError("subclass must be implemented by this method")

# class circle(Shape):
#     def __init__(self, color,radius):
#         #initiated the parent class shape with color
#         super().__init__(color)
#         #storing the radius of circle
#         self.radius=radius
#     def area(Self):
#         return 3.14*Self.radius**2
    
# #creating instances
# #shape instance with color "red"
# s=Shape("red")
# #circle instance with color "blue "and radius 5
# c=circle("blue",5)
# #accessing the attribute and methods
# print(s.color)
# print(c.color)
# print(c.radius)
# print(c.area())





# create outer class
class Doctors:
    def __init__(self):
        self.name = 'Doctor'
        self.den = self.Dentist()
        self.car = self.Cardiologist()

    def show(self):
        print('In outer class')
        print('Name:', self.name)

    # create a 1st Inner class
    class Dentist:
        def __init__(self):
            self.name = 'Dr. Savita'
            self.degree = 'BDS'

        def display(self):
            print("Name:", self.name)
            print("Degree:", self.degree)

    # create a 2nd Inner class
    class Cardiologist:
        def __init__(self):
            self.name = 'Dr. Amit'
            self.degree = 'DM'

        def display(self):
            print("Name:", self.name)
            print("Degree:", self.degree)


# create a object
# of outer class
outer = Doctors()
outer.show()

# create a object
# of 1st inner class
d1 = outer.den

# create a object
# of 2nd inner class
d2 = outer.car
print()
d1.display()
print()
d2.display()