from collections import deque
from typing import List, Tuple

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS  = len(grid), len(grid[0])
        DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue: deque[Tuple[int, int]] = deque()

        fresh = 0
        # Record the rotten oranges as starting point
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        if not fresh:
            return 0

        visited = set()
        time = 0
        while queue:
            time += 1
            for i in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in DIRS:
                    nr = r + dr
                    nc = c + dc

                    # Navigate to fresh oranges
                    if (
                        nr >= 0 and nr < ROWS and
                        nc >= 0 and nc < COLS and
                        (nr, nc) not in visited and
                        grid[nr][nc] == 1
                    ):
                        queue.append((nr, nc))
                        visited.add((nr, nc))
                        fresh -= 1

                    # No more fresh oranges remain
                    if not fresh:
                        return time

        return time if fresh <= 0 else -1

