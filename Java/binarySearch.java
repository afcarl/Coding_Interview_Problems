
public class binarySearch {

	private static int binarySearch(int[] array1, int val){
		return bsHelper(array1, 0, array1.length-1, val);
	}
	
	private static int bsHelper(int[] A, int beginIndex, int endIndex, int val){
		System.out.println("beginIndex =" + beginIndex + " and endIndex = " + endIndex );
		// the endIndex is included in the search
		int mid = (beginIndex + endIndex)/2;
		if (beginIndex == endIndex){
			
			if (A[beginIndex] == val){
				return beginIndex;
			} else {
				// we're sure that the val is not found in this sorted array A
				return -1;
			}
			
		} else {
			if (A[mid] == val){
				return mid;
			} else if (val < A[mid]) {
				// val must be on the left of mid
				return bsHelper(A, beginIndex, mid, val);
			} else {
				// in this case, val > A[mid]
				return bsHelper(A,mid+1,endIndex, val);
			}
		}
	}
	
	public static void main(String[] args){
		int[] A = {1,2,3,4,5,6,7,8,9,10};
		for (int el : A){
			System.out.println(el);
		}
		
		System.out.println("test");
		
		System.out.println(""+ binarySearch(A,11));
	}
}
