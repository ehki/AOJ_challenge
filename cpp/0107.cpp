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
    int a, b, c;
    int n;
    int r;
    while (scanf("%d %d %d", &a, &b, &c))
    {
        if (a == 0 and b == 0 and c == 0)
            return 0;
        scanf("%d", &n);
        int r1;
        r1 = a * a + b * b;
        r1 = min(r1, b * b + c * c);
        r1 = min(r1, c * c + a * a);
        for (int i = 0; i < n; i++)
        {
            scanf("%d", &r);
            printf("%s\n", 4 * r * r > r1 ? "OK" : "NA");
        }
    }
    return 0;
}