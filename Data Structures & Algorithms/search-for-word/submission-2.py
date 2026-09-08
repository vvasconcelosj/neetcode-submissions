class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def backtrack(i, row, col, visited):
            if i >= len(word):
                return True

            if  row < 0 or row >= len(board) or col < 0 or col >= len(board[row]):
                return False
        
            if (row, col) in visited:
                return False

            if board[row][col] != word[i]:
                return False


            visited.add((row, col))
            result = (
                backtrack(i + 1, row, col + 1, visited) or
                backtrack(i + 1, row, col - 1, visited) or
                backtrack(i + 1, row + 1, col, visited) or
                backtrack(i + 1, row - 1, col, visited)
            )
            visited.remove((row, col))
            return result
            


        for row in range(len(board)):
            for col in range(len(board[row])):
                if backtrack(0, row, col, set()):
                    return True

        return False
