class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dict ={}
        for i in words:
            dict[i] = dict.get(i, 0)+1
        sorted_word = sorted(dict.keys(), key = lambda w: (-dict[w], w))
        return sorted_word [:k]
        
