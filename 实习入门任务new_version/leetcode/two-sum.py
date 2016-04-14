class Solution(object):
    def twoSum(self, nums, target):
        mydict = {}
        for pos,x in enumerate(nums):
            if(mydict.get(target-x,None) == None):
                mydict[x]=pos
            else:
                return mydict[target-x],pos