class StringTest { 
  public static void main(String[] args) {
    String s1 = "Welcome to Java!";
    String s2 = s1;
    
    String s3 = "Welcome to Java!";
    String s4 = "Welcome to Java!";

    String s5 = new String("Welcome to Java!");
    String s6 = new String("Welcome to Java!");
    String s7 = new String("Yahoo");
    
    if (s1 == s2)
      System.out.println("s1 and s2 reference to the same String object"); // yes
    else
      System.out.println("s1 and s2 reference to different String objects");

    if (s3 == s4)
      System.out.println("s3 and s4 reference to the same String object"); //yes?
    else
      System.out.println("s3 and s4 reference to different String objects");
      
    if (s5 == s6)
      System.out.println("s5 and s6 reference to the same String object"); 
    else
      System.out.println("s5 and s6 reference to different String objects");
      
    //Checking something new
    System.out.println(s5.equals(s6) == s6.equals(s5));
  }
}
