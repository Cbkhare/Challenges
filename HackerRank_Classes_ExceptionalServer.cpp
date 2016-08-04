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


class Server {
private:
	static int load;
public:
	static int compute(long long A, long long B) {
		load += 1;
		if(A < 0) {
			throw std::invalid_argument("A is negative");
		}
		vector<int> v(A, 0);
		int real = -1, cmplx = sqrt(-1);
		if(B == 0) throw 0;
		real = (A/B)*real;
		int ans = v.at(B);
		return real + A - B*ans;
	}
	static int getLoad() {
		return load;
	}
};
int Server::load = 0;

int main() {
	int T; cin >> T;
	while(T--) {
		long long A, B;
		cin >> A >> B;
		try
		{
		    
		    Server s;
		    long long R = s.compute(A,B);
		    cout << R << endl;
		}
		catch(bad_alloc&){ cout << "Not enough memory" << endl; }
		catch(exception &e){ cout << "Exception: " << e.what() << endl; }
		catch(...){ cout << "Other Exception" << endl; }
		}
	cout << Server::getLoad() << endl;
	return 0;
}

/*
Your friend set up a small computational server that performs complex calculations.
It has a function that takes large numbers as its input and returns a numeric result. Unfortunately, there are various exceptions that may occur during execution.

Complete the code in your editor so that it prints appropriate error messages, should anything go wrong. The expected behavior is defined as follows:

    If the compute function runs fine with the given arguments, then print the result of the function call.
    If it fails to allocate the memory that it needs, print Not enough memory.
    If any other standard C++ exception occurs, print Exception: S where is the exception's error message.
    If any non-standard exception occurs, print Other Exception.

Input Format

The first line contains an integer, , the number of test cases.
Each of the subsequent lines describes a test case as space-separated integers, and , respectively.

Constraints


Output Format
1<=T<=10^3
0<=A,B<=2^60

For each test case, print a single line containing whichever message described in the Problem Statement above is appropriate. After all messages have been printed, the locked stub code in your editor prints the server load.

Sample Input

2
-8 5
1435434255433 5

Sample Output

Exception: A is negative
Not enough memory
2

Explanation

See the implementation of the compute function.
is the server load.*/
