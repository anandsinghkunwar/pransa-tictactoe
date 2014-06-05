#include<stdio.h>
struct Node
	{
		int val;
		struct Node * child[81];
	}root, present, next, temp;
int minimax();
int minmove();
int maxmove();


int minmove()
	{
		int i,min,move;
		for(i=0;i<81;i++)
			{
				next=present->child[i];
				if (next->val<min)
					{
						min=next->val;
						move=i;
					}
			}
		return move;
	}

int maxmove()
        {
                int i,max,move;
                for(i=0;i<81;i++)
                        {
                                next=present->child[i];
                                if (next->val>max)
                                        {
                                                max=next->val;
                                                move=i;
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
