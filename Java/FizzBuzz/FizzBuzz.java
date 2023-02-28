import java.util.Scanner;

public class FizzBuzz 

{
    public static void main (String[] args)
    {
        Scanner scan = new Scanner(System.in);
        
        while (!scan.hasNextInt()) {
          System.out.println("Input is not a number.");
          scan.nextLine();
        }

        int countto = scan.nextInt();

        for(int i=0; i <= countto; i++) 
        {

            if(i%3==0 && i%5==0)
            {
                System.out.println("Fizz Buzz");
            }

            else if(i%3==0)
            {
                System.out.println("Fizz");
            }
            //durch fünf teilbar
            else if(i%5==0)
            {
                System.out.println("Buzz");
            }
            
            else
            {
                System.out.println(i);
            }

        }
        
    }
}