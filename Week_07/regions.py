#被围绕的区域
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) <= 2 or len(board[0]) <= 2:
            return

        row, col = len(board), len(board[0])

        def dfs(i, j):

            if i < 0 or j < 0 or i >= row or j >= col or board[i][j] != 'O':
                return
            board[i][j] = 'A'

            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

        for i in range(row):
            dfs(i, 0)
            dfs(i, col - 1)

        for j in range(col):
            dfs(0, j)
            dfs(row - 1, j)

        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'A':
                    board[i][j] = 'O'