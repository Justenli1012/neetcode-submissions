class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        visited = set()
        max_area = 0

        #Loop through all cells in grid,
        # for each cell: run dfs on it until it ends,
        #     dfs(grid, r,c, visited, max_area) returns area
        #     if max_area = area returned
        #         set max_area = new_area
        #     Run it again for next unvisited cell (island)
        # return max_area
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if (r,c) not in visited and grid[r][c] == 1: #visits a new island cell
                    visited, area = self.dfs(grid, r, c, visited, 0)
                    print(area)
                    if max_area < area:
                        max_area = area
        return max_area

    def dfs(self, grid, r, c, visited, max_area):
        #check edge cases
        #Out of bounds
        if r < 0 or r > len(grid)-1 or c < 0 or c > len(grid[0])-1:
            return visited, max_area

        #base case: terminates if it hits water, or the cell has been visited already
        if grid[r][c] == 0:
            return visited, max_area
        if (r,c) in visited:
            return visited, max_area

        #recursive case: 
        #everytime visit a new island and its a 1, update max_area
        #new island cell: (cell == '1') and cell not in visited = max_area++
        max_area += 1
        visited.add((r,c))

        #explore neighbors
        visited, max_area = self.dfs(grid, r-1, c, visited, max_area) #left node
        visited, max_area = self.dfs(grid, r+1, c, visited, max_area) #right node
        visited, max_area = self.dfs(grid, r, c+1, visited, max_area) #above node
        visited, max_area = self.dfs(grid, r, c-1, visited, max_area) #below node

        return visited, max_area




