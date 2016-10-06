#include <iostream>
#include <cmath>
int sum1(int n1);
int sum2(int n2);
double sum3(int n3);
using namespace std;

int main()
{
    int s1,s2;
    double s3,s;
    sum1(100);
    sum2(50);
    sum3(10);
    s = s1 + s2 +s3;
    cout << "s1 + s2 + s3 = " << s << endl;
    return 0;
}

int sum1(int n1)
{
    int s1 = 0;
    for(int i = 0;i < n1+1; i++)
    {
        s1 = s1 + i;
    }
    cout << "s1=" << s1 << endl;
    return s1;
}

int sum2(int n2)
{
    int s2 = 0;
    for(int i = 0;i < n2+1;i++)
    {
        s2 = s2 + i*i;
    }
    cout << "s2=" << s2 << endl;
    return s2;
}

double sum3(int n3)
{
    double s3 = 0;
    for(int i = 1;i < n3+1;i++)
    {
        s3 =s3 + 1.0/i;
    }
    cout << "s3=" << s3 << endl;
    return s3;
}

