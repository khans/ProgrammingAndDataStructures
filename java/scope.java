class Scope { 
    public static void main(String[] arguments){ 
        int x = 5; 
        if (x == 5){ 
            //int x = 6;  //results in error, because it can access x as 5
            int y = 72;
            System.out.println("x = " + x + " y = " + y);
        } 
        System.out.println("x = " + x);
    }
}