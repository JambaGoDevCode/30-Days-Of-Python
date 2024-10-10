'''
    DAY 3 -Operators
'''


print(True)
print(False)



'''
    Example Integers
    Arithmetic Operations in Python | Integers
'''

print('Addition:', 3 + 4)
print('Subtraction:', 3 - 4)
print('Multiplication:', 3 * 4)
print('Division:', 3 / 4)
print('Division without the remainder:', 3 // 4)
print('Modules:', 3 % 4)
print('Exponentiation:', 3 ** 4)
print('Exponentiation:', 3 ^ 4)



'''
    Example Floats
    Floating numbers
'''

print('Floating Point Number, PI', 3.14)
print('Floating Point Number, gravity', 9.81)


'''
    Complex numbers
'''

print('Complex', 2 + 5j)
print('Multiplying complex number: ', (2 + 3j) * (1 + 2j))



'''
    Let´s declare a variable and assign a number date type. I am going to use
    single character variable but remember do not develop habit od declaring such types
    of variables. Variable name should be all the time mnemonic.
    
    Example: Declaring the variable at the top first
'''

a = 5
b = 5

total = a + b
diff = a - b
product = a * b 
division = b / a
remainder = a % b
floor_division = a // b
exponential = a ** b


'''
    I should have used sum instead of total but sum is a built-in function -try to avoid
    overriding built-in functions.
    
    If you do not label your print with some string, you never know where the result is coming from.
'''

print(total)
print("a + b:   ", total)
print("a - b:   ", diff)
print("a * b:   ", product)
print("a / b:   ", division)
print("a % b:   ", remainder)
print("a // b:  ", floor_division)
print("a ** b:  ", exponential)


'''
    Example
'''
print("==   Addition, Subtraction, Multiplication, Division, Modules ==")

number_one = 6
number_two = 8

# Arithmetic Operation
total_ = number_one + number_two
diff_ = number_one - number_two
product_ = number_one * number_two
div_ = number_one / number_two
remainder_ = number_one % number_two


# Printing Values With label
print("Total: ", total_)
print("Difference: ", diff_)
print("Product: ", product_)
print("Division: ", div_)
print("Remainder: ", remainder_)


'''
    Let us start connecting the dots and start making us of what we already 
    know to calculate (area, volume, density, weight, perimeter, distance, force).
    
    Example
'''

#   Calculating area of a circle
radius = 20
area_of_circle = 3.14 * radius ** 2
print('Area of circle:  ', area_of_circle)


#   Calculating area of a rectangle
length = 10
width = 30
area_of_rectangle = length * width
print('Area of rectangle: ', area_of_rectangle)


#    Calculating a weight of an object 
mass = 76
gravity = 9.83
weight = mass * gravity
print(weight, ' N')


# Calculate the density of a liquid
mass_ = 75
volume = 0.0234
density = mass_ /  volume
print(density, ' kg/m^3-')




# Comparison Operators

print("_____________________________________________________")
print("____________________COMPARISON OPERATORS_____________")
print(3>2)
print(3>=2)
print(3<2)
print(3<=2)
print(3==2)
print(3!=2)
print(len('mango') == len('avocado'))
print(len('mango') != len('avocado'))
print(len('mango') < len('avocado'))
print(len('milk') != len('meat'))
print(len('milk') == len('meat'))
print(len('tomato') == len('potato'))
print(len('python') > len('dragon'))

print("_____________________________________________________")
print("Comparing something gives either a True or False")
print("_____________________________________________________")
print('True == True', True == True)
print('True == False', True == False)
print('False == False', False == False)