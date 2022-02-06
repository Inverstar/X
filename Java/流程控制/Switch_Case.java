package Java.流程控制;
public class Switch_Case
{
    public static void main(String[] args) 
    {
        int i = 10111;
        switch (i) {
            case 1:
                System.out.println(i);
                break;//不加则继续执行下面的语句
            default:
                System.out.println(i);
        }
    }
}