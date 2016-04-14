class Solution(object):
    def isPalindrome(self, s):
        def isword(x):
            if ((x >= 'a' and x <= 'z') or (x >= 'A' and x <= 'Z') or (x >= '0' and x <= '9')):
                return True
            return False

        s = filter(lambda x: isword(x),s)
        s = s.lower()
        return s==s[::-1]