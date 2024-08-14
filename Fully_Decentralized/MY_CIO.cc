#include "MY_CIO.h"
#include <iostream>
#include <stdint.h>
double celloffset[6][6]= {0.0};
int Handover [6][6]=
{
   {0,1,0,1,0,1},
   {1,0,1,1,1,1},
   {0,1,0,0,1,1},
   {1,1,0,0,1,0},
   {0,1,1,1,0,1},
   {1,1,1,0,1,0}
};
uint8_t HO_offset[6]={3,5,3,3,4,4};
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
