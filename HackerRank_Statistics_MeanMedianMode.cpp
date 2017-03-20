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

int main() {
    std::vector<float> vec; 
    int size, vec_size,mid;
    float elem_sum;
    std::cin>>size;
    for (int i=0; i<size;i++){
        float val;
        std:cin>>val;
        vec.push_back(val);
    }
    elem_sum = std::accumulate(vec.begin(),vec.end(),0);
    vec_size = vec.size();
    std::cout<<setprecision(1)<<std::fixed;
    std::cout<<elem_sum/vec_size<<std::endl;
    
    //sorting vec
    std::sort (vec.begin(), vec.end());
    float mid_sum;
    if (vec_size%2==0){
        mid = vec_size/2;
        mid_sum = (vec[mid]+vec[mid-1])/2; //std::accumulate(vec.begin()+mid,vec.begin()+mid+1,0);
    }
    else{
        mid_sum = vec[vec_size/2];   //since zero based index list
    }
    std::cout<<mid_sum<<std::endl;
    std::map<int,int> map_vec;
    for (auto i: vec)
        map_vec[i]++;
        
    using pair_type = decltype(map_vec)::value_type;  
    auto max_elem = std::max_element(
    std::begin(map_vec), std::end(map_vec),
    [] (const pair_type & p1, const pair_type & p2)
        {return p1.second < p2.second;});
    std::cout<<max_elem->first<<std::endl;
    return 0;
}

/*
Objective
In this challenge, we practice calculating the mean, median, and mode. Check out the Tutorial tab for learning materials and an instructional video!

Task
Given an array, , of integers, calculate and print the the respective mean, median, and mode on separate lines. If your array contains more than one modal value, choose the numerically smallest one.

Note: Other than the modal value (which will always be an integer), your answers should be in decimal form, rounded to a scale of decimal place (i.e., , format).

Input Format

The first line contains an integer, , denoting the number of elements in the array.
The second line contains space-separated integers describing the array's elements.

Constraints

    , where is the element of the array.

Output Format

Print lines of output in the following order:

    Print the mean on a new line, to a scale of decimal place (i.e., , ).
    Print the median on a new line, to a scale of decimal place (i.e., , ).
    Print the mode on a new line; if more than one such value exists, print the numerically smallest one.

Sample Input

10
64630 11735 14216 99233 14470 4978 73429 38120 51135 67060

Sample Output

43900.6
44627.5
4978

Explanation

Mean:
We sum all elements in the array, divide the sum by , and print our result on a new line.

Median:
To calculate the median, we need the elements of the array to be sorted in either non-increasing or non-decreasing order. The sorted array . We then average the two middle elements:
and print our result on a new line.

Mode:
We can find the number of occurrences of all the elements in the array:

 4978 : 1
11735 : 1
14216 : 1
14470 : 1
38120 : 1
51135 : 1
64630 : 1
67060 : 1
73429 : 1
99233 : 1

Every number occurs once, making the maximum number of occurrences for any number in . Because we have multiple values to choose from, we want to select the smallest one, , and print it on a new line.
*/

