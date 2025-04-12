class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        top = -1
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])
                top += 1
            else:
                if top == -1:
                    return False
                if s[i] == ')' and stack[top] == '(':
                    stack.pop(top)
                    top -= 1
                elif s[i] == '}' and stack[top] == '{':
                    stack.pop(top)
                    top -= 1
                elif s[i] == ']' and stack[top] == '[':
                    stack.pop(top)
                    top -=  1
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
