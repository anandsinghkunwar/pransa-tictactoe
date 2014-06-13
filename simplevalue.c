#include <stdio.h>
int scoreline (int com, int opp);
int value (char matrix[3][3]);
int scoreline (int com, int opp)
{
	if (com == 3)
		return 100;
	else if (opp == 3)
		return -100;
	else if (com == 2 && opp == 0)
		return 10;
	else if (com == 0 && opp == 2)
		return -10;
	else if (com == 1 && opp == 0)
		return 1;
	else if (com == 0 && opp == 1)
		return -1;
	else
		return 0;
}

int value (char matrix[3][3])
{
	int i, j, k, com = 0, opp = 0, score = 0;

	for (i = 0; i < 3; i++)
	{
		com = 0, opp = 0;
		for (j = 0; j < 3; j++)
		{
			if (matrix[i][j] == 'x')
				com++;
			else if (matrix[i][j] == 'o')

				opp++;
		}

		score = score + scoreline(com, opp);

	
	}

	for (j = 0; j < 3; j++)
	{
		com = 0, opp = 0;
		for (i = 0; i < 3; i++)
		{
			if (matrix[i][j] == 'x')
				com++;
			else if (matrix[i][j] == 'o')
				opp++;
		}

		score = score + scoreline(com, opp);	
	}
	
	com = 0, opp = 0;
	for (i = 0; i < 3; i++)
	{
		if (matrix[i][i] == 'x')
			com++;
		else if (matrix[i][i] == 'o')
			opp++;
	}

	score = score + scoreline(com, opp);

	com = 0, opp = 0;
	for (i = 0; i < 3; i++)
	{
		if (matrix[i][2-i] == 'x')
			com++;
		else if (matrix[i][2-i] == 'o')
			opp++;
	}

	score = score + scoreline(com, opp);
	
	return score;
}

int main()
	{
		char matrix[3][3],temp;
		int i,j;
		for(i=0;i<3;i++)
			for(j=0;j<3;j++)
				scanf("%c%c",&matrix[i][j],&temp);
		printf("%d",value(matrix));
		
		return 0;
	}
