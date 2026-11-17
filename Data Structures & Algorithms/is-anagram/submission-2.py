class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s) != sorted(t):
            return False

        Sset = set(s)
        Tset = set(t)

        if Tset == Sset:
            return True
        
        else:
            return False


