import java.util.ArrayList;

class ArrayListExample {

    public static void main(String[] arguments){
		ArrayList<String> strings = new ArrayList<String>();
		strings.add("Evan");
		strings.add("Eugene");
		strings.add("Adam");

		System.out.println(strings.size());
		System.out.println(strings.get(0));
		System.out.println(strings.get(1));

		strings.set(0, "Goodbye");
		strings.remove(1);

		for (int i=0;i<strings.size();i++){
			System.out.println(strings.get(i));
		}
		
		for (String s : strings){ 
			System.out.println(s); 
		} 
	}
}