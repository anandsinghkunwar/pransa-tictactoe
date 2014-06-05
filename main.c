#include<stdio.h>
struct Node
	{
		int val;
		struct Node * child[3][3][3][3];
	}root, present, next, temp;
int minimax();
int minmove();
int maxmove();
char check_winner(char [][3]);
char check_win_main(char [][3]);

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

int mixmove(int matrix[3][3][3][3])
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


int maxmove(int matrix[3][3][3][3])
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
int main()
	{
		int a[3][3][3][3];
		printf("Trial");
		return 0;
	}
