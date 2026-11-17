class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        angs = {}

        for i in strs:
            if str(sorted(i)) in angs:
                angs[str(sorted(i))].append(i)
            
            else:
                angs[str(sorted(i))] = [i]

        return list(angs.values())