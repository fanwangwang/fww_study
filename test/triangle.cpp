//编写有字符型参数Ｃ和整形参数Ｎ的函数，让他们让他显示出由字符Ｃ组成的三角形，其方式为第一行有一个字符Ｃ，第二行有两个字符Ｃ，等等.
#include <iostream>

void triangle(char c,int n);

using namespace std;

int main()
{
    char a;
    triangle('a',10);
    return 0;
}

void triangle(char c, int n)
{
    int i,j;
    for(i = 0;i < n; i++)
    {
        for(j = 0;j <= i; j++)
        {
            cout << c;
        }
        cout << endl;
    }
}


