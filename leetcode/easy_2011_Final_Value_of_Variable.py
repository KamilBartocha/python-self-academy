# There is a programming language with only four operations and one variable X:

# ++X and X++ increments the value of the variable X by 1.
# --X and X-- decrements the value of the variable X by 1.
# Initially, the value of X is 0.

# Given an array of strings operations containing a list of operations, return the final value of X after performing all the operations.

from ast import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        # solution 1 - easiest
        x = 0
        for operation in operations:
            if operation[1] == "+":
                x += 1
            elif operation[1] == "-":
                x -= 1
        return x

        # solution 2
        # return sum([op for op in map(lambda op: 1 if op[1] == '+' else -1, operations)])
