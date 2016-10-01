#include <iostream>

using namespace std;

namespace A
{
    int x = 1;
    void fun()
    {
        cout << "A" << endl;
    }
}

namespace B
{
    int x = 2;
    void fun()
    {
        cout << "B" <<endl;
    }
    void fun2()
    {
        cout << "BB" << endl;
    }
}
int main(void)
{
    cout << A::x << endl;
    B::fun();
    B::fun2();
    return 0;
}
