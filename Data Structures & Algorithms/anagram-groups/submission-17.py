class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordMap = defaultdict(list)
        for word in strs:
            freq = [0] * 26
            for c in word:
                freq[ord(c) - ord("a")] += 1
            
            wordMap[tuple(freq)].append(word)

        return list(wordMap.values())