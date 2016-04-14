class Solution(object):
    def getRow(self, rowIndex):
        mylist = []
        for i in range(rowIndex+1):
            mylist.append([1])
            for j in range(1,i+1):
                if(j<i):
                    mylist[i].append(list[i-1][j-1]+list[i-1][j])
                else:
                    mylist[i].append(1)
        return mylist[rowIndex]