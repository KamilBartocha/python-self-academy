# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
# determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# Input: s = "()[]{}"
# Output: true
# Input: s = "(]"
# Output: false

def isValid(s):
    """Solution using dummy stack - list with pop and append"""
    stack = []
    for i in s:
        #Check if it opening Parentheses then push it into stack
        if i=='(' or i =='[' or i=='{':
            stack.append(i)
        # stack len >0 and its closing parantheses
        elif(len(stack)):
            el = stack.pop()
            if el=='(' and i !=')':
                return False
            elif el=='[' and i !=']':
                return False
            elif el=='{' and i !='}':
                return False
        else:
            return False

    # something left in stack
    if(len(stack)):
        return False

    else:
        return True

s = "()[]{}"
print(isValid(s))