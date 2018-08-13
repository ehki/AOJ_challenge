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
    int qa = 200;
    int qb = 300;
    int qc = 500;
    int pa = 380;
    int pb = 550;
    int pc = 850;
    int ua = 5;
    int ub = 4;
    int uc = 3;
    int ra = 20;
    int rb = 15;
    int rc = 12;

    int n;
    int tmp;
    while (scanf("%d", &n),n)
    {
        int ret = 10000;
        rep(i, n / qa + 1)
            rep(j, n / qb + 1)
                rep(k, n / qc + 1)
                    if (i * qa + j * qb + k * qc == n)
                    {
                        tmp = i * pa + j * pb + k * pc;
                        tmp -= ((i / ua) * ua * pa * ra) / 100;
                        tmp -= ((j / ub) * ub * pb * rb) / 100;
                        tmp -= ((k / uc) * uc * pc * rc) / 100;
                        ret = min(ret, tmp);
                    }
        printf("%d\n", ret);
    }
    return 0;
}