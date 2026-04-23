from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool: # type: ignore
        seen = set()
        for row in range(9):
            for col in range(9):
                value = board[row][col]
                
                if value == ".":
                    continue
                
                row_key = ("row", row, value)
                col_key = ("col", col, value)
                box_key = ("box", row // 3, col // 3, value)
                
                if row_key in seen or col_key in seen or box_key in seen:
                    return False
                
                seen.add(row_key)
                seen.add(col_key)
                seen.add(box_key)

        return True                