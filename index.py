import math
meaning = 0

print("")
# if meaning > 10:
#     print('Right on')
# else:
#     print('Not today')

# Ternary
# print('Right on') if meaning > 10 else print('Failed')

first = 'dave'
last = 'Gray'

# print(type(first) == str)
# print(isinstance(first, str))

# # constructor function
# pizza = str('Pepperoni')
# print(type(pizza) == str)
# print(isinstance(pizza, str))

fullname = first + ' ' + last
fullname += '!'
print(fullname)

# casting
# decade = str(1950)
# print(type(decade))

# statement = "I like rock music from the " + decade + 's'
# print(statement)

multiline = """
  The boy is a very good guy

                                              yes we all know that. 
  
  But you are not in anyway
"""
# print(multiline)

# # string methods
# print(first)
# print(first.lower())
# print(first.upper())
# print(first.title())

# # print(multiline.title())
# # print(multiline.replace('good', 'ok'))
# print(len(multiline))
# multiline += '                                     '
# multiline = '                                      ' + multiline
# print(len(multiline))

# print(multiline.strip())
# print(multiline.lstrip())
# print(multiline.rstrip())

title = ' menu '.upper()
# print(title.center(20, '='))
# print('Coffee'.ljust(16, '.') + '$1'.rjust(4))
# print('Muffin'.ljust(16, '.') + '$5'.rjust(4))
# print('Cheesecake'.ljust(16, '.') + '$10'.rjust(4))

# string index
# print(first[-1])
# print(first[1:-1])

# Boolean data

# print(first.startswith('d'))
# print(first.endswith('d'))
# print(fullname.count('a'))
x = bool(False)

# complex_type
comp_value = 5+3j
# print(type(comp_value))
# print(comp_value.real)
# print(comp_value.imag)

# Function for integers
gpa = 3.58
# print(abs(gpa))
# print(round(gpa))
# print(round(gpa, 1))

# print(math.pi)
# print(math.sqrt(gpa))
# print(math.ceil(gpa))
# print(math.floor(gpa))
# print(math.pow(gpa, 5))

# Casting string to int
zipcode = '1001'
zip_value = int(zipcode)

