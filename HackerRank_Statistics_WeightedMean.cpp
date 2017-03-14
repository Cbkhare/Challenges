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
#include <iomanip>
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

int main() {
    std::vector<int> w,x;
    //std::vector<int> x;
    int size, totalWeight;
    float ans; 
    std::cin>>size;
    for (int i = 0; i<size;i++){
        int val;std::cin>>val;
        x.push_back(val);
    }
    
    for (int i = 0; i<size;i++){
        int val;std::cin>>val;
        w.push_back(val);
        totalWeight+=w[i];
    }
    float ws=0; //weighted sum
    for (int i=0; i<size;i++){
        ws += w[i]*x[i];
    }
    std::cout<<std::setprecision(1)<<std::fixed;
    std::cout<<ws/totalWeight;
    return 0;
}
/*Objective
In the previous challenge, we calculated a mean. In this challenge, we practice calculating a weighted mean. Check out the Tutorial tab for learning materials and an instructional video!

Task
Given an array, , of integers and an array, , representing the respective weights of 's elements, calculate and print the weighted mean of 's elements. Your answer should be rounded to a scale of decimal place (i.e., format).

Input Format

The first line contains an integer, , denoting the number of elements in arrays and .
The second line contains space-separated integers describing the respective elements of array .
The third line contains space-separated integers describing the respective elements of array .

Constraints

    , where is the element of array .
    , where is the element of array .

Output Format

Print the weighted mean on a new line. Your answer should be rounded to a scale of decimal place (i.e., format).

Sample Input

5
10 40 30 50 20
1 2 3 4 5

Sample Output

32.0
*/
