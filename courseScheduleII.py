from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        in_degree = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)    
            in_degree[course] += 1

        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])

        answer = []

        while queue:
            course = queue.popleft()
            answer.append(course)
            for neighbour in graph[course]:
                in_degree[neighbour] -= 1
                if in_degree[neighbour] == 0:
                    queue.append(neighbour)

        if len(answer) == numCourses:
            return answer
        else:
            return []
