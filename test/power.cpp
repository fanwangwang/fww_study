//输出r的n次幂

#include <iostream>
#include <cmath>

void power(double r,int n);
using namespace std;

void power(double r,int n)
{
    double x = 1.0;
    for(int i = 0; i < n; i++)
    {
        x = x*r;
    }
    cout << x << endl;
}

int main(void)
{
    double r,x;
    int n;
    cout << "Please input the number of r and n:" << endl;
    cin >> r; 
    cin >> n;
    power(r,n);
    return 0;
}
