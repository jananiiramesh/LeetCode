class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        temps = len(temperatures)
        answer = [0]*temps
        i = 0
        for temp in temperatures:
            if not stack or temp < stack[-1][0]:
                stack.append((temp, i))
                i += 1
            else:
                while stack and temp > stack[-1][0]:
                    answer[stack[-1][1]] = i - stack[-1][1]
                    stack.pop()
                stack.append((temp, i))
                i += 1 

        return answer
        
