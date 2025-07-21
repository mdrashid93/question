#Encapsulation in python
# In Python, encapsulation refers to the bundling of data (attributes) and methods (functions)
# that operate on the data into a single unit, typically a class. It also restricts direct access
# to some components, which helps protect the integrity of the data and ensures proper usage.


# Note: The __init__ method is a constructor and runs as soon as 
# an object of a class is instantiated. 

# #public member
# class Public:
#     def __init__(self):
#         self.name="md"  #public attribute
    
#     def display_name(self):
#         print(self.name)  #public method

# obj=Public()
# obj.display_name() #accessible 
# print(obj.name)#accessible


# #protect member
# class Protected:
#     def __init__(self):
#         self._age=25 #protected attribute
# class subclass(Protected):
#     def display_age(self):
#         print(self._age) #accessible in subclass
        
# obj=subclass()
# obj.display_age()


#private members
class Private:
    def __init__(self):
        self.__salary=50000 # private attribute
    
    def salary(self):
        return self.__salary # access through public method
    
obj=Private()
# print(obj.salary()) #works
# print(obj.__salary) # raises attribute error



# program to illustrate private access modifier in a class

class Geek:

    # private members
    __name = None
    __roll = None
    __branch = None

    # constructor
    def __init__(self, name, roll, branch):
        self.__name = name
        self.__roll = roll
        self.__branch = branch

    # private member function
    def __displayDetails(self):

        # accessing private data members
        print("Name:", self.__name)
        print("Roll:", self.__roll)
        print("Branch:", self.__branch)

    # public member function
    def accessPrivateFunction(self):

        # accessing private member function
        self.__displayDetails()

# creating object
obj = Geek("R2J", 1706256, "Information Technology")

print(dir(obj))
print("")

# Throws error
# obj.__name
# obj.__roll
# obj.__branch
# obj.__displayDetails()

# To access private members of a class
print(obj._Geek__name)
print(obj._Geek__roll)
print(obj._Geek__branch)
obj._Geek__displayDetails()

print("")

# calling public member function of the class
obj.accessPrivateFunction()