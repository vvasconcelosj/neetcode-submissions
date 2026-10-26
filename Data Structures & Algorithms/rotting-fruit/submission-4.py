class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        fresh = 0
        queue = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    queue.append((r, c))

        if not fresh:
            return 0

        time = 0
        DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()
        while queue:
            time += 1

            for i in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in DIRS:
                    nr = r + dr
                    nc = c + dc

                    if (
                        nr in range(0, ROWS) and
                        nc in range(0, COLS) and
                        (nr, nc) not in visited and
                        grid[nr][nc] == 1
                    ):
                        visited.add((nr, nc))
                        fresh -= 1
                        queue.append((nr, nc))

                    if not fresh:
                        return time

        return time if not fresh else -1

