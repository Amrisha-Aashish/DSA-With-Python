class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res= []
        candidates.sort()
        def backtrack(start, curr, total):
            if total== target:
                res.append(curr.copy())
            if total> target:
                return
            for i in range(start, len(candidates)):
                if i> start and candidates[i]== candidates[i-1]:
                    continue
                curr.append(candidates[i])
                backtrack(i+1, curr, total+ candidates[i])
                curr.pop()
        backtrack(0, [], 0)
        return res
        