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
        atlantic = set()

        for c in range(COLS):
            dfs(0, c, pacific, heights[0][c])
            dfs(ROWS - 1, c, atlantic, heights[ROWS - 1][c])

        for r in range(ROWS):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, COLS - 1, atlantic, heights[r][COLS - 1])              

        result = []
        for r, c in pacific:
            if (r, c) in atlantic:
                result.append([r, c])

        return result
        

