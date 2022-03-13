package mapshashmaps;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;

public class Main {

	public static void main(String[] args) {
		
//		Hash tables, hash maps, mapa de espalhamento
//		Dictionarys in python, with key and values
		
		Map m = new HashMap();
		m.put("macbook", 7000);
		m.put("asusrog", 9000);
		m.put("dellxps", 12000);
//		Can not add new key, it will only override
		m.put("dellxps", 13000);
		
		System.out.println(m);
		
		System.out.println(m.get("macbook"));
	}
}
