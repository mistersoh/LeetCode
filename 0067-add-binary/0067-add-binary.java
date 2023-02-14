class Solution {
    public String addBinary(String a, String b) {
        StringBuilder res = new StringBuilder();
		
		int aLen = a.length() - 1;
		int bLen = b.length() - 1;
		int carry = 0;
		
		while(aLen >=0||bLen>=0) {
			int sum = carry;
			if(aLen >= 0) {
				sum += a.charAt(aLen) - '0';
				aLen--;
			}
			
			if(bLen >= 0) {
				sum += b.charAt(bLen) - '0';
				bLen--;
			}
			
			if(sum > 1) {
				carry = 1;
			}else {
				carry = 0;
			}
			
			res.append(sum%2);			
		}
        
        if(carry != 0) {
			res.append(carry);
		}
		return res.reverse().toString();
    }
}