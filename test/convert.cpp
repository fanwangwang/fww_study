#include <iostream>
int stonetolb(int);
using namespace std;

int main()
{
    int stone;//声明变量
    cout << "Enter the weight in stone:";//输出字符串
    cin >> stone;//输入一个stone值
    int pounds = stonetolb(stone);//声明变量,调用stonetolb函数
    cout << stone <<"stone =";//输出字符串
    cout << pounds << "pounds."<<endl;//输出pounds的结果
    return 0;
}
//自定义函数
int stonetolb(int sts)
{
    return 14*sts;
}
