class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrm = {}

        for word in strs:
            if "".join(sorted(word)) in anagrm:
                anagrm["".join(sorted(word))].append(word)
            else:
                anagrm["".join(sorted(word))] = [word]
        
        return list(anagrm.values())

                