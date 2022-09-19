# Given an integer x, return true if x is palindrome integer.
# An integer is a palindrome when it reads the same backward as forward.
# For example, 121 is a palindrome while 123 is not.

if __name__ == "__main__":
    def isPalindrome(x):
        """ dummy solution """
        signs = str(x)
        while True:
            if(len(signs) > 1):
                if(signs[0] == signs[-1]):
                    signs = signs[1:-1]
                else: return False
            else: return True
    
    print(isPalindrome(1000021))