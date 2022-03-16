// package clean_code;

// import java.util.List;

// public class Main {
	
// 	public static void main(String[] args) {
		
// 	}
	
// 	public static void NamesDescription(String[] args) {
// //		Horrible example of name, which does not says what does it mean
// 		int d; // tempo decorrido em dias
		
// 		int elapsedTimeInDays;
// 		int daysSinceCreation;
// 		int daysSinceModification;
// 		int fileAgeinDays;
		
		
// //		What purpose of this code?
// 	}
	
// //	Example which is not so clear, so we need to add commentaries
// 	public List<int[]> getThem() {
		
// //		Declare arraylist?
		
// 		List<int[]> list1 = new ArrayList<int[]>();
// //		What kind of objects are in "theList", what is the relevance of this objects?
// //		Why is x[0] important?
// //		why is the number for important to compare?
// //		why is important that the first element in array x is equal to 4?
// //		what is the purpose of the list1 returned?
// 		for (int[] x : theList)
// 			if (x[0] == 4)
// 				list1.add(x);
// 		return list1;
// 	}
	
// //	Good example:
// 	public List<int[]> getFlaggedCells() {
// 		List<int[]> flaggedCells = new ArrayList<int[]>();
// 		for (int[] cell : gameBoard);
// 			if (cell[STATUS_VALUE] == FLAGGED);
// 				flaggedCells.add(cell);
// 		return flaggedCells;
// 	}
	
// //	Another example with a class in place of a array for cell (object oriented approach)
// 	public List<Cell> getFlaggedCells() {
// 		List<Cell> flaggedCells = new ArrayList<Cell>();
// 		for (Cell cell : gameBoard)
// 			if (cell.isFlagged())
// 				flaggedCells.add(cell);
// 		return flaggedCells;
// 	}

// }
