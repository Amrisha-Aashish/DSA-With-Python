class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i= 0
        unique= 1
        j= 1
        while j< len(nums):
            if nums[j]== nums[j-1]:
                j+=1
                continue
            nums[i+1]= nums[j]
            i+= 1
            unique+= 1
            j+= 1
        return unique
        