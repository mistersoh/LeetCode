class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        
        len_spells = len(spells)
        len_potions = len(potions)
        
        
        answer = [0] * len_spells
        
        potions.sort()
        max_potion = max(potions)
        
        for num,s in enumerate(spells):
            
            min_strength = (success + s - 1) // s
            
            if min_strength > max_potion:
                continue
                
            weak_potions = bisect.bisect_left(potions, min_strength)
            answer[num] = len_potions - weak_potions
            
        return answer