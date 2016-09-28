#include <iostream>
#include <cmath>

using namespace std;

class  Sparse
{
    public:

        Sparse (int size)
        {
            m_sr = size;//矩阵的行数
            m_sc = size;//矩阵的列数
            m_nnz = 2*3 + 2*4 + (size - 4)*5;//非零元个数
            m_row = new int[m_nnz];//非零元所在行位置
            m_col = new int[m_nnz];//非零元所在列位置
            m_value = new int[m_nnz];//非零元的值
            for (int i = 0; i < size; i++)
            {
                for (int j = 0; j < size; j++)
                {
                    if (i == j)
                        m_value[i] = 4;
                    else
                        m_value[i] = -1;
                }
                
            }

        }

        void show()
        {
            for (int i = 0; i < size; i++)
            {
                for (int j = 0; j < size; j++)
                {
                    A[i][j] = 0;
                }
            }

            for (int i = 0; i < m_nnz; i++)
            {
                A[m_row[i]][m_col[i]] = m_value[i];
            }
            cout << m_nnz << endl;
            cout << A[0][0] << endl;
            cout << A[0][6] << endl;
        }

        ~Sparse()
        {
            delete m_row;
            delete m_col;
            delete m_value;
        }


    private:
        
            int *m_row;
            int *m_col;
            int *m_value;
            int m_sr;//稀疏矩阵行数
            int m_sc;//稀疏矩阵列数
            int m_nnz;//非零元个数
            int size;
            int **A;
            int *sp;
};

int main()
{
    int size;
    cin >> size;
    Sparse sp(size);
    sp.show();
    return 0;
}
