class Marathon {
    
    public static int fastest(int[] times){
        int min = times[0]; //assign the first value to be minimum
        int i;
        int x=0;  //will be used to find the lowest value index
        int len = times.length;
        for(i=1;i<len;i++){
            if (times[i]<min){
                min = times[i];
                x=i;
            }
            else{
                continue; //go to the for loop using next i
            }            
        }
        return x;
    }
    
    public static int runner_up(int[] times){
        int j = fastest(times); //get the index of the fastest runner
        int i;
        int x=0;            // return the runner-up's index
        int second_min = times[0]; // using for comparison
        for(i=0;i<times.length;i++){
            if(times[i]<second_min && times[i]!=times[j]){
                second_min=times[i];
                x=i;
            }
            else{
                continue;
            }
        }
        return x;        
    }
    
    
    public static void main (String[] arguments){
        int j,k;
        String[] names = {
            "Elena", "Thomas", "Hamilton", "Suzie", "Phil", "Matt", "Alex",
            "Emma", "John", "James", "Jane", "Emily", "Daniel", "Neda",
            "Aaron", "Kate"
        };
        int[] times = {
            341, 273, 278, 329, 445, 402, 388, 275, 243, 334, 412, 393, 299,
            343, 317, 265
        };
        
        for(int i = 0; i < names.length; i++){
            System.out.println(names[i] + ": " + times[i]);    
        }
        
        j = fastest(times);
        k = runner_up(times);
        System.out.println("The fastest runner is " + names[j] +" with time in minutes as " + times[j]);
        System.out.println("The second fastest runner is " + names[k] +" with time in minutes as " + times[k]);
           
    }
}