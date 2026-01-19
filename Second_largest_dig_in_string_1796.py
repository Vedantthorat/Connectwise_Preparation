class Solution:
    def secondHighest(self, s: str) -> int:
        seen = set()
        for ch in s:
            if ch.isdigit():
                seen.add(int(ch))
        if len(seen) < 2:
            return -1
        new = sorted(seen)
        return new[-2]
        
