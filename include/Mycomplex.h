#include <iostream>

#ifndef mycomplex_h
#define mycomplex_h

calss complex
{
    private:
        {
            float real;
            float image;
        }

    public:
        {
            complex(float = 0.0,float = 0.0);//构造函数
            float getreal const;//获取实部
            float getimage const;//获取虚部
            void setcomplex(float r,float i);//重新设置复数

        };
        const complex le(0,1);

}
#endif

