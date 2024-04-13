class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
        queue = deque()
        time_taken = 0
        for i in range(len(tickets)):
            queue.append(i)
            
        while(queue):
            
            front = queue.popleft()
            
            tickets[front] -= 1
            time_taken += 1
            
            if(tickets[front] == 0 and k == front):
                return time_taken
            
            if( tickets[front] != 0):
                queue.append(front)
            
            

            
            