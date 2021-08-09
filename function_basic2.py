# Countdown
def Countdown(a):
    lis =[]
    for x in range (a,-1,-1):
        lis.append(x)
    return lis
print(Countdown(20))
# Print and Return
def print_and_return(a):
    print(a[0])
    return(a[1])
print(print_and_return([1,2]))
# First Plus Length
def first_plus_length(a):
    y = a[0] + len(a)
    return y
print(first_plus_length([5,2,3,4,6,7]))
# Values greater than second
def values_greater_than_second(a):
    lis=[]
    count= 0
    if len(a) < 2:
        return False
    for x in range (len(a)):
        if a[x] > a[1]:
            print(a[x], a[1])
            lis.append(a[x])
            count = count + 1
    print(count)
    return(lis)
print(values_greater_than_second([5,2,3,1,4,5]))