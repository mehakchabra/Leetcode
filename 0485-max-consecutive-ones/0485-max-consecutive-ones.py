class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        return len(max(''.join(list(map(str,nums))).split("0")))
        