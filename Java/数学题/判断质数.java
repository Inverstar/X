package Java.数学题;

import java.util.Scanner;

public class 判断质数 
{
    public static boolean 素数(int n)
    {
        for(int i = 2;i<=Math.sqrt(n);i++)
        {
            if(n%i == 0)
                {
                    //System.out.println(n+" "+i+"*"+n/i);
                    return false;
                }
        }
        return true;
    }
    public static void main(String[] args) 
    {
        try (Scanner input = new Scanner(System.in)) {
            int n = input.nextInt();
            boolean m = 素数(n);
            System.out.println(m);
        }
    }
}
