#   1- Inside 30DaysOffPython create a folder called day_2. Inside this folder create a file named variables.py
#   2- Write a python comment saying "Day 2: 30 Days of Python programming"
#   3- Declare a first name variable and assign a value to it
firstname_ = "João"

#   4- Declare a last name and assign a value to it
lastname_ = "Jamba"

#   5- Declare a full name variable and assign a value to it
fullname_ = "João Jamba"

#   6- Declare a country variable and assign a value to it
country_ = "Angola"

#   7- Declare a city variable and assign a value to it
city_ = "Luanda"

#   8- Declare a age variable and assign a value to it
age_ = 29

#   9- Declare a year variable and assign a value to it
year_ = '2024'

#   10- Declare a variable is_married and assign a value to it
is_married = True

#   11- Declare a variable is_true and assign a value to it 
is_true = False

#   12- Declare a variable is_light_on and assign a value to it
is_light_on = False

#   13- Declare multiple variable on one line
bi_number, father_name, mother_name, my_name, morada, bairro, municipio, altura, data_nascimento, data_emicao = 123456789, "Nome do pais dele", "Nome da mãe", "Mue nome", "Luanda", "malueca", "Bengo", 1.45, "12-04-2021","12-04-2021"


'''
    Exercises Leves 2
'''

#   1- Check the data type of all your variables using type() built-in function
print(type(firstname_))
print(type(lastname_))
print(type(fullname_))
print(type(country_))
print(type(city_))
print(type(age_))
print(type(year_))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))


#   2- Using the len() built-in function, find the length of your first name
print(len(firstname_))

#   3- Compare the length of your first name and your last name
print(len(lastname_) < len(firstname_))
print(len(lastname_) > len(firstname_))
print(len(lastname_) == len(firstname_))
print(len(lastname_) != len(firstname_))

#   4- Declare 5 as num_one and 4 as num_two

num_one = 5
num_two = 4

total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one**num_two
floor_division = num_one // num_two

print(total)
print(product)
print(division)
print(remainder)
print(exp)
print(floor_division)

#   5- The radius of a circle is 30 meters.
    
    # Calculate the are of a circle and assign the value to a variable name of area_of_cicle

radius_circle = 30
area_of_circle = 3.14159 * (radius_circle)**2
print(area_of_circle)

    # Calculate the circumference of circle and assign the value to a variable name of circum_of_circle

radius_circle = 30
circum_of_circle = 2 * 3.14159 * radius_circle
print(circum_of_circle)


    # Take radius as user inout and calculate the area

radius_circle = int(input("Insert de Circle Anglo:"))
area_of_circle = 3.14159 * (radius_circle)**2
print(area_of_circle)

