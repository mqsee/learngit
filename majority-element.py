class Solution(object):
    def majorityElement(self, nums):
        l = len(nums)
        count = 0
        for i in range(0,l):
            if(count == 0):
                elem = nums[i]
                count = 1
            else:
                if(elem==nums[i]):
                    count+=1
                else:
                    count-=1
        return elem