

# This is the firts comment
# This is the second comment
# Python is eating the world 

print("Hello Jamba")


"""
    This is multiline comment
    multiline comment tekes multiple lines.
    Python is eating the world
"""


""" DATA TYPES

    Number
        Imnteger: 
            Interger (Negative, Zero and positive) numbers examples: ...-3, -2, -1, 1, 2, 3 ...
        
        Float:
            Decimal number example: ...-3.5, -2.5, -1.0, 0.0, 1.1, 2.2, 3.5 ....

        Complex 
            example: 1 + j, 2 + 4j

    
    
    String
        A collection of one or more characters under a single or double quote.
        If a string is more than one sentence then we use a triple quote.

        Example:
            'Jamba'
            'Python'
            'I love programming'
            'I hope you are enjoying the first day of 3oDayOfPython Challenge'
    
    Booleans
        A boolean data type is either a True or False value. T and F should be always uppercase.

        Example:
            True # Is the light on? If it is on, then the value is True
            False # Is the light on? If it is off, then value is false

    
    List 
        Python list is an ordered collection which allows to store different data type items.
        A list is similar to an array in JavaScript.

        Example:
            [0,1,2,3,4,5,6,7] # all are the data types - a list of numbers
            ["Banna","Orange","Mango","Avocado"] # all the same data types -a list of strings (fruits)

            
    Dictionary
        A Python dictionary object is an unordered collection of data in a key
        value pair format.

        example:
            {
                'first_name': "Joao",
                'last_name': "Jamba",
                'country': 'Finland',
                'age': 250,
                'is_married': True,
                'skills': ['JS','React','Node','Python']
            }
            
    Tuple
        A tuple is an ordered colletion of diferent data types like list but
        tuples can not be modified once they are created. They are immutable.

        example:
            ("Earrth","Jupiter","Neptune","Mars","Venus","Saturn","Mercury") # planets
            ("Asabeneh","Pawel","Jamba","Brook","Abraham","Lidiya") # Names
    
            
    Set 
        A set is a colletion of data types similar to list and tuple. Unlike
        list and tuple, set is not and ordered collection of items. Like in 
        Mathematics, set in Python stores only unique items.

        In later sections, we willgo in detail about each and very Python data type.

        example:
            {2, 4, 3, 5}
            {3.43,9.54, 2.13} # order is not important in set


    
"""


age = 12
heigth= 1,56

user_name= "joao jamba"
first_name= "joao"
message= "This is the message to send email for all!"

is_maridy= True
is_single= False

age_interval = [0,1,2,3,4,5,6,7,8,9,10]
fruits= ["Banana","Orange","Mango","Avocado"]
countries=["Filand","Estonia","Sweden","Norway"]
different_types= ["Banana", 10, False, 9.34]

Developr = {
    'first_name': "Joao",
    'last_name': "Jamba",
    'country': 'Finland',
    'age': 29,
    'is_married': False,
    'skills': ['JS','React','Angular','Node','Python']
}

dimension= {3.2344, 2.45, 8.34, 5.34}




# Day 01 - 30DaysOfPython Challeng

print(2 + 3)        # Additiona (+)
print(3 - 1)        # Subtraction (-)
print(3 * 4)        # Multiplication (*)
print(16 / 2)       # Division (/)
print(3 ** 2)       # Exponential (**)
print(4 % 2)        # Modulues (%)
print(4 // 2)       # Floor division operator

# Checking data types
print(type(10))             # int
print(type(3.10))           # Float
print(type(1 + 3j))         # Complex number
print(type('Asabeneh'))     # String
print(type([1,2,3,4]))      # List
print(type({'name':'Jamba'}))   # Dictionary
print(type({2.3,97.4,34.6,3.57}))   # Set
print(type((2.3,97.4,34.6,3.57)))   # Tuple


