class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r, c):
            if (
                r not in range(0, ROWS) or
                c not in range(0, COLS) or
                grid[r][c] == "0"
            ):
                return

            grid[r][c] = "0"
            for dr, dc in DIRS:
                nr = r + dr
                nc = c + dc

                dfs(nr, nc)


        islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    islands += 1
                    dfs(r, c)

        return islands