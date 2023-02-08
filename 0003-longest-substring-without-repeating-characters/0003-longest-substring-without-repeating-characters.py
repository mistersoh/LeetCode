class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start_idx, max_len = 0,0
        last_idx = {}

        for i in range(0, len(s)):
            if s[i] in last_idx:
                start_idx = max(start_idx, last_idx[s[i]]+1)

            max_len = max(max_len, i-start_idx+1)

            last_idx[s[i]] = i


        return max_len