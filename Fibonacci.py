### 12th Sep

def fibo():
    n = int(input("How many times do you wanna run it for? "))
    a = 0 
    b = 1 
    # c = 
    print(a)
    print(b)
    d = 0

    for i in range(n - 2):
        d = a + b
        # c.append(d)
        print(d)
        # b = d
        # a = b
        a = b  # Update 'a' to the previous 'b'
        b = d  # Update 'b' to the newly calculated Fibonacci number
        
    # return c        

    
# print(fibo())

fibo()

def fibo():
    n = int(input("How many times do you wanna run it for? "))
    a = 0 
    b = 1 
    print(a)
    print(b)
    # d = 0

    for i in range(n - 2):
        # d = a + b
        # c.append(d)
        print(a+b)
        # b = d
        # a = b
        b = a + b  # Update 'a' to the previous 'b'
        a = b - a  # Update 'b' to the newly calculated Fibonacci number
        
    # return c        

    
# print(fibo())

fibo()



def fibo():
    n = int(input("How many times do you wanna run it for? "))
    a,b = -1,1

    for i in range(n):
       
        print(a+b)

        b = b + a  # Update 'a' to the previous 'b'
        a = b - a  # Update 'b' to the newly calculated Fibonacci number

fibo()