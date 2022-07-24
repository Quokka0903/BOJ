class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = [0] * 2
        for i in range(len(nums)) :
            for j in range(i + 1, len(nums)) :
                if i + j == target :
                    ans[0] = i
                    ans[1] = j 
        return (ans)