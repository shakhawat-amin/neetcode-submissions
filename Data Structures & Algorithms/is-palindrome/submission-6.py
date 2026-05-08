class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(x.lower() for x in s if (x.isalnum()))
        print(s)
        start, end = 0, len(s)-1
        while start < end:
            if s[start] != s[end]:
                return False
            start, end = start+1, end-1
        
        return True