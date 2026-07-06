class Solution:
    def twoSum(self, num: List[int], target: int) -> List[int]:
        i, j= 0, len(num)-1
        while i<j:
            sum= num[i]+ num[j]
            if sum== target:
                return [i+1, j+1]
            elif sum< target:
                i+= 1
            else:
                j-= 1
        