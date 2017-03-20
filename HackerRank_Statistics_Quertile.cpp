#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cctype>
#include <string>
#include <vector>
#include <list>
#include <tuple>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <functional>
#include <ostream>
#include <iomanip>
using namespace std;
#define DEBUG(x) cout << '>' << #x << ':' << x << endl;
#define REP(i,n) for(int i=0;i<(n);i++)
#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MIN(a,b) ((a)<(b)?(a):(b))
#define ABS(x) ((x)<0?-(x):(x))
#define DB(x) cout<<"\n"<<#x<<" = "<<(x)<<"\n";
#define MS(a,b) memset(a,b,sizeof(a))
#define SZ(x) ((int)x.size())
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

std::tuple<float,int,int> quartile(std::vector<int> v){
	int mid,vs;
	double ret;
	vs = SZ(v);
	mid = (vs)/2;
	if (vs%2==0){
		float sum = static_cast<float>(v[mid]+v[mid-1]);
		ret = std::ceil(sum/2);
	}
	else {
		ret = v[mid];
	}
	return make_tuple(ret, mid,vs);
};

int main()
{
    int size,m1,m2,m3,vss,vs1,vs2; 
    float q1,q2,q3;
    std::vector<int> vec; 
    std::cin>>size;
    REP(i,size){
    	int val;
    	std::cin>>val;
    	vec.push_back(val);
	}
	std::sort (vec.begin(), vec.end());
	//tie(qut,rer,add,sub,mul)=cal(a,b);
	tie(q2,m2,vss)= quartile(vec);
	
	if (vss%2==0){      //because if mid & mid-1
		std::vector<int> v1(vec.begin(), vec.begin()+m2-1);
		tie(q1,m1,vs1) = quartile(v1);
	}
	else {
		std::vector<int> v1(vec.begin(), vec.begin()+m2);
		tie(q1,m1,vs1) = quartile(v1);		
	}
	std::vector<int> v3(vec.begin()+m2+1,vec.end());
	tie(q3,m3,vs2) = quartile(v3);
	std::cout<<q1<<"\n"<<q2<<"\n"<<q3;
	return 0;
}


/*
Objective
In this challenge, we practice calculating quartiles. Check out the Tutorial tab for learning materials and an instructional video!

Task
Given an array, , of integers, calculate the respective first quartile (), second quartile (), and third quartile (). It is guaranteed that , , and are integers.

Input Format

The first line contains an integer, , denoting the number of elements in the array.
The second line contains space-separated integers describing the array's elements.

Constraints

    , where is the element of the array.

Output Format

Print lines of output in the following order:

    The first line should be the value of .
    The second line should be the value of .
    The third line should be the value of .

Sample Input

9
3 7 8 5 12 14 21 13 18

Sample Output

6
12
16

Explanation

. When we sort the elements in non-decreasing order, we get . It's easy to see that .

As there are an odd number of data points, we do not include the median (the central value in the ordered list) in either half:

    Lower half (L): 3, 5, 7, 8

    Upper half (U): 13, 14, 18, 21
*/
