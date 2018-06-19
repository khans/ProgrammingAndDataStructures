package book_library;
import java.io.BufferedReader;

import java.io.FileReader;
import java.io.IOException;

public class MagicSquares {
    public static void main(String[] args) throws IOException{
    	boolean isMagic = true;
        int lastSum = -1;
		FileReader fr= 
				new FileReader("/Users/safa/Documents/safa/workspace/mit_java/mit/src/book_library/Mercury.txt");
		BufferedReader br = new BufferedReader(fr);
		String line = null;
		
		while((line = br.readLine())!=null){
			String[] fileinput = line.split("\t");
			
			int sum=0;
			//for loop begins
			for (String each:fileinput){
				if (each == null){
					continue;
				}
				else if (each.equals("")){
					continue;
				}
				else{
				int e = Integer.parseInt(each);
				sum = sum+e;
				}
			}//for loop ends
			System.out.println(sum);
			if (lastSum == -1){
				lastSum = sum;
			}else if(lastSum != sum){
				isMagic = false;
				break;
			}
			
		}
		
		System.out.println("For this file, let's see if it is a Magic Square "+isMagic);
		br.close();	
	}
		
}


