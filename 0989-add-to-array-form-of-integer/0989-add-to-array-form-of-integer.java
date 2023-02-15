class Solution {
    public List<Integer> addToArrayForm(int[] num, int k) {
        List<Integer> list = new ArrayList<>();
		int numLen = num.length-1;
		
		while(numLen >= 0|| k>0) {
			if(numLen>=0) {
				k=k+num[numLen];
			}
			list.add(k%10);
			k/=10;
			numLen--;
		}
		Collections.reverse(list);
		return list;
    }
}