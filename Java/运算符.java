package Java;
public class 运算符
{
    public static void main(String[] args) 
    {
        byte b1 = 127;
        b1++;//b1=-128 数据类型不变
        double d1 =32.1;
        d1 %= 3;//2.1000000000000014 java小数也可取余

        d1 *=b1+3;//等价于d1=d1*(b1+3)

        int result = d1==0?100:2*b1;//d1=0,则100,否则2*b1

        //将两个变量交换
        int k = 1;
        int j = 2;
        k ^= j;
        j ^= k;
        k ^= j;
        System.out.println(j+" "+k);
    }
    
}