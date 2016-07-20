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
    //vector<int> testVector;
    std::cin>>testCaseSize;
    set<int> st;
    for(int i=0; i<testCaseSize; i++){
        int val,task;
        std::cin>>task>>val;
		switch (task){
	        case 1:
	            st.insert(val);
	            break;
	        case 2:
	            st.erase(val);
	            break;
	        case 3:
	            std::cout << (st.find(val) == st.end() ? "No" : "Yes") << std::endl;
	            break;
    			}
			}
    for (auto i: st){
		std::cout << i << ' ';}
    return 0;
}
