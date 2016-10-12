//编写一个ieqiu字符串长度的函数，strlen(),再用strlen()函数编写一个函数revers(s)的倒序递归程序，使字符串s逆序。
#include <iostream>
#include <string>

int strlen(char *str);
void revers(char *b);
using namespace std;

int main()
{
    char str[] = {"1234567890"};
    cout << str << "length of str:" << strlen(str)<< endl;
    cout << str << endl;//倒序前
    revers(str);
    cout << str << endl;//倒序后
    return 0;
}

int strlen(char *str)
{
    int len = 0;
    while(str[len] != '\0')
    {
        len++;
    }
    return len;
}

void revers(char *b)
{
    char c;
    int j,len;
    len = strlen(b);
    j = len/2 - 1;
    while(j>=0)
    {
        c = *(b+j);
        *(b+j) = *(b+len-j-1);
        *(b+len-j-1) = c;
        j--;
    }
    b[len] = '\0';
}
