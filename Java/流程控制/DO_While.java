package Java.流程控制;
public class DO_While 
{
   public static void main(String[] args) 
   {
    long start = System.currentTimeMillis();
    //计时器
    int i = 0;
    do
    {
        i++;
    }
    while(i<100000);
    //long start = System.currentTimeMillis();
    long end = System.currentTimeMillis();
    System.out.println("Time: "+(end - start)+"ms");
   } 
}
