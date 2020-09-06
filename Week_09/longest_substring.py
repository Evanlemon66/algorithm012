#最长回文子串
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s: return ""
        length = len(s)
        if length == 1 or s == s[::-1]: return s
        max_len,start = 1,0
        for i in range(1, length):
            even = s[i-max_len:i+1]
            odd = s[i-max_len-1:i+1]
            if i - max_len - 1 >= 0 and odd == odd[::-1]:
                start = i - max_len - 1
                max_len += 2
                continue
            if i - max_len >= 0 and even == even[::-1]:
                start = i - max_len
                max_len += 1
                continue
        return s[start:start + max_len]