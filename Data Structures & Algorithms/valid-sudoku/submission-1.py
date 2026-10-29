class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Row check
        for row in range(9):
            seen = set()

            for cols in range(9):
                digits = board[row][cols]
                
                if digits == ".":
                    continue
                
                if digits in seen:
                    return False
                seen.add(digits)

        # Cols check
        for cols in range(9):
            seen = set()

            for row in range(9):
                digits = board[row][cols]

                if digits == ".":
                    continue
                
                if digits in seen:
                    return False
                seen.add(digits)
        
        # 3*3 box check
        for box_row in range(0, 9, 3):
            for box_cols in range(0, 9, 3):
                seen = set()

                for row in range(box_row, box_row + 3):
                    for cols in range(box_cols, box_cols + 3):
                        digits = board[row][cols]

                        if digits == ".":
                            continue
                        
                        if digits in seen:
                            return False
                        seen.add(digits)
        return True
        
