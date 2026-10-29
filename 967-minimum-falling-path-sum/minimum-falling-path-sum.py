class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        n= len(matrix)
        dp= matrix[0][:]
        for i in range(1, n):
            prev= dp[:]
            for j in range(n):
                if j>0:
                    left= prev[j-1]
                else:
                    left= float('inf')
                down= prev[j]
                if j< n-1:
                    right= prev[j+1]
                else:
                    right= float('inf')
                dp[j]= matrix[i][j]+ min(left, down, right)
        return min(dp)                

        