class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        i=0
        while i < len(nums):
            ans.append(nums[nums[i]])
            i+=1
        return ans
        