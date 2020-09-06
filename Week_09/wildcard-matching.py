#通配符匹配
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [set() for _ in range(len(p)+1)]
        dp[0].add(-1)
        for i in range(len(p)):
            if p[i] == '?':
                for x in dp[i]:
                    if x + 1 < len(s):
                        dp[i+1].add(x+1)
            elif p[i] == '*':
                minx = len(s)
                for x in dp[i]: minx = min(minx, x)
                while minx < len(s):
                    dp[i+1].add(minx)
                    minx += 1
            else:
                for x in dp[i]:
                    if x+1 < len(s) and s[x+1] == p[i]:
                        dp[i+1].add(x+1)
        if len(s)-1 in dp[-1]:
            return True
        return False