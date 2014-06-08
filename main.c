#include<stdio.h>
#include<stdlib.h>
#include<string.h>
struct Node
	{
		int val;
		struct Node * child[3][3][3][3];
	}*root, *present, *next, *temp;
int minimax(struct Node *,char,char [3][3][3][3]);
int minmove();
int maxmove();
char check_winner(char [][3]);
char check_win_main(char [][3]);
int * check_empty(char [3][3][3][3], int, int);

int * check_empty(char matrix[3][3][3][3], int a, int b)
        {
                int i,j,k,l,count=0;
                int * moves = (int *) malloc(sizeof(int)*81);
		if(a==3&&b==3)
                {
                for(i=0;i<3;i++)
                        {
                        for(j=0;j<3;i++)
                                {
                                        for(k=0;k<3;i++)
                                                {
                                                        for(l=0;l<3;i++)
                                                                {

                                                                        if(matrix[i][j][k][l]=='s')
                                                                                {
                                                                                        moves[count]=i*1000+j*100+k*10+l;
                                                                                        count++;
                                                                                }
                                                                }
                                                }
                                }
                        }
                moves[count]=-1;
                }
                else
                {       for(i=0;i<3;i++)
                        {
                        for(j=0;j<3;i++)
                                {
                                        if(matrix[a][b][i][j]=='s')
                                        {
                                                moves[count]=a*1000+b*100+i*10+j;
                                                count++;
                                        }

                                }
                        }
                }
                return moves;
        }

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
                                copy_main[x][y]='s';
                        }

                        else
                        {
                                copy_main[x][y]=main_matrix[x][y];
                        }
                }
        }

        if(check_winner(copy_main)=='o')
        {
                return 'o';
        }
        if(check_winner(copy_main)=='x')
        {
                return 'x';
        }

        int flag=0;

        for(x=0;x<3;x++)
        {
                for(y=0;y<3;y++)
                {
                        if(main_matrix[x][y]=='s')
                        {
                                flag=1;
                                break;
                        }
                }
        }

        if(flag==0)
        {
                return 't';
        }

        return 's';
}

int minmove(char matrix[3][3][3][3])
        {
                int i,j,k,l,min=32767,move;
                for(i=0;i<3;i++)
                        {
                        for(j=0;j<3;i++)
                                {
                                        for(k=0;k<3;i++)
                                                {
                                                        for(l=0;l<3;i++)
                                                                {
                                                                        if(matrix[i][j][k][l]!='s')
                                                                                continue;
                                                                        next=present->child[i][j][k][l];
                                                                        if (next->val<min)
                                                                                {
                                                                                        min=next->val;
                                                                                        move=i*1000+j*100+k*10+l;
                                                                                }
                                                                }
                                                }
                                }
                        }
                return move;
        }


int maxmove(char matrix[3][3][3][3])
        {
                int i,j,k,l,max=-32767,move;
                for(i=0;i<3;i++)
                        {
			for(j=0;j<3;i++)
                        	{
					for(k=0;k<3;i++)
                        			{
							for(l=0;l<3;i++)
                        					{

                                					if(matrix[i][j][k][l]!='s')
										continue;
									next=present->child[i][j][k][l];
                                					if (next->val>max)
                                        					{
                                                					max=next->val;
                                               						move=i*1000+j*100+k*10+l;
                                        					}
								}
						}
				}
                        }
                return move;
        }
int minimax(struct Node *current,char turn,char matrix[3][3][3][3])
	{
		int i,*empty;
		char copy[3][3][3][3];
		for(i=0;i<81;i++)
			current->child[i]=NULL;
		if (checkwin()=='x')
			{
				current->val=1;
				return 1;
			}
		else
			if (checkwin()=='o')
				{
					current->val=-1;
					return -1;
				}
			else
				{
					
					empty=check_empty(matrix,a,b);
					for(i=0;empty[i]i!=-1&&i<81;i++)
						{
							memcpy(copy,matrix,sizeof(matrix));
							current->child[i]=(struct Node *) malloc(sizeof(struct Node));
							if(turn == 'x')
								{
								return minimax(current->child[i],'o',matrix);
								}
							else
								{
								return minimax(current->child[i],'x',matrix);
								}
						}
				}
	}
int main()
	{
		int i,j,k,l,x,y,matrix[3][3][3][3];
		scanf("%d %d",&x,&y);
		for(i=0;i<3;i++)
			for(j=0;j<3;i++)
				for(k=0;k<3;i++)
					for(l=0;l<3;i++)
                                        	scanf("%c",&matrix[i][j][k][l]);                  

		printf("Trial");
		return 0;
	}
