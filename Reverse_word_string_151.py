class Solution:
    def reverseWords(self, s: str) -> str:
        word = s.split()
        word.reverse()
        return ' '.join(word)
        
# or
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])
