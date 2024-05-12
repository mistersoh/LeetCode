class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
  
         # First Attempt
#         def quickSort(fractions):
#             if (len(fractions) <= 1):
#                 return fractions
            
#             pivot = fractions[len(fractions)//2]
#             l,r,e = [],[],[]
            
#             for a in fractions:
#                 if a[0]*pivot[1] < a[1]*pivot[0]:
#                     l.append(a)
#                 elif a[0]*pivot[1] > a[1]*pivot[0]:
#                     r.append(a)
#                 else:
#                     e.append(a)
        
#             return quickSort(l) + e + quickSort(r)
        
        fractions = []
        for idx, val in enumerate(arr):
            subarr = arr[idx+1:][::-1]
            for num in subarr:
                fractions += [(val, num)]
                
        sorted_fractions = sorted(fractions, key=lambda x: x[0]/x[1])
        
        return sorted_fractions[k-1]
        
        
            
            