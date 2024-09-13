def palindrome(n):     # 121 is a palindrome   ## 13th Sep  ## 12 mins
    pal = n
    new_ = 0

    while n!= 0:
        rem = n%10
        new_ = new_*10 + rem
        n = n //10

    # return n , new_   # (0, 121)      
        if new_ == pal:
            print(pal, "and", new_, "is palindrome")
        else:
            print("no")

print(palindrome(121))

# no   ## for every instance of loop , if-else is printing
# no
# 121 and 121 is palindrome
# None

######## correct version  ###########

def palindrome(n):

    pal = n
    new_ = 0

    while n!= 0:
        rem = n%10

        new_ = new_*10 + rem

        n = n //10

    # return n , new_   # (0, 121)
        
    if new_ == pal:
        print(pal, "and", new_, "is palindrome")
    else:
        print("no")


print(palindrome(121))

# 121 and 121 is palindrome
# None


# print(125%10)

# print(1258//10)

############ krish naik sol

def is_palindrome(word):
    return word == word[::-1]






            









            