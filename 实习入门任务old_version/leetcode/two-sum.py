class Solution(object):
    def twoSum(self, nums, target):
        dict = {}
        l = len(nums)
        for i in range(l):
            if(dict.get(target-nums[i],None) == None):
                dict[nums[i]]=i
            else:
                return dict[target-nums[i]],i