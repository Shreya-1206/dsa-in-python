#  chk palindrome
 
def isPalindrome(x):
    if x < 0:
        return False
    return x == int(str(x)[::-1])   

print(isPalindrome(13))
#  Incase Of Num
  
#  123  === 123 => "123" => ["1","2","3"] => ["3","2","1"] => "321"
#  this + operator will convert to num from string