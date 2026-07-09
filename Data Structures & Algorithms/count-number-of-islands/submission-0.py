class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        counter = 0
        seen = set()
        
        rows = len(grid)
        cols = len(grid[0])

        def bfs(seen, grid, index):
            q = deque()
            seen.add(index)
            q.append(index)
            while q:
                curr = q.popleft()
                # get all the neighbors of this item and add them to the queue and seen if we haven't seen them yet
                x, y = curr[0], curr[1]
                
                new_coords = []
                if x != 0: 
                    new_coords.append((x - 1, y))
                if x != rows - 1:
                    new_coords.append((x + 1, y))
                if y != 0:
                    new_coords.append((x, y - 1))
                if y != cols - 1:
                    new_coords.append((x, y + 1))
                
                for new_coord in new_coords:
                    if new_coord not in seen:
                        if grid[new_coord[0]][new_coord[1]] != "0":
                            seen.add(new_coord)
                            q.append(new_coord)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    if (i, j) not in seen:
                        bfs(seen, grid, (i, j))
                        counter += 1
        
        return counter
