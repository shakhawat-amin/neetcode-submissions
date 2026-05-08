class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = ""
        for i in range(len(strs[0])):
            for j in range(len(strs)):
                if len(strs[j]) <= i:
                    return lcp
                if strs[0][i] != strs[j][i]:
                    return lcp
            lcp += strs[0][i]
        return lcp
