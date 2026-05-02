class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freqMap = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1 # double check ord(c)
            freqMap[tuple(count)].append(s)
            # print(freqMap) remember to comment this line out

        return list(freqMap.values())