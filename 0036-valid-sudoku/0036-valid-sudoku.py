from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
#         for i in board:
#             print(i)
        
        sudoku_hash = defaultdict()
        
        sudoku_hash["row"] = defaultdict(list)
        sudoku_hash["col"] = defaultdict(list)
        sudoku_hash["block"] = defaultdict(list)

        
        
        for i in range(9):
            
            for j in range(9):
                
                board_element = board[i][j]
                
                if board_element != '.':
                    
                    if board_element not in sudoku_hash["row"][i]:
                        
                        sudoku_hash["row"][i].append(board_element)
                    else:
                        return False
                    
                    if board_element not in sudoku_hash["col"][j]:
                        
                        sudoku_hash["col"][j].append(board_element)
                    else:
                        return False
                    
                    if board_element not in sudoku_hash["block"][j//3 + i//3*3]:
                        
                        sudoku_hash["block"][j//3 + i//3*3].append(board_element)
                    else:
                        return False
        return True