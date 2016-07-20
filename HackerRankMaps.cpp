#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cctype>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <functional>
#include <ostream>
using namespace std;
#define DEBUG(x) cout << '>' << #x << ':' << x << endl;
#define REP(i,n) for(int i=0;i<(n);i++)
#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)
inline bool EQ(double a, double b) { return fabs(a-b) < 1e-9; }
const int INF = 1<<29;
typedef long long ll;
inline int two(int n) { return 1 << n; }
inline int test(int n, int b) { return (n>>b)&1; }
inline void set_bit(int & n, int b) { n |= two(b); }
inline void unset_bit(int & n, int b) { n &= ~two(b); }
inline int last_bit(int n) { return n & (-n); }
inline int ones(int n) { int res = 0; while(n && ++res) n-=n&(-n); return res; }
template<class T> void chmax(T & a, const T & b) { a = max(a, b); }
template<class T> void chmin(T & a, const T & b) { a = min(a, b); }
/////////////////////////////////////////////////////////////////////

int main()
{
    int testCaseSize;
    std::cin>>testCaseSize;
    std::map <string, int> Map;
    for(int i=0; i<testCaseSize; i++){
        int task, val;
        string key;
        std::cin>>task;
        switch (task) {
        	case 1:
        		std::cin>>key>>val;
        		Map[key] += val;
        		break;
        	case 2:
        		std::cin>>key;
        		Map.erase(key);
        		break;
        	case 3:
        		std::cin>>key;
        		std::cout<< Map[key]<<std::endl;
		}
    }
    for (auto i: Map){
		std::cout << i.first << " " << i.second <<"\n";}
    return 0;
}
