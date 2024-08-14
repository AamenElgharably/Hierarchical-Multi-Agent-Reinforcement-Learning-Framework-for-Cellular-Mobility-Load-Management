#include "MY_CIO.h"
#include <iostream>

int celloffset[6][6]= {0};

void print_offset()
{
	for (int i=0;i<6;i++)
	{
		for(int j=0;j<6;j++){
			std::cout<<celloffset[i][j];
		}
		std::cout << std::endl;
	}


};
