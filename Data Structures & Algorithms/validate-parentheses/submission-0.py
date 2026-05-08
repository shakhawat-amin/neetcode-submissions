class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict = {'(': ')', '{': '}', "[": ']'}
        for char in s:
            if not stack or dict.get(stack[-1]) != char:
                stack.append(char)
            else:
                stack.pop()
        
        return len(stack) == 0