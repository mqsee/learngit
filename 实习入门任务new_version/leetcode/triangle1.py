class Solution(object):
    def generate(self, numRows):
        mylist = []
        for i in range(numRows):
            mylist.append([1])
            for j in range(1,i+1):
                if(j<i):
                    mylist[i].append(list[i-1][j-1]+list[i-1][j])
                else:
                    mylist[i].append(1)
        return mylist