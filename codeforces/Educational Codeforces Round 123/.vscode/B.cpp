#include <iostream>
#include <string>
#include <map>
#include <vector>
using namespace std;

void solve(int n) {
    vector<int> v;
    for (int i = 1; i <= n; i++){
        v.push_back(i);
    }
    
}

int main(int argc, char const *argv[])
{
    int t;
    cin >> t;
    cin.ignore();
    for (int i = 0; i < t; i++) 
    {
        int n;
        cin >> n;
        cin.ignore();

        solve(n);
    }
    
    return 0;
}
