//提示用户输入一个整数，将该整数分别以8进制，10进制，16进制打印在屏幕上
//提示用户输入一个布尔值，以布尔方式将值打印在屏幕上
#include <iostream>

using namespace std;

int main()
{
    cout <<"Please input an integer:"<<endl;
    int x = 0;
    cin >> x;

    cout << oct << x << endl;// 8进制
    cout << dec << x << endl;//10进制
    cout << hex << x << endl;//16进制

    cout << "Please input a number of bool 0 or 1:"<< endl;
    bool y = false;//布尔值
    cin >> y;
    cout << boolalpha << y <<endl;//输出一个布尔值
    return 0;
}
