#include <iostream>
#include <math.h>
using namespace std;

class Norm2
{
   

    public:
        Norm2()
        {

        }

        Norm2(int size)
        {
            arr = new int[size];
            for(int i = 0; i < size; i++)
            {
                arr[i] = 1;
            }

            c = 0;
            for(int i=0; i < size;i++)
            {
                c = c + arr[i]*arr[i];
            }
            
            c = c/size;
            c = sqrt(c);
           
        }

        void print()
        {
            cout << c  << endl;
        }
        
    private:
        int *arr;
        double c;
};

int main()
{
    Norm2* no = new Norm2(1000);
    no->print();
    return 0;
}
