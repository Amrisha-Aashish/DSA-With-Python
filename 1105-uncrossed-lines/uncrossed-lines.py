class Solution:
    def maxUncrossedLines(self, nums1: list[int], nums2: list[int]) -> int:
        n= len(nums1)
        m= len(nums2)
        dp= [[-1]* m for _ in range(n)]
        def func(i, j):
            if i== n or j== m:
                return 0
            if dp[i][j]!= -1:
                return dp[i][j]
            if nums1[i]== nums2[j]:
                dp[i][j]= 1+ func(i+1, j+1)
            else:
                dp[i][j]= max(func(i+1, j), func(i, j+1))
            return dp[i][j]
        return func(0, 0)

        