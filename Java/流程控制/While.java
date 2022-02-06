package Java.流程控制;
public class While {
    public static void main(String[] args) 
    {
        int sum = 0, i = 100;
        while(i<200)
        {
            i++;
            sum +=i;
        }
        System.out.println(sum);
    }
}
