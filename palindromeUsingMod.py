## In mod num % 10 gives the last digit of the num
## Means 12 % 10 = 2
## Add the last digit to the reversed_num
## last step remove the last digit from num example 12 will be 1

def isPalindrome(x):
    if x < 0:
        return False
    
    original_num = x
    reversed_num = 0

    while x > 0:
        last_digit = x % 10
        reversed_num = reversed_num * 10 + last_digit
        x = x // 10

    return original_num == reversed_num    


print(isPalindrome(121))