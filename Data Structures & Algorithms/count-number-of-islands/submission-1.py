class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        visited = set()
        def dfs(r, c):
            if (
                min(r, c) < 0 or
                r >= len(grid) or
                c >= len(grid[r]) or
                (r, c) in visited
            ):
                return

            visited.add((r, c))

            if grid[r][c] == '0':
                return

            
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                dfs(r + dr, c + dc)


        result = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == '1' and (r, c) not in visited:
                    result += 1
                    dfs(r, c)

        return result
