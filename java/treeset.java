import java.util.TreeSet;

class SetExample {
    public static void main(String[] arguments) {
		
		TreeSet<String> strings = new TreeSet<String>();
		
		strings.add("Evan");
		strings.add("Eugene");
		strings.add("Adam");
		//strings.add("Adam"); irrespective of duplicate item, it will show set removing duplicates
		
		System.out.println(strings.size());
		System.out.println(strings.first());
		System.out.println(strings.last());

		strings.remove("Eugene");
		for (String s : strings) {
			System.out.println(s);
		}
	}
}