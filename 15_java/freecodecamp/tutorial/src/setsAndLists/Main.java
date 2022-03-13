package setsandlists;
import java.util.Scanner;
import java.util.Set;
import java.util.HashSet;
import java.util.TreeSet;
import java.util.LinkedHashSet;
import java.util.ArrayList;

public class Main {
	
//	Always use lower case for main function here
	public static void main(String[] args) {
		
//		"Simple" declarion of set data structure type
		Set<Integer> t = new HashSet<Integer>();
		
		t.add(737);
		t.add(380);
		t.add(787);
		t.add(777);
		t.add(380);
		
		t.remove(737);
		
		System.out.print(t.isEmpty());
		
		System.out.print(t.size());
		
		System.out.println(t + "\n");
		
		System.out.print(t.contains(777));
		
		t.clear();
		
		System.out.print(t);
		
		
		Set<Integer> treeSet = new TreeSet<Integer>();
		treeSet.add(15);
		treeSet.add(50);
		
		System.out.println("\n TreeSet: \n " + treeSet);
		
		
		Set<Integer> linkHashSet = new LinkedHashSet<Integer>();
		
		linkHashSet.add(80);
		linkHashSet.add(90);
		
		System.out.println("\n LinkedHashSet + \n" + linkHashSet); 
		
		
//		Lists: similar to array, but slower, which can chance sizee
		ArrayList<Integer> arrayList = new ArrayList<Integer>();
		arrayList.add(1);
		arrayList.add(0);
		arrayList.add(3);
		arrayList.add(4);
		arrayList.add(5);
		arrayList.add(8);
		
		System.out.println(arrayList);
		
		arrayList.set(1,5);
		
		System.out.println(arrayList);
		
//		Python equivalent slicing?
		System.out.println(arrayList.subList(1, 3));
		
		
		
	}

}
