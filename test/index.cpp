#include <iostream>

using namespace std;
int main()
{
    int x = 3;
    int &y = x;//定义一个引用y，y是x的引用
    cout << x << endl;
    cout << y << endl;

    y = 20;//修改y的值
    cout << x << endl;
    cout << y << endl;
    return 0;
}
