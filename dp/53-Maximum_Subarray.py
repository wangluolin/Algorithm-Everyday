class Solution:
    def maxSubArray(self, nums: list) -> int:
        mx, dp = nums[0], nums[0]
        for idx,i in enumerate(nums):
            if idx == 0: continue
            dp = i+dp if i+dp > i else i
            mx = max(mx, dp)
        return mx



s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
