class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        edgesMap = {}
        for i in range(n):
            edgesMap[i] = set()
        for edge in edges:
            src, dst = edge[0], edge[1]
            edgesMap[src].add(dst)
            edgesMap[dst].add(src)
        
        def bfs(seen, start, edgesMap):
            q = deque()
            seen.add(start)
            q.append(start)
            while q:
                curr = q.popleft()
                connections = edgesMap[curr]
                for conn in connections:
                    if conn not in seen:
                        seen.add(conn)
                        q.append(conn)
        
        connectedComponents = 0
        seen = set()
        for i in range(n):
            if i not in seen:
                connectedComponents += 1
                bfs(seen, i, edgesMap)
        return connectedComponents
