class Solution:
    def maxSubArray(self, nums: list) -> int:
        mx, dp = nums[0], nums[0]
        for idx,i in enumerate(nums):
            if idx == 0: continue
            dp = i+dp if i+dp > i else i
            mx = max(mx, dp)
        return mx
    
    # 分治法
    # 即递归计算左右两部分的最大子序列和，计算中间部分的序列和 
    def maxSubArray2(self, nums: list) -> int:
        if len(nums) == 1:
            return nums[0]
        else:
            max_left = self.maxSubArray2(nums[0:len(nums)//2])
            max_right = self.maxSubArray2(nums[len(nums)//2:len(nums)])
        # 开始计算中间部分的序列和
        # range(start, stop[, step])
        max_mid_l, tmp = nums[len(nums)//2 - 1], 0
        for i in range(len(nums)//2-1, -1, -1):
            tmp += nums[i]
            max_mid_l = max(max_mid_l, tmp)
        max_mid_r, tmp= nums[len(nums)//2], 0
        for i in range(len(nums)//2, len(nums), 1):
            tmp += nums[i]
            max_mid_r = max(max_mid_r, tmp)

        return max(max_left, max_right, max_mid_l+max_mid_r)

s = Solution()
print(s.maxSubArray2([-2,1,-3,4,-1,2,1,-5,4])) # 6
print(s.maxSubArray2([-2,-1])) # -1
