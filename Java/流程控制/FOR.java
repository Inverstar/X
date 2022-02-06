package Java.流程控制;
import java.util.Scanner;
//Fibonacci
public class FOR 
{
    public static void main(String[] args) 
    {
        long f1, f2, f3, n;
        Scanner S = new Scanner(System.in);
        n = S.nextLong();
        f1=f2=1;
        for(int i = 3;i <= n;i++)
        {
            f3 = f1 + f2;
            f1 = f2;
            f2 = f3;
            System.out.println(f3+" ");
            if(i%10==0) System.out.println();
        }
    }
}
