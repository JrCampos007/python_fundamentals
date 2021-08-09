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