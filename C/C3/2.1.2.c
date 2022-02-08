#include <stdio.h>
#include <stdlib.h>
//2.1.2 整数类型
//长短无符号整形
//P16
//主程序
void main()
{
    // Test0();
    // Test1();
    // Test2();
    Test3();
    //return 0;
}
void Test0()
{
    //测试6种整型的字节数 short 2个字节 int 和 long 4个(64位)
    short s = -1;
    int i = -1;
    long l = -1l;
    //long int li = -1l; 这和long有什么区别吗?
    unsigned short us = -1;
    unsigned int ui = -1;
    unsigned long ul = -1l;
    printf("%d %d %d\n", sizeof(s), sizeof(i), sizeof(l));
    printf("%u %u %u\n", sizeof(us), sizeof(ui), sizeof(ul));
}
void Test1()
{
    //测试三种整型的负数赋值与格式化输出
    short s = -1;   // 4294967295
    int i = -1;     // 4294967295
    long l = -1l;   // 4294967295
    unsigned short us = -1; // 65535
    unsigned int ui = -1;   // 4294967295
    unsigned long ul = -1l; // 4294967295
    printf("%u %u %u\n%u %u %u\n", s, i, l, us, ui, ul);
    printf("%d %d %d\n%d %d %d\n", s, i, l, us, ui, ul);
}
void Test2()
{
    short s = 1;
    int i = 1;
    unsigned short us = 1;
    long l = 1;
    for(;;)
    {
        s--;
        us++;
        printf("%u %u\n", s, us);
        //很奇怪, 使用u来输出short时范围自动扩大了?
    }
}
void Test3()
{
    //不同进制的赋值
    int i = 0123;
    int i1 = 0x123;
    int i2 = 0b0101;
    printf("%u %u %u\n", i, i1, i2);
    printf("%o %x %d\n", i, i1, i2);
}