#include <cstdlib>
#include <iostream>
#include <string>
using namespace std;

string repStr(string &obj, string from, string to) {
    int pos = obj.find(from);
    int toLen = to.length();
 
    if (from.empty()) {
        return obj;
    }
 
    while ((pos = obj.find(from, pos)) != string::npos) {
        obj.replace(pos, from.length(), to);
        pos += toLen;
    }
    return obj;
}

int main(){
    cin.tie(0);
    ios::sync_with_stdio(false);

    int n;
    cin >> n;
    cin.ignore();
    while(--n >= 0){
        string s;
        getline(cin,s);
        repStr(s, "Hoshino", "Hoshina");
        cout << s << endl;
    }
    return EXIT_SUCCESS;
}