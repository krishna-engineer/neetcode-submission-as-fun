from typing import List
import operator

math_ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": lambda a,b: int(a/b),
}

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Task:
        - You are given a list of strings tokens that represents a valid arithmetic expression in 
            Reverse Polish Notation.
        - Return the integer that represents the evaluation of the expression.
        - The operators include '+', '-', '*', and '/'.
        - Assume that division between integers always truncates toward zero.

        Example:
        - Input: tokens = ["1","2","+","3","*","4","-"]
        - Output: 5
        - Explanation: ((1 + 2) * 3) - 4 = 5


        Approach:
        - For each item of list: 
            > check if it's integer, if yes append it to a buffer list
            > if it's operand, pop 2 numbers from list and perform operation on them and then add result back to buffer
        
        - Time complexity:
            > O(n) bcoz each item of input list is being traversed
        
        - Space complexity:
            > O(n/2) buffer will always include operators that are to be used in math operations
        """
        operands = set(["+", "-", "*", "/"])
        buffer = []

        # Code written is based on assumption that input is valid RPN
        for tok in tokens:
            if tok not in operands:
                # Tok is an integer
                buffer.append(int(tok))
                continue
            second, first = buffer.pop(), buffer.pop()
            result = math_ops[tok](first, second)
            buffer.append(result)

        return buffer[0]