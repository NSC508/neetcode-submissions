class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def addNeighbor(i, j, distance, seen, grid, q):
            newCoords = (i, j, distance)
            if (i, j) not in seen and grid[i][j] != -1: 
                q.append(newCoords)
                seen.add((i, j))
            
        rows, cols = len(grid), len(grid[0])

        q = deque()
        seen = set()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    coordinates = (i, j, 0)
                    q.append(coordinates)
                    seen.add((i, j))
        
        while q:
            i, j, distance = q.popleft()

            grid[i][j] = distance

            if i != 0: 
                addNeighbor(i - 1, j, distance + 1, seen, grid, q)
            if i != rows - 1:
                addNeighbor(i + 1, j, distance + 1, seen, grid, q)    
            if j != 0:
                addNeighbor(i, j - 1, distance + 1, seen, grid, q)
            if j != cols - 1:
                addNeighbor(i, j + 1, distance + 1, seen, grid, q)
        

