class Solution(object):
    def isPalindrome(self, s):
        s = filter(lambda x:(x>='a' and x<='z') or (x>='A' and x<='Z') or (x>='0' and x<='9'),s)
        s = s.lower()
        flag = True
        l = len(s)
        for i in range(l/2):
            if(s[i]!=s[l-1-i]):
                flag = False
        return flag