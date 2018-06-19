class FooCorporation{
    public static void salary(double base,int time){
        if(time>60 || base<8.0){
            System.out.println("Error!");
        }
        else if (time>40){
            System.out.println((base * 40) + (base * 1.5 * (time-40)));
        }
       else{
            System.out.println(base*time);
       }
    }
    
    public static void main(String[] arguments){
        salary(7.50,35);
        salary(8.20,47);
        salary(10.00,73);
    }
}
