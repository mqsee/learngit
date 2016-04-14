class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        if(s!=""):
            ss = s.split()
            l = len(ss)
            for i in range(l/2):
                tmp = ss[i]
                ss[i] = ss[l-1-i]
                ss[l-1-i] =tmp
            s = (' ').join(ss)
        return s