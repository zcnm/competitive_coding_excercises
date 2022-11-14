#include <iostream>
#include <string>
#include <map>
using namespace std;

void solve(string input) {
    map<char, int> m;
    for (char c: input) {
        if (isupper(c)) {
            if (m.count(tolower(c)) == 0) 
            {
                cout << "NO\n";
                return;
            }
        }
        else m[c] = 0;
    }
    cout <<"YES\n";
}

int main(int argc, char const *argv[])
{
    int t;
    cin >> t;
    cin.ignore();
    for (int i = 0; i < t; i++) 
    {
        string input;
        getline(cin, input);
        solve(input);
    }
    
    return 0;
}
