#include <stdio.h>

typedef struct a {
   int i;
   int j;
}a;

*a f(a x)
{
   a *r = x;
   return r;
}

int main(void)
{
   a *x = { 56,89 };
   a *y = f(x);
   printf("%d\n", y->j);
   return 0;
}