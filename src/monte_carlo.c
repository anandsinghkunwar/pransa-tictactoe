#include<stdio.h>
#include<time.h>

char check_winner(char matrix[][3])
{
	if(matrix[0][0]==matrix[0][1]&&matrix[0][1]==matrix[0][2]&&matrix[0][2]!='s')
		return matrix[0][0];
	if(matrix[1][0]==matrix[1][1]&&matrix[1][1]==matrix[1][2]&&matrix[1][2]!='s')
		return matrix[1][0];
	if(matrix[2][0]==matrix[2][1]&&matrix[2][1]==matrix[2][2]&&matrix[2][2]!='s')
		return matrix[2][0];

	if(matrix[0][0]==matrix[1][0]&&matrix[1][0]==matrix[2][0]&&matrix[2][0]!='s')
		return matrix[0][0];
	if(matrix[0][1]==matrix[1][1]&&matrix[1][1]==matrix[2][1]&&matrix[2][1]!='s')
		return matrix[0][1];
	if(matrix[0][2]==matrix[1][2]&&matrix[1][2]==matrix[2][2]&&matrix[2][2]!='s')
		return matrix[0][2];

	if(matrix[0][0]==matrix[1][1]&&matrix[1][1]==matrix[2][2]&&matrix[2][2]!='s')
		return matrix[0][0];
	if(matrix[0][2]==matrix[1][1]&&matrix[1][1]==matrix[2][0]&&matrix[2][0]!='s')
		return matrix[0][2];

	int x,y;
	for(x=0;x<3;x++)
	{
		for(y=0;y<3;y++)
		{
			if(matrix[x][y]=='s')
				return 's';
		}
	}

	return 't';
}

char check_win_main(char main_matrix[][3])
{
	char copy_main[3][3];

	int x,y;
	for(x=0;x<3;x++)
	{
		for(y=0;y<3;y++)
		{
			if(main_matrix[x][y]=='t')
			{
				copy_main=[x][y]='s'
			}

			else
			{
				copy_main[x][y]=main_matrix[x][y];
			}
		}
	}

	if(check_winner(copy_main)=='o')
		return 'o';
	if(check_winner(copy_main)=='x')
		return 'x';

	int flag=0;

	for(x=0;x<3;x++)
	{
		for(y=0;y<3;y++)
		{
			if(matrix[x][y]=='s')
			{
				flag=1;
				break;
			}
		}
	}

	if(flag==0)
		return 't';

	return 's';
}

char random_moves(char matrix[][3][3][3],char main_matrix[][3],firstmove[])
{
	int iplay=-1;
	int jplay=-1;
	int xrand,yrand;

	matrix[firstmove[0]][firstmove[1]][firstmove[2]][firstmove[3]]='o';

	if(check_winner(matrix[firstmove[0]][firstmove[1]])=='o')
	{
		main_matrix[firstmove[0]][firstmove[1]]='o';
		if(check_win_main(main_matrix)=='o')
			return 'o';
		
		else if(check_win_main(main_matrix)=='t')
			return 't'
	}

	else if(check_winner(matrix[firstmove[0]][firstmove[1]])=='t')
	{
		main_matrix[firstmove[0]][firstmove[1]]='t';
		if(check_win_main(main_matrix)=='t')
			return 't'
	}

	if(main_matrix[firstmove[2]][firstmove[3]]!='s')
	{
		iplay=-1;
		jplay=-1;
	}
	
	else
	{
		iplay=firstmove[2];
		jplay=firstmove[3];
	}

	//Division between firstmove and loop

	while(1)
	{
		if(iplay==-1 && jplay==-1)
		{
			//Randomisation
		}

		else
		{
			//Randomistaion
		}

		matrix[iplay][jplay][xrand][yrand]='x';
		if(check_winner(matrix[iplay][jplay])=='x')
		{
			main_matrix[iplay][jplay]='x';
			if(check_win_main(main_matrix)=='x')
				return 'x';
			else if(check_win_main(main_matrix)=='t')
				return 't'
		}

		else if(check_winner(matrix[iplay][jplay])=='t')
		{
			main_matrix[iplay][jplay]='t';
			if(check_win_main(main_matrix)=='t')
				return 't'
		}

		if(main_matrix[xrand][yrand]!='s')
		{
			iplay=-1;
			jplay=-1;
		}
		
		else
		{
			iplay=xrand;
			jplay=yrand;
		}

		//Division between first and second move

		if(iplay==-1 && jplay==-1)
		{
			//Randomisation
		}

		else
		{
			//Randomistaion
		}

		matrix[iplay][jplay][xrand][yrand]='o';
		if(check_winner(matrix[iplay][jplay])=='o')
		{
			main_matrix[iplay][jplay]='o';
			if(check_win_main(main_matrix)=='o')
				return 'o';
			else if(check_win_main(main_matrix)=='t')
				return 't'
		}

		else if(check_winner(matrix[iplay][jplay])=='t')
		{
			main_matrix[iplay][jplay]='t';
			if(check_win_main(main_matrix)=='t')
				return 't'
		}

		if(main_matrix[xrand][yrand]!='s')
		{
			iplay=-1;
			jplay=-1;
		}
		
		else
		{
			iplay=xrand;
			jplay=yrand;
		}

	}
}

