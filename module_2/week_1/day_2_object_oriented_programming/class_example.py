class Guitarist(object): # (object) is for python 2, inhererit from object
    """
    Docstring
    """
    age = 50 # a classs attribute
    _handicap = False # '_' for hidden attribute (another way to protect)

    # decorator: to protect an attribute (from overwrite by accident)
    @property   # turn a method into a property, access by .wheels , not .wheels()
    def wheels(self): # may move after __init__ since need passing in argument
        if _is_f350 == True:
            return 6
        else:
            return 4

    #instance method
    def __init__(self, age):
        self.age = age
        self.name = "George" #instance attribute
        self.role = "Guitarist"
        self.instrument_type = "Stringed Instrument"

    @classmethod    #a class method, so can call the method without instantiating the class
    def tune_instrument(cls):
        print("Tune the strings!")

    #instance method
    def practice(self):
        print("Strumming the old 6 string!")

    @staticmethod  # a static method, can call without instantiating the class
    def perform(): #or def perform(new_name)
        print("Hello, New  York!") # print(f"Hello, New  York! {new_name}")
                                    # call with: Guitarist.perform()

class Bass_Guitarist(Guitarist):

    def __init__(self):
        super().__init__(None)  # or pass a number because parent init requires to pass in age.
        # super(the specific parent).__init__(), ##if multiple inheretance
        self.name = "Paul"
        self.role = "Guitarist" #overwrite since it is after super, vice versa
        if type(toppings)!= list: #better use "isintance(var, e.g., str or class)"
            raise TypeError('gotta be a list')
        self.toppings = [*toppings] # or .copy(), watch out for slicing

    def slicing(self, number): #or number = None, later if number = None: number = []; do not do number =[]
        if type(number)!=int:
            raise TypeError('gotta be an integer')
        print(f'slice into {number} pieces')

    def practice(self):
        print("I play the Seinfeld Theme Song when I get bored")

    def perform(self):
        super().perform()
        print("Thanks for coming out!")
