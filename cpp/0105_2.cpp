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
 
#define reep(i,f,n) for(int i=f; i<int(n); ++i)
#define rep(i,n) reep(i,0,n)
 
typedef vector<int> vi;
typedef vector<vi> vvi;
 
int main()
{
    map<string, vi> table;
    char str[32];
    int page;
    while(scanf("%s %d", str, &page) != EOF){
        string s(str);
        if(table.count(s))
            table[s].push_back(page);
        else
            table[s] = vi(1, page);
    }
 
    for(map<string, vi>::iterator itr = table.begin(); itr != table.end(); ++itr){
        sort(itr->second.begin(), itr->second.end());
        puts(itr->first.c_str());
        rep(i, itr->second.size())
            printf("%s%d", i?" ":"", itr->second[i]);
        puts("");
    }
 
    return 0;
}