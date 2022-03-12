package practice;
import java.util.Scanner;  
public class StudyTonight
{  
    public static void main(String[] args) 
    {  
        try
        {
          System.out.println("Enter the two values : ");  
          Scanner sc = new Scanner(System.in);  
          double a = sc.nextDouble();  
          double b = sc.nextDouble();  
          System.out.println("sum is = " + Double.sum(a, b));  // will return the sum of a and b. 
        }
        catch(Exception e)
        {
          System.out.println("Invalid Input");
        }        
    }  
} 