package Java.数学题;

import java.util.Scanner;
//import Java.数学题.判断质数;

public class 哥德巴赫猜想 
{
    public static void main(String[] args) 
    {
        long start = System.currentTimeMillis();
        long N = 1_000_000L;
        //Scanner input = new Scanner(System.in))
        //int N = input.nextInt();
        if(N%2!=0) N -= 1; 
        for(int i = 4;i <= N; i+=2)
        {
            //System.out.println(i);
            boolean is = false;
            for(int j = 2;j <= i/2; j++)
            {
                if(判断质数.素数(j)&&判断质数.素数(i-j)) 
                {
                    is = true;
                    //System.out.println(i+"="+j+"+"+(i-j));
                    break;
                }
                    else continue;
            }
            if(!is) 
            {
                System.out.println("Error!"+i);
                return;
            }
        }
        long end = System.currentTimeMillis();
        System.out.println("Time: "+(end - start)+"ms");
    }
}
