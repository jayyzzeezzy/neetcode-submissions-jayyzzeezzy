class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []
            
        freqMap = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            freqMap[tuple(count)].append(s)
            # print(freqMap)

        return list(freqMap.values())