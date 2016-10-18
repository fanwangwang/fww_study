#ifndef STOCK00_H_
#define STOCK00_H_

#include <iostream>
#include <cmath>

class Sparse
{
   private:
        double N;
    public:
        void sparse(int i ,int j);
        void vec(int N,double *x,double *y);
        void show();
}

#endif
