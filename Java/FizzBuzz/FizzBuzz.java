public class FizzBuzz 
{
    public static void main (String[] args)
    {
        for(int i=0; i <= 16; i++) 
        {

            //Tais Lösung
            /* 
            if(i%3==0)
            {
                if (i%5==0) 
                {
                    System.out.println("Fizz Buzz"); 
                }
                else
                    {
                    System.out.println("Fizz");
                    }
            }
            */

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