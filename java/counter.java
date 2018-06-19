class Counter{
    int myCount=0;
    static int ourCount=0;
    public void increment(){
        myCount++;
        ourCount++;
    }
    
    public static void main(String[] arguments){
        Counter c1 = new Counter();
        Counter c2 = new Counter();
        
        c1.increment();
        c1.increment();
        c2.increment();
        
        System.out.println("c1  "+c1.myCount+ Counter.ourCount);
        System.out.println("c2  "+c2.myCount+ c2.ourCount);
        //System.out.println("c1"+Counter.myCount+ c1.ourCount)
    }
}    