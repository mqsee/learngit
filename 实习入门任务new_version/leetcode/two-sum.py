class Solution(object):
    def twoSum(self, nums, target):
        dict = {}
        for pos,x in enumerate(nums):
            if(dict.get(target-x,None) == None):
                dict[x]=pos
            else:
                return dict[target-x],pos