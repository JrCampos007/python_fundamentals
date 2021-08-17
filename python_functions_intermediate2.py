# 1. Update Values in Dictionaries and Lists
# Change array between values
x = [[5,2,3], [10,8,9]]
x[1][0] = 15
print(x)

# Change last name of first student from 'Jordan' to 'Campos'
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
students[0]['last_name'] = 'Campos'
print(students)

# In the sports_directory, change 'Messi' to 'Jose'
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory['soccer'][0] = 'Jose'
print(sports_directory)

# Change value 20 in z to 30
z = [ {'x': 10, 'y': 20} ]
z[0]['y'] = 30
print(z)

#######################################################################
# 2. Iterate Through a List of Dictionaries


#######################################################################
# 3. Get Values From a List of Dictionaries



#######################################################################
# 4. Iterate Through a Dictionary with List Values