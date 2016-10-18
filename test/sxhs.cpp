#include <iostream>
#include <cmath>
using namespace std;
void sxhs(int a,int b,int c);
int main()
{
    int a,b,c;
    sxhs(a,b,c);
    return 0;
}

void sxhs(int i,int j,int k)
{
    int d,f;
    for(i=1;i<10;i++)
        for(j=0;j<10;j++)
            for(k=0;k<10;k++)
            {
                d = 100*i + 10*j + k;
                f = i*i*i + j*j*j +k*k*k;
                if(d==f)
                {
                    cout << i << "," << j << "," << k << endl;
                    cout << d << "," << f << endl;
                }
            }
}
