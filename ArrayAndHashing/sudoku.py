import collections
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        colums = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)# key = row//3 , colum//3

        for row in range(9):
            for colum in range(9):
                boardNumber = board[row][colum]

                if boardNumber == ".":
                    continue

                if (boardNumber in rows[row] or
                    boardNumber in colums[colum] or
                    boardNumber in squares[row // 3, colum // 3]):
                    return False

                colums[colum].add(boardNumber)
                rows[row].add(boardNumber)
                squares[row // 3, colum // 3].add(boardNumber)
        return True

solution = Solution()
solution = solution.isValidSudoku([
                        ["1", "2", ".", ".", "3", ".", ".", ".", "."],
                        ["4", ".", ".", "5", ".", ".", ".", ".", "."],
                        [".", "9", "8", ".", ".", ".", ".", ".", "3"],
                        ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
                        [".", ".", ".", "8", ".", "3", ".", ".", "5"],
                        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                        [".", ".", ".", ".", ".", ".", "2", ".", "."],
                        [".", ".", ".", "4", "1", "9", ".", ".", "8"],
                        [".", ".", ".", ".", "8", ".", ".", "7", "9"]])
print(solution)