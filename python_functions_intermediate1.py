# If no arguments are provided, the function should return a random integer between 0 and 100.
import random
def randInt(min=0, max=100):
    num = random.random() * max + min
    return round(num)
print('integer between 0 to 100: ', randInt(), '\n')

# If only a max number is provided, the function should return a random integer between 0 and the max number.
import random
def randInt(min=0, max=100):
    num = random.random() * max + min
    return round(num)
print('integer between 0 to 60: ', randInt(max=60), '\n')

# If only a min number is provided, the function should return a random integer between the min number and 100
import random
def randInt(min=0, max=100):
    num = random.random() * (max-min) + min
    return round(num)
print('integer between 60 to 100: ', randInt(min=50), '\n')

# If both a min and max number are provided, the function should return a random integer between those 2 values.
import random
def randInt(min=0, max=100):
    num = random.random() * (max-min) + min
    return round(num)
print('integer between 50 and 500: ', randInt(min=50, max=500), '\n')

###########################################################################################
# # Added a couple edge cases
###########################################################################################
# 1
import random
def randInt(min=0, max=100):
    if min > max:
        print('you are not very good at this')
        return
    num = random.random() * (max-min) + min
    return round(num)
print('edge case min>max: ', randInt(min=10, max=5), '\n')
# 2
import random
def randInt(min=0, max=100):
    if max < 0:
        print('you are not very good at this')
        return
    num = random.random() * (max-min) + min
    return round(num)
print('edge case max<0: ', randInt(min=10, max=-5), '\n')