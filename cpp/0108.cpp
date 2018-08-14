#include <cstdio>
#include <vector>
#include <algorithm>
#include <cstring>
#include <string>
#include <cctype>
#include <sstream>
#include <cmath>
#include <climits>
#include <set>
#include <iostream>
#include <map>
#include <functional>
#include <cstdlib>
#include <numeric>
#include <queue>
#include <complex>
#include <sstream>
#include <stack>

using namespace std;

#define reep(i, f, n) for (int i = f; i < n; ++i)
#define rep(i, n) reep(i, 0, n)

int main()
{
    int n;
    int r;
    int tmp1[15000] = {};
    int tmp2[15000] = {};
    while (scanf("%d", &n))
    {
        if (n == 0)
            break;
        cin.ignore();
        for (int i = 0; i < n; i++)
        {
            scanf(" %d", &r);
            tmp1[i] = r;
        }
        int m = 0;
        int f = 1;
        while (f)
        {
            int chk = 0;
            for (int i=0; i < n; i++)
            {
                int cnt = 0;
                for (int j=0; j < n; j++)
                    if (tmp1[j] == tmp1[i])
                        cnt++;
                // printf("%d ",cnt);
                tmp2[i] = cnt;
                if (tmp2[i] != tmp1[i])
                    chk++;
                // printf("HOGE");
            }
            if (chk == 0)
            {
                printf("%d\n", m);
                for (int i=0; i < n - 1; i++)
                    printf("%d ", tmp2[i]);
                printf("%d\n", tmp2[n - 1]);
                f = 0;
                break;
            }
            else
            {
                m++;
                for (int i=0; i < n; i++)
                    tmp1[i] = tmp2[i];
            }
        }
    }
    return 0;
}