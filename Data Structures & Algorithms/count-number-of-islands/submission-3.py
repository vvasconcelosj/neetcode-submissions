class Solution:
    def in_bounds(self,grid: List[List[str]], r: int, c: int):
        return (
            r >= 0 and r < len(grid) and
            c >= 0 and c < len(grid[0])
        )


    def dfs(self, grid: List[List[str]], r: int, c: int):
        if not self.in_bounds(grid, r, c):
            return 
        
        if grid[r][c] == "0":
            return

        DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        grid[r][c] = "0"

        for dr, dc in DIRS:
            nr = r + dr
            nc = c + dc

            self.dfs(grid, nr, nc)



    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    islands += 1
                    self.dfs(grid, r, c)


        return islands
