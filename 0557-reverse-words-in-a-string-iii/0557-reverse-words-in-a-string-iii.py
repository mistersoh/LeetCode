class Solution:
    def reverseWords(self, s: str) -> str:
        s2 = [*s]

        l = 0
        r = len(s2)-1

        while l<r:
            s2[l],s2[r] = s2[r],s2[l]

            l+=1
            r-=1

        s3 = "".join(s2).split()

        l2 = 0
        r2 = len(s3)-1
        while l2<r2:
            s3[l2],s3[r2] = s3[r2],s3[l2]

            l2+=1
            r2-=1
            
        return " ".join(s3)