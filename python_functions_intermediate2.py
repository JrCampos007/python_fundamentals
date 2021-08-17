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
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
def iterateDictionary(lis):
    for x in range(len(lis)):
        fn = lis[x]['first_name']
        ln = lis[x]['last_name']
        print("first_name - " + fn + ", last_name - "+ ln)
    return
iterateDictionary(students)

#######################################################################
# 3. Get Values From a List of Dictionaries
def iterateDictionary2(key_name, some_list):
    for x in range(len(some_list)):
        val = some_list[x][key_name]
        print(val)
iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)


#######################################################################
# 4. Iterate Through a Dictionary with List Values
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(some_dict):
    for i in some_dict:                         
        print(len(some_dict[i]), i.upper())     # print the number of values (some_dict[i]) and the key name
        for x in some_dict[i]:                  # iterate through the values to print the list
            print(x)
        print('\n')
printInfo(dojo)