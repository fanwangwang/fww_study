//编写一个求方程ax2 + bx + c = 0的根的程序，分别求当b2-4ac大于零、
//等于零、和小于零时的方程的根。要求从主函数输入a,b,c的值并输出结果。  

#include <iostream>
#include <cmath>
void fun(int a,int b,int c);
using namespace std;

int main()
{
    int a;
    int b;
    int c;
    cout << "Please input:"<< endl;
    cin >> a >> b >> c;
    fun(a,b,c);
    return 0;
}

void fun(int a,int b,int c)
{
    double D;
    D = b*b - 4.0*a*c;
    int p;
    p = -b/(2.0*a);
    double q;
    q = sqrt(D)/(2.0*a);
    double x1;
    double x2;
    if(D < 0)
    {
        cout << "The equation has not real root!" << endl;
       // q = sqrt(-D)/(2*a); 
       // x1 = p + q;
       // x2 = p - q;
       // cout << x1 << "," << x2 << endl;
    }
    else
    {
        x1 = p + q;
        x2 = p - q;
        cout << x1 << "," << x2 << endl;
    }
}
