class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for r in range(9):
            seen = set()
            for c in range(9):
                num = board[r][c]

                if num == ".":
                    continue

                if num in seen:
                    return False
                seen.add(num)
        
        for c in range(9):
            seen = set()
            for r in range(9):
                num = board[r][c]

                if num == ".":
                    continue

                if num in seen:
                    return False
                seen.add(num)

        boxes = {}    
        
        for r in range(9):
            for c in range(9):
                box = (r // 3, c // 3)

                if box not in boxes:
                    boxes[box] = set()
                
                num = board [r][c]
                if num == ".":
                    continue

                if num in boxes[box]:
                    return False
                
                boxes[box].add(num)
                
        return True
                