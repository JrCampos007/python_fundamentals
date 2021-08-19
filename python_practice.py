import random

def oranges():
    random_oranges = round(random.random() * 50)
    print(random_oranges)
    if random_oranges % 2 !=0:
        return f"Tammy has {random_oranges} which is an odd number in her basket"
    else:
        return f"Tammy has {random_oranges} which is an even number in her basket"

print(oranges())