int main()
{
	char inputloc[]="../data/matrixforai.txt";
	char outputloc[]="../data/aimove.txt";

	FILE *fpinput=fopen(inputloc,"r");
	FILE *fpoutput=fopen(outputloc,"w+");

	char matrix[3][3][3][3];
	char main_matrix[3][3];

	int iplay,jplay;
	char temp;

	fscanf(fpinput,"%d %d",&iplay,&jplay);
	fscanf(fpinput,"%c",&temp);

	int i,j,k,l;

	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			for(k=0;k<3;k++)
			{
				for(l=0;l<3;l++)
				{
					fscanf("%c",&matrix[i][k][j][l]);
				}
			}
			fscanf("%c",&temp);
		}
	}

	for (i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			main_matrix[i][j]=check_win(matrix[i][j]);
		}
	}

	int positions[81][4];
	int noofpositions=0;

	if(iplay!=-1 && jplay!=-1)
	{
		for(i=0;i<3;i++)
		{
			for(j=0;j<3;j++)
			{
				if(matrix[iplay][jplay][i][j]=='s')
				{
					positions[noofpositions][0]=iplay;
                                        positions[noofpositions][0]=jplay;
                                        positions[noofpositions][0]=i;
                                        positions[noofpositions][0]=j;
					noofpositions++;
				}
			}
		}
	}

	else
	{
		for(i=0;i<3;i++)
		{
			for(j=0;j<3;j++)
			{
				if(main_matrix[i][j]=='s')
				{
					for(k=0;k<3;k++)
					{
						for(l=0;l<3;l++)
						{
							if(matrix[i][j][k][l]=='s')
							{
								positions[noofpositions][0]=i;
                                                                positions[noofpositions][1]=j;
                                                                positions[noofpositions][2]=k;
                                                                positions[noofpositions][3]=l;
								noofpositions++;
							}
						}
					}
				}
			}
		}
	}

	double best_prob=0.0;
	int best_pos[4]={-1,-1,-1,-1};

	char copy_matrix[3][3][3][3];
	char copy_main[3][3];
	int currpos;

	for(currpos=0;currpos<noofpositions;currpos++)
	{
		double timepermove=5.0/noofpositions;

		int noofwins=0,nooflosses=0,noofties=0;

		time_t currtime,inittime;
		time(&inittime);

		while(difftime(time(&currtime),inittime)<timepermove)
		{
			for(i=0;i<3;i++)
			{
				for(j=0;j<3;j++)
				{
					for(k=0;k<3;k++)
					{
						for(l=0;l<3;l++)
						{
							copy_matrix[i][j][k][l]=matrix[i][j][k][l];
						}

					}
				}
			}

			for(i=0;i<3;i++)
			{
				for(j=0;j<3;j++)
				{
					copy_main[i][j]=main_matrix[i][j];
				}
			}

			temp=random_moves(copy_matrix,copy_main,positions[currpos]);

			if(temp=='o')
				noofwins+=1;
			else if (temp=='x')
				nooflosses+=1;
			else
				noofties+=1;
		}
		
		double prob=(1.0*noofwins)/(noofwins+nooflosses+noofties);	

		printf("noofgames: %d %d %d=%d",noofwins,nooflosses,noofties,noofwins+nooflosses+noofties);	

		if(prob>best_prob)
		{
			best_prob=prob;
			best_pos[0]=positions[currpos][0];
                        best_pos[1]=positions[currpos][1];
                        best_pos[2]=positions[currpos][2];
                        best_pos[3]=positions[currpos][3];
		}	
	}

	fprintf(foutput,"%d %d %d %d\n",bestpos[0],bestpos[1],bestpos[2],bestpos[3]);

	fclose(fpinput);
	fclose(fpoutput);
	return 0;
}
