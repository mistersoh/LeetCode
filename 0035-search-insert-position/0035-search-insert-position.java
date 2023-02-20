class Solution {
    public int searchInsert(int[] nums, int target) {
		
		int start_point = 0;
		int end_point = nums.length - 1;
		
		while(start_point<=end_point) {
			
			int mid_length = (start_point+end_point)/2;
			
			if(target <= nums[mid_length]) {
				end_point = mid_length - 1;
			}
			else if(target > nums[mid_length]){
				start_point += 1;
			} else {
				return mid_length;
			}
		}
		
		return start_point;
	}
}