### 19th Aug
# Input : 153
# Output : Yes
# 153 is an Armstrong number.
# 1*1*1 + 5*5*5 + 3*3*3 = 153

# Input : 120
# Output : No
# 120 is not a Armstrong number.
# 1*1*1 + 2*2*2 + 0*0*0 = 9


def Armstrong():
    n = int(input("Enter the num "))
    arm_ = 0
    while n != 0:
        rem = n % 10
        arm = rem**3
        arm_ += arm

        n = n // 10
    return arm_

print(Armstrong())

# print(153%10)
# print(3**3)
