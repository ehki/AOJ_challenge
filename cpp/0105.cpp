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

typedef vector<int> vi;

int main()
{
    map<string, vi> table;
    char str[32];
    int p;
    while (scanf("%s %d", str, &p) != EOF)
    {
        string s(str);
        if (table.count(s))
            table[s].push_back(p);
        else
            table[s] = vi(1, p);
    }
    for (map<string, vi>::iterator itr = table.begin(); itr != table.end(); itr++)
    {
        sort(itr->second.begin(), itr->second.end());
        puts(itr->first.c_str());
        for (int i = 0; i < itr->second.size(); i++)
            printf("%s%d", i ? " " : "", itr->second[i]);
        puts("");
    }
    return 0;
}