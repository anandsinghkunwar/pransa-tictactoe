#include<stdio.h>
#include<stdlib.h>
#include<time.h>

int main()
{
	getchar();
	getchar();

	int a,b;
	scanf("%d %d",&a,&b);
	getchar();

	char matrix[3][3][3][3];

	int i,j,k,l;

	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			for(k=0;k<3;k++)
			{
				for(l=0;l<3;l++)
				{
					scanf("%c",&matrix[i][k][j][l]);
				}
			}
			getchar();
		}
	}
/*
	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			for(k=0;k<3;k++)
			{
				for(l=0;l<3;l++)
				{
					printf("%c",matrix[i][j][k][l]);
				}
				printf("\n");
			}
			printf("\n");
		}
	}
*/
	srand(time(NULL));
	
	if(a==-1&&b==-1)
	{
		i=rand()%3;
		j=rand()%3;
		k=rand()%3;
		l=rand()%3;
		while(matrix[i][j][k][l]!='-')
		{
                	i=rand()%3;
			j=rand()%3;
	                k=rand()%3;
			l=rand()%3;
		}

		printf("%d %d %d %d\n",i,j,k,l);
	}

	else
	{
		i=rand()%3;
		j=rand()%3;
		while(matrix[a][b][i][j]!='-')
		{
			i=rand()%3;
			j=rand()%3;
		}
		printf("%d %d %d %d\n",a,b,i,j);
	}

	return 0;
}
