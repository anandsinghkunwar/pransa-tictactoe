#include<stdio.h>
#include<stdlib.h>
#include<string.h>
struct Node
	{
		int val;
		char depth;
		struct Node * child[81];
	};
int minimax(struct Node *,char,char [3][3][3][3],char [3][3],char,char);
int minmove(struct Node *);
int maxmove(struct Node *);
char check_winner(char [][3]);
char check_win_main(char [][3]);
int * check_empty(char [3][3][3][3], char [][3],int, int);

int * check_empty(char matrix[3][3][3][3],char main_matrix[3][3], int a, int b)
        {
                int i,j,k,l,count=0;
                static int * moves = (int *) malloc(sizeof(int)*81);
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

                                                                        if(matrix[i][j][k][l]=='s'&&main_matrix[i][j]=='s')
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

int minmove(struct Node * present)
        {
		int move,i,min=2,mini;
		struct Node *next;
		
		for(i=0;present->child[i]!=NULL&&i<81;i++)
		{
			next=present->child[i];
			if(next->val<min)
			{
				mini=i;
				min=next->val;
			}
		}
                
		return mini;
        }

int maxmove(struct Node * present)
        {
                int move,i,max=-2,maxi,count,maxdepth,mindepth;
		maxdepth=-1;
		mindepth=82;
                struct Node *next;
                for(i=0;present->child[i]!=NULL&&i<81;i++)
                {
                        next=present->child[i];
                        if(next->val>=max)
                        {
                                if(next->val==1&&next->depth<mindepth)
				{
					maxi=i;
                                	max=next->val;
					mindepth=next->depth;
                        	}
				else
					if(next->val!=1&&next->depth>maxdepth)
					{
						maxi=i;
						max=next->val;
						maxdepth=next->depth;
					}
			}
                }


                return maxi;
        }

int minimax(struct Node *current,char turn,char matrix[3][3][3][3],char main_matrix[3][3],char x,char y)
	{
		int i,*empty,a,b,c,d,k,move;
		empty = NULL;
		char copy[3][3][3][3];
		for(i=0;i<81;i++)
			current->child[i]=NULL;
		if (check_winner(matrix[x][y])=='x')
			{
				main_matrix[x][y]='x';
				if(check_win_main(main_matrix)=='x')
					{
						current->val=1;
						current->depth=0;
						return 1;
					}
				else
					if(check_win_main(main_matrix)=='t')
					{
						current->val=0;
						current->depth=0;
						return 0;
					}

			}
		else
			if (check_winner(matrix[x][y])=='o')
				{
					main_matrix[x][y]=='o';
					if(check_win_main(main_matrix)=='o')

						{
							current->val=-1;
							current->depth=0;
							return -1;
						}
					else
						if(check_win_main(main_matrix)=='t')
						{
							current->val=0;
							current->depth=0;
							return 0;
						}
				}
	
		printf("#\n");				
		empty=check_empty(matrix,main_matrix,x,y);
		printf("#\n");
		for(i=0;empty[i]!=-1&&i<81;i++)
			{
				a=empty[i]/1000;
				b=empty[i]/100 - a*10;
				c=empty[i]/10 - a*100 - b*10;
				d=empty[i]-a*1000 - b*100 - c*10;
				memcpy(copy,matrix,sizeof(matrix));
				current->child[i]=(struct Node *) malloc(sizeof(struct Node));
				if(turn == 'x')
					{
					copy[a][b][c][d]='x';
					return minimax(current->child[i],'o',copy,main_matrix,a,b);
					}
					else
					{
					copy[a][b][c][d]='o';
					return minimax(current->child[i],'x',copy,main_matrix,a,b);
					}
			}
	
		if(turn=='x')
			k=maxmove(current);
		else
			k=minmove(current);
		current->depth=(current->child[k])->depth + 1;
		move=empty[k];
		free(empty);
		empty=NULL;
		return move;
			
	}
int main()
	{
	char matrix[3][3][3][3];
	char main_matrix[3][3];

	int iplay,jplay,turn,move;
	char temp;
	scanf("%c",&turn);
	scanf("%c",&temp);
	scanf("%d %d",&iplay,&jplay);
	scanf("%c",&temp);
        int i,j,k,l,a,b,c,d;

        for(i=0;i<3;i++)
        {
                for(j=0;j<3;j++)
                {
                        for(k=0;k<3;k++)
                        {
                                for(l=0;l<3;l++)
                                {
                                        scanf("%c",&matrix[i][k][j][l]);
                                        if(matrix[i][k][j][l]=='X')matrix[i][k][j][l]='x';
                                        else if(matrix[i][k][j][l]=='O')matrix[i][k][j][l]='o';
                                        else if(matrix[i][k][j][l]=='-')matrix[i][k][j][l]='s';
                                }
                        }
                        scanf("%c",&temp);
                }
        }
        for (i=0;i<3;i++)
        {
                for(j=0;j<3;j++)
                {
                        main_matrix[i][j]=check_winner(matrix[i][j]);
                }
        }
	struct Node *root= (struct Node *) malloc(sizeof(struct Node));
	move=minimax(root,turn,matrix,main_matrix,iplay,jplay);
	a=move/1000;
	b=move/100 - a*10;
	c=move/10 - a*100 - b*10;
	d=move-a*1000 - b*100 - c*10;
	printf("%d %d %d %d",a,b,c,d);
        return 0;

	}
