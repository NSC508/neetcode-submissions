class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        degree = [0] * numCourses
        depends = [set() for i in range(numCourses)]
        for classes in prerequisites:
            pre_req = classes[1]
            dependent = classes[0]

            degree[dependent] += 1
            depends[pre_req].add(dependent)
        
        taken = []
        q = deque()
        for i in range(numCourses):
            if degree[i] == 0:
                q.append(i)
        
        while q:
            curr = q.popleft()
            taken.append(curr)
            for dependent in depends[curr]:
                degree[dependent] -= 1
                if degree[dependent] == 0:
                    q.append(dependent)
        
        return len(taken) == numCourses
