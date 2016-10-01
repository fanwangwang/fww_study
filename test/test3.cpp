//使用一个函数找出一个整型数组中的最大值或者最小值
//
#include <iostream>

using namespace std;

int getMaxOrMin(int *arr,int count,bool isMax)//这里的isMax是行参
{
    int temp = arr[0];
    for(int i = 1; i < count; i++)
        if(isMax)
        {
            if(temp < arr[i])
            {
                temp = arr[i];
            }
        }
        else
        {
            if(temp > arr[i])
            {
                temp = arr[i];
            }
        }
    return temp;
}

int main()
{
    int arr[4] = {3,5,1,7};
    bool isMax = false;//这里的isMax是定义的一个布尔类型的值，跟行参的isMax不同
    cin >> isMax;
    cout << getMaxOrMin(arr,4,isMax) << endl;
    return 0;
}

