package forloops;

public class Main {
	
	public static void main(String[] args) {
		int incrementLoop = 5;
		int superiorLimitLoop = 50;
		
		for (int i = 0; i <= superiorLimitLoop; i+=incrementLoop) {
			System.out.println(i);
		} 	
		
		
//		array 
		
		int CONSTANT = 5;
		int[] numbersToIterate = {1,7,5,9,6,2,4};
		
		for (int i = 0; i < numbersToIterate.length; i ++) {
			if (numbersToIterate[i] == CONSTANT) {
				System.out.println("Found a " + CONSTANT + " at index " + i);
			}
		}
	}
}
