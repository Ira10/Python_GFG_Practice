######### 20th August 

# def prime_(n):
#     for i in range(n+1):
#         n = 0 


# def prime(n):
#     x = [1 for i in range(1, n+1)]
#     print('x:', x)


#     for i in range(2, int(n ** 0.5) + 1) :
#         print('i', i)

#         for j in range(i, len(x)):
#             print(j)

#             x[j] = 0 if x[j] % i == 0 else 1
    
#     results = [x[k] for k in x if x[k] == 1]

#     return results

# print(prime(9))
            

import math

start = int(input("enter the interval starting poin "))
end = int(input("enter the interval ending point "))

def prime_(start,end):
    prime = []
    for i in range(start, end):
        
        if i < 2:
            continue  # Skip numbers less than 2 since they're not prime
        is_prime = True
        for j in range(2, math.isqrt(i) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            print(is_prime)
            prime.append(i)
    return prime 

print(prime_(start, end))

