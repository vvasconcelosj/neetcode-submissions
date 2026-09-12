class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        

        def dfs(r, c, visited, prev_height):
            if (
                min(r, c) < 0 or
                r >= ROWS or
                c >= COLS or
                (r, c) in visited or 
                heights[r][c] < prev_height
            ):
                return 

            visited.add((r, c))

            for dr, dc in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                dfs(r + dr, c + dc, visited, heights[r][c])


        # pacific
        pacific = set()
        for r in range(ROWS):
            dfs(r, 0, pacific, float('-inf'))
        for c in range(COLS):
            dfs(0, c, pacific, float('-inf'))

        # atlantic
        atlantic = set()
        for r in range(ROWS):
            dfs(r, COLS - 1, atlantic, float('-inf'))
        for c in range(COLS):
            dfs(ROWS - 1, c, atlantic, float('-inf'))                

        result = []
        for r, c in pacific:
            if (r, c) in atlantic:
                result.append([r, c])

        return result
        

