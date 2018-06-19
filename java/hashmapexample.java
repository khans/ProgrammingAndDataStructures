import java.util.HashMap;
import java.util.Map;

class HashMapExample{
    public static void main(String[] arguments){ 
		HashMap<String, String> strings = new HashMap<String, String>(); 
		
		strings.put("Evan", "email1@mit.edu"); 
		strings.put("Eugene", "email2@mit.edu"); 
		strings.put("Adam", "email3@mit.edu"); 
		
		System.out.println(strings.size());
		
		strings.remove("Evan");

		System.out.println(strings.get("Eugene"));

		
		//looping through the key set values, keySet()
		System.out.println("Keys");
		for (String s : strings.keySet()) { 
		System.out.println(s);

		}

		System.out.println("Values");
		for (String s : strings.values()) {
		System.out.println(s);
		}

		System.out.println("Pairs");
		//use strings.entrySet() for pairs,keySet() for keys, values() for values
		for (Map.Entry<String, String> pairs : strings.entrySet()) {
		System.out.println(pairs); 
		} 
	} 
}
