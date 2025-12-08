class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        Check if two strings are isomorphic.
        Two strings are isomorphic if characters in s can be replaced to get t,
        maintaining one-to-one character mapping.
        
        Examples:
        - "egg" and "add" -> True (e->a, g->d)
        - "foo" and "bar" -> False (o maps to both a and r)
        """
        if len(s) != len(t):
            return False
        
        s_to_t = {}
        t_to_s = {}
        
        for char_s, char_t in zip(s, t):
            # Check if mapping from s to t is consistent
            if char_s in s_to_t and s_to_t[char_s] != char_t:
                return False
            
            # Check if mapping from t to s is consistent (one-to-one)
            if char_t in t_to_s and t_to_s[char_t] != char_s:
                return False
            
            s_to_t[char_s] = char_t
            t_to_s[char_t] = char_s
        
        return True