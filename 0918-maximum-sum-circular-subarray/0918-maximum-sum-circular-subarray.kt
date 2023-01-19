class Solution {
    fun maxSubarraySumCircular(nums: IntArray): Int {
        var array_sum:Int = 0
        var (currMax, currMin) = Int.MIN_VALUE to Int.MAX_VALUE
        var (maxSoFar, minSoFar) = 0 to 0
        
        val arraySize = nums.size

        for(i in nums) {
            array_sum = array_sum + i
            
            maxSoFar = maxSoFar + i
            currMax = maxOf(maxSoFar, currMax)
            
            minSoFar = minSoFar + i
            currMin = minOf(minSoFar, currMin)
            if (maxSoFar < 0)
                maxSoFar = 0
            if (minSoFar > 0)
                minSoFar = 0
        }
        
        return if (currMin == array_sum) currMax else maxOf(currMax, array_sum - currMin)
    }
}