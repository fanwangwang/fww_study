#include <iostream>
#include <cmath>
using namespace std;
int main()
{
    int i,j;
    int A[10][10];
    for(i=0;i<10;i++)
    {
        for(j=0;j<10;j++)
        {
            A[i][j] = 0;
            if(i==j)
            {
                A[i][j] = 4;
            }
            else if(abs(i-j)<=2)
            {
                A[i][j] = -1;
            }
                     
            cout << A[i][j] << "\t";
        }

        cout << endl;

    }
	return 0;
}
