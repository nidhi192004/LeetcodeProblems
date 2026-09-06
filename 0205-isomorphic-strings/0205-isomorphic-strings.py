class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping_s = {}
        mapping_t = {}
        for i in range(len(s)):
            if s[i] in mapping_s and mapping_s[s[i]] != t[i]:
                return False
            if t[i] in mapping_t and mapping_t[t[i]] != s[i]:
                return False
            mapping_s[s[i]] = t[i]
            mapping_t[t[i]] = s[i]
        return True