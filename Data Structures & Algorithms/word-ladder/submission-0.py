class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        # hashMap for neighbors called nei
        nei = collections.defaultdict(list)
        # beginWord is not in the wordList
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + '*' + word[j + 1:]
                nei[pattern].append(word)

        visit = set([beginWord])
        q = collections.deque([beginWord])
        res = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                # find this word's pattern then find this pattern in the hashMap
                for j in range(len(word)):
                    pattern = word[:j] + '*' + word[j + 1:]
                    for neiWord in nei[pattern]:
                        if neiWord not in visit:
                            visit.add(neiWord)
                            q.append(neiWord)
            res += 1
        return 0