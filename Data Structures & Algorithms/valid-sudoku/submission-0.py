class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS = len(board)
        COLS = len(board[0])

        # Validate rows
        rows = defaultdict(set)
        cols = defaultdict(set)
        diagonals = defaultdict(set)

        for r in range(ROWS):
            for c in range(COLS):
                val = board[r][c]

                if val == '.':
                    continue

                if val in rows[r]:
                    return False

                if val in cols[c]:
                    return False

                x = r // 3
                y = c // 3
                if val in diagonals[(x, y)]:
                    return False

                
                rows[r].add(val)
                cols[c].add(val)
                diagonals[(x, y)].add(val) 

        return True