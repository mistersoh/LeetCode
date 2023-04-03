class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        answer = 0
        people.sort()
        
        l, r = 0, len(people) - 1
        
        while l <= r:
            
            small = people[l]
            big = people[r]
            
            if small + big <= limit:
                answer += 1
                l += 1
                r -= 1
                
            else:
                answer += 1
                r -= 1
        return answer