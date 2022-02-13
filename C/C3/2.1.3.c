#include <stdio.h>
#include <stdlib.h>
//2.1.3 实数类型
//单双精度, long double
//P17
//主程序
void main()
{
    void Test0();
    void Test1();
    void Test2();
    void Test3();
    // Test0();
    // Test1();
    Test2();
    // Test3();
    //return 0;
}
void Test0()
{
    //测试3种实型的字节数 f 4个字节 double 8 和 long double 16个(64位)
    float f = 1.0f;
    double d = -1.0;
    long double ld = -1.12e-6l;
   
    printf("%i %i %d\n", sizeof(f), sizeof(d), sizeof(ld));
}
void Test1()
{
    //测试三种浮点数的负数赋值与格式化输出
    float f = -1.0f;   // 4294967295
    double d = -1.0;     // 4294967295
    long double ld = -1.0l;   // 4294967295
    printf("%f %lf %lf\n%g %e\n", f, d, ld, f, d);
}
void Test2()
{
    float f = 3.12f;
    int i = 4;
    double d = f + i ;
    printf("%f\n", d);
}
void Test3()
{
   
}