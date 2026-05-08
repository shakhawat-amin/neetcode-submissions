class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        for char in s:
            s_dict[char] =  s_dict.get(char, 0) + 1

        for char in t:
            t_dict[char] =  t_dict.get(char, 0) + 1

        if len(s_dict) != len(t_dict):
            return False
        for k, v in s_dict.items():
            if t_dict.get(k, 0) != v:
                return False
        return True        
