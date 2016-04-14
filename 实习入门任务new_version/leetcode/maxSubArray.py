class Solution(object):
    def maxSubArray(self, nums):
        subresults = []
        flag = False
        for x in nums:
            if not flag and x >= 0:
                subresults.append([x])
                flag = True
            else:
                if (sum(subresults[-1]) + x > 0):
                    subresults[-1].append(x)
                else:
                    subresults.append([x])

        return sum(sorted(subresults, key=lambda x: sum(x), reverse=True)[0])
