#include <iostream>

using namespace std;
int main()
{
    char ch = 'M';//对M声明一个ASCII码
    int i = ch;
    cout << "The ASCII code for " << ch << "is" << endl;

    cout << "Add one to the character code:" << endl;
    ch =ch + 1;//改变ch的值
    i = ch;

    cout << "The ASCII code for " << ch << "is" << i << endl;

    cout << "Displaying char ch using cout.put(ch):";
    cout.put(ch);//成员函数

    cout.put('!');//输出！
    cout << endl << "Done" << endl;
    return 0;

}

//cout.put()成员函数可以替代<<云算符
