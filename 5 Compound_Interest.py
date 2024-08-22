######### 18th August ######

def compound_interest():
    P = int(input("Enter the principal "))
    r = int(input("Enter the rate ")) #ValueError: invalid literal for int() with base 10: '7.5'
    t = int(input("Enter the time "))

    a=P*(1+(r/100))**t  # formula for calculating amount 
    ci=a-P
    return ci

    # interest = (P*(1 + r//100))**t 
    # CI = interest - P
    # # return interest
    # return CI

    # return P(1 + r/100)**t # TypeError: 'int' object is not callable

# getting # TypeError: 'int' object is not callable because
# you're trying to use P(1 + r//100) as if P were a function, 
# but P is an integer. Instead, you should 
# use the multiplication operator * to properly calculate the compound interest.


print(compound_interest())

# print(compound_interest(4444,33,9))  #TypeError: compound_interest() takes 0 positional arguments but 3 were given
