class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        answer = []
        for w1,w2 in zip_longest(word1,word2):
            answer.append(w1)
            answer.append(w2)
            
        return (''.join(filter(None, answer)))