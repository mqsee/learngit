class Solution(object):
    def majorityElement(self, nums):
        count = 0
        for x in nums:
            if(count == 0):
                elem = x
                count = 1
            else:
                if(elem == x):
                    count+=1
                else:
                    count-=1
        return elem