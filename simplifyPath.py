class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        dirs = path.split('/')

        for dire in dirs:
            if dire == '' or dire == '.':
                continue

            elif dire == '..':
                if stack:
                    stack.pop()
            
            else:
                stack.append(dire)

        return '/'+'/'.join(stack)
