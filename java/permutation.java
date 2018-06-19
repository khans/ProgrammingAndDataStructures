import java.util.ArrayList;

class permutation {
    private String[] arr;
	private int size;
    public ArrayList<String> one_item_list(String[] array){
        size = 1;
        arr = new String[size];
        arr[0] = array[0];
        return arr[0];
    }
	
	public static void main(String[] args){
        int len = args.length;
		ArrayList<String> list = new ArrayList<String>();
        for(String s: args){
            list.add(s);
        }
        System.out.println(list);
			
		
		
	}

}
