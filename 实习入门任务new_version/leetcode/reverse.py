class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        mylist = s.split()
        mylist.reverse()
        s = (' ').join(mylist)
