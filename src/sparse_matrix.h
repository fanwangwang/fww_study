#include <iostream>

class Sparse_matrix 
{
public:
	Sparse_matrix()
	{
	int size = 6;
	AA = new int[size];
	AA[0] = 1;
	AA[1] = 2;
	AA[2] = 3;
	AA[3] = 4;
	AA[4] = 5;
	AA[5] = 6;
	JA = new int[size];
	JA[0] = 0;
	JA[1] = 1;
	JA[2] = 1;
 	JA[3] = 0;
	JA[4] = 2;
	JA[5] = 3;
	IA = new int[size];
	IA[0] = 0;
	IA[1] = 1;
	IA[2] = 2;
	IA[3] = 3;
	IA[4] = 6;
	}
	
	~Sparse_matrix()
	{
	delete AA[];
	delete JA[];
	delete IA[];
	}
	
	void print()
	{
	cout << Sparse_matrix[i][j] << endl;
	}
private:
	int *AA;
	int *JA;
	int *IA;
	int i;
	int j;
}; 
