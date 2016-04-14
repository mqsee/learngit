class Solution(object):
    def maxSubArray(self, nums):
        l = len(nums)
        dp = []
        dp.append(nums[0])
        res = dp[0]
        for i in range(1,l):
            if(dp[i-1]>=0):
                dp.append(dp[i-1]+nums[i])
            else:
                dp.append(nums[i])
            if(dp[i]>res):
                res = dp[i]
        return res
