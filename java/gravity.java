//Program computes the position of  a falling object.
//Equation x(t)=0.5*at^2+vit+xi
class GravityCalculator{
    public static void main(String[] args){
        double gravity = -9.81; //m/s^2
        double initialVelocity=0.0;
        double fallingTime=10.0;
        double initialPosition=0.0;
        double finalPosition=0.0;
        finalPosition = (0.5*gravity*fallingTime*fallingTime)+(initialVelocity*fallingTime)+initialPosition;
        System.out.println("The object's position after" +fallingTime + "seconds is"+
        finalPosition + "m.");
    }
}