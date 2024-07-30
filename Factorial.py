##### My Approach -- 30th July -- 9:38 PM

n = int(input("Enter the number: "))


def factorial():
    fact = 1
    for i in range(1, n+1):
        fact = fact * i 
    return fact


print(factorial()) 


##### My Approach -- 30th July -- 9:38 PM


##### My Approach -- 30th July -- 9:38 PM --- While loop


# n = int(input("Enter the number: "))


def factorial():
    n = int(input("Enter the number: "))

    fact = 1
    while n >= 1:
        fact = fact * n
        n = n - 1
    return fact


print(factorial())
