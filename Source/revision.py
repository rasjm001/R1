# Question one
def distance(velocity, time):
    distance = velocity * time
    return distance


#create a class
class Person:
    #init the class
    def __init__(self, name, age, gender):
        #use self.parameter so that each instantion of the class with assign the passed parametrs as its own.
        self.name = name
        self.age= age
        self.gender = gender

    def method1(self):
        print("My name is ", self.name, " I am ", self.age, " and a ", self.gender)



#create and object from the class
person_james = Person("James", 30, "male")

#call the method in the person_james object

person_james.method1()

#Create a subclass/inherit

#creat a subclass that adds new to the superclass

#use a dictionary

#use a list#

#use a set