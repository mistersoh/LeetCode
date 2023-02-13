class Solution:
    def countOdds(self, low: int, high: int) -> int:
        range_of_nums = high-low + 1

        if range_of_nums%2 == 1 and low % 2 == 1: # even case
            return range_of_nums // 2 + 1
        else:
            return range_of_nums // 2