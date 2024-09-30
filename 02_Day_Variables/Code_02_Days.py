

# Variables in Python

firste_name = "Joao"
last_name = "Jamba"
country = "Angola"
city = "Luanda"
age = 29
is_married = False
skills = ["JavaScript", "TypeScript", "Python"]

person_info = {
    'firstname':'Joao',
    'lastname':'Jamba',
    'country':'Angola',
    'sigla':'AO',
    'city':'Luanda'
}

print('Hello Jamba Code')
print(len('Hello Jamba Code'))
print('Hello Jamba',',','Code')

print('First name:', firste_name)
print('First name length', len(firste_name))

print('Last name', last_name)
print('Last name length', len(last_name))

print('Country:', country)
print('City', city)
print('Age', age)
print('Married:', is_married)
print('Skills', skills)
print('Person information:', person_info)




# Declaring Multiple Variable in a Line 


pais_origem, provincia, municipio, idade, seu_nome, casa_numerio = 'Angola', 'luanda', 'belas', 29, 'jamba', 124

print('Nome: ', seu_nome)
print('Idade: ', idade)
print('Casa Nº: ', casa_numerio)
print('Município: ', municipio)
print('Província: ', provincia)
print('País: ', pais_origem)
print(pais_origem, provincia, municipio, idade, seu_nome, casa_numerio)



'''
    Getting user input using input() built-in function. Let us assing the data we get from a user into
    first_name and age variable.
'''

my_first_name = input('What is your first name: ')
my_age = input('How old are you')
print(my_first_name)
print(my_age)



'''
    Data Types

    There are several data types in Python. To identify the data type we use the type built-in-function.
    I would like to ask you to focus on understanding different data types very well. When it comes to programming,
    it is all about data types. I introduced data types at the very beginning and it comes again, because every topic
    is related to data types. We will cover data types in more detail in their respective section.

    Checking data types and casting
        Check data types: To check the data type of certain data/variable we use the type
'''


firste_name_ = "Joao"
last_name_ = "Jamba"
country_ = "Angola"
city_ = "Luanda"
age_ = 29

# printing out types
print(type(firste_name_))
print(type(last_name_))
print(type(country_))
print(type(city_))
print(type(age_))

print(type(10))
print(type(10.54))
print(type(5 + 3j))
print(type(True))
print(type([2,4,6,7,3,2]))
print(type({'nome':'jamba','idade':32,'is_sigle':'no'}))
print(type((2,6)))
print(type(zip([43,45],[2,7])))

'''
    Casting: Converting one data type to another data type. We use int(), float(), str(), list, set When 
    we do arthmetic operation string numbers should be first converted to int or float otherwise it will
    return an error. If we concatrnate a number wth a string, the number should be first converted to a string.
    We will talk about concatenation in String section.
'''

# int to float
num_int = 100
print('number ', num_int)
num_float = float(num_int)
print(num_float)

# float to int
gravity = 9.56
print(int(gravity))

# int to string
new_number = 20
print(new_number)
new_str = str(new_number)
print(new_str)






