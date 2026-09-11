class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        bot = 0
        top = len(matrix) - 1
        row = 0

        while top >= bot:
            row = bot + ((top - bot) // 2)
            print(row)
            if target > matrix[row][-1]:
                bot = row + 1
            elif target < matrix[row][0]:
                top = row - 1
            else:
                break

        if top < bot: 
            return False

        bot = 0
        top = len(matrix[row])
        mid = 0

        while top >= bot:
            mid = bot + ((top - bot) // 2)
            if target > matrix[row][mid]:
                bot = mid + 1
            elif target < matrix[row][mid]:
                top = mid - 1
            else:
                return True

        return False
