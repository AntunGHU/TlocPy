# html
class Animal:
    pass
class Friend:
    pass

# Question 1: Say we have a class Pet :
class Pet(Animal, Friend):
    def __init__(self, name):
        self.name = name
# What is the best way to call the parent __init__ methods?
    # In the init method, call Animal.__init__  and Friend.__init__ 
    # In the init method, call super().__init__ 
    # Just lookup what the parent's __init__ methods parameters are and pass arguments to them directly when instantiating Pet .
# Correct Answer: In the init method, call super().__init__ 

# Question 2: What is MRO in Python?
    # The order in which you define methods on a class.
    # The order in which the parent methods are defined.
    # The order in which Python resolves functions.
    # The order in which Python looks up (aka resolves) methods on a class, influenced by inheritance.
# Correct Answer: The order in which Python looks up (aka resolves) methods on a class, influenced by inheritance.

# Question 3: What are three ways to look up MRO for the class Penguin ?
    # Penguin.__mro__
    # Penguin.mro
    # mro(Penguin)
    #?Penguin.__mro__
    #?Penguin.mro()
    #?mro(Penguin)
    # Penguin.mro
    # Penguin.mro()
    # help(Penguin)
    #?Penguin.__mro__
    #?Penguin.mro()
    #?help(Penguin)
# Correct Answer:
    #! Penguin.__mro__
    #! Penguin.mro()
    #! help(Penguin)

# Question 4:
class Animal:    
    def speak():
        raise NotImplementedError
# Why is it considered good OOP practice for Animal  to raise a NotImplementedError ?
    # It's impossible to generalize a sound that all animals make, therefore it's best left up to the subclasses to implement.
    #? It should be up to users of the API to implement the speak  method on Animal , since it could be anything.
    # Speak  can vary among different types of animals, therefore we shouldn't try to implement it at all. This is the OOP way of indicating that you shouldn't implement speak .
    #? We haven't finished writing our code, so this is the OOP way to say "I haven't finished implementing this method yet".
# Correct Answer: It's impossible to generalize a sound that all animals make, therefore it's best left up to the subclasses to implement.

# Question 5
print(5 + 5) # 10
print("5" + "5")  # "55"
# How does Python know how to interpret the +  operator differently in these cases?  
    # Python looks at both arguments and decides which version of the +  operator to use by comparing the types.
    #? Python operators have special methods for handling numeric types vs. strings.
    # The first argument has a special method that defines what to do with the + operator.
#Correct Answer: The first argument has a special method that defines what to do with the + operator.

# Question 6
class ShoppingCart:
    def __init__(self):
        self.items = []
        self.count = 0
# How can I make it so that len(cart)  returns the count  of items in my shopping cart, provided cart  is an instance of ShoppingCart ?
    # Add ShoppingCart to the list of classes on the built-in len  function, with a reference to the count  attribute.
    #? Add self.length  as a new attribute to ShoppingCart  that returns self.count .
    # Add self.__len__  as a new attribute to ShoppingCart  that wraps around self.count .
    #?Add self.__len__(self)  as a new method on ShoppingCart that returns self.count .
# Correct Answer: Add self.__len__(self)  as a new method on ShoppingCart that returns self.count .