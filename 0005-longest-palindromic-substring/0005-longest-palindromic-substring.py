class Solution:
    def longestPalindrome(self, s: str) -> str:
        # initialize 2-D table for storing results
        n = len(s)
        results = [[False] * n for i in range(n)]
        x, y = 0, 0  # start, end of longest palindromic substring so far

        # every 1-letter substring is a palindrome
        for i in range(n):
            results[i][i] = True

        # 2-letter substring(i, j) is a palindrome if string[i] == string[j]
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                results[i][i + 1] = True
                # change longest palindrome to the 1st 2-letter palindrome
                if not x and not y:
                    x, y = i, i + 1

        # results[i][j] = True if results[i + 1][j - 1] == True
        # and string[i] == string[j]
        for k in range(2, n):
            for i in range(n - 2):
                j = i + k
                # break the loop if it exceeds the boundaries of the matrix
                if j == n:
                    break
                # check if current substring is a palindrome
                if results[i + 1][j - 1] and s[i] == s[j]:
                    results[i][j] = True
                    # len(substring(i, j)) > len(substring(x, y))
                    # this way we always choose 1st longest palindrome
                    if j - i > y - x:
                        x, y = i, j

        return s[x:y + 1]