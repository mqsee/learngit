class Solution(object):
    def getRow(self, rowIndex):
        list = []
        for i in range(rowIndex+1):
            list.append([1])
            for j in range(1,i+1):
                if(j<i):
                    list[i].append(list[i-1][j-1]+list[i-1][j])
                else:
                    list[i].append(1)
        return list[rowIndex]