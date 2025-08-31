class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = len(position)
        pairs = list(zip(position, speed))
        pairs.sort(key= lambda x: x[0], reverse=True)

        for car in pairs:
            time = (target - car[0]) / car[1]
            if not stack:
                stack.append(time)
            else:
                if time > stack[-1]:
                    stack.append(time)

        return len(stack)
        
