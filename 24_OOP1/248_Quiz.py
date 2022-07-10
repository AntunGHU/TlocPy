# Question 1: -What's the difference between a class and an instance?
# -A class is an object constructed from a blueprint; an instance is the # blueprint for constructing class objects.
# -A class is a blueprint for constructing objects; an instance is an object # constructed from the class definition.
# -A class is the primary adventuring style of a player character and # describes spells, skills, and abilities; an instance is a dungeon that a # group of players complete together isolated from the outer world.
# * Correct Answer: 2
# 
# Question 2: -What is encapsulation in OOP?
# -Encapsulation is the process of designing a class to be a module that can # be exported or used by other programmers.
# -Encapsulation is the process of designing a programmatic class using # public and private methods and attributes to implement abstraction.
# -Encapsulation is the process of grouping code into logical namespaces # called classes that are abstract.
# -Encapsulation is the process of building an OOP API.
# * Correct Answer: 2
# 
# Question 3 -What is abstraction in OOP?
# -The idea of making an abstract class that is impractical on its own but # can be used as a template to implement other classes.
# -The idea that you strip programming concepts down to their constituent or # abstract parts and group them into classes.
# -The idea of exposing only "relevant" data in a class interface, hiding # private attributes and methods (aka the "inner workings") from users
# * Correct Answer: 3
# 
# Question 4: -Given the following code snippet, how do we make a new # instance of Car ?
class Car():
    def __init__(self, make):
        self.make = make
#? honda = new Car(make="honda") 
honda = Car() 
honda = Car("honda") 
#? honda = super().__init__("honda") 
# * Correct Answer: 3
# 
# Question 5: -What's the difference between a class method and an instance # method?
# -A class method has class (cls ) as the implicit first argument whereas # instance method has the instance (called self ).
# -Class methods must be decorated with @classmethod , whereas instance # methods don't.
# -Class methods are used when the method does not need to know about the # specific instance; instance methods are the opposite.
# -All of the above.
# * Correct Answer: 4