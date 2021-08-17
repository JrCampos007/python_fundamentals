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
# If both a min and max number are provided, the function should return a random integer between those 2 values.