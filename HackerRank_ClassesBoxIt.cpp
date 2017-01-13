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

class Box{
    private:
    long l,b,h;
    
    public:
    //constructors 
    Box(){l=0,b=0,h=0;}
    Box(long len, long brt, long het){ l=len,b=brt,h=het;}
    Box(Box &box){
        l = box.l, b = box.b, h=box.h;
    }
    
    //getters 
    long getLength(){return l;}
    long getBreadth(){return b;}
    long getHeight(){return h;}
    long long CalculateVolume(){return l*b*h;}
    
    bool operator<(Box& box){
        if ((l<box.l) || (l==box.l && b<box.b) || (l==box.l && b==box.b && h<box.h)){
            return true;
        }
        else {return false;}
    }
    
    friend ostream& operator<<( ostream& out, Box& B){  
        std::stringstream ss;
        ss<<B.l<<" "<<B.b<<" "<<B.h;
        out<< ss.str();
        return  out;
    }
    
};
void check2()
{
	int n;
	cin>>n;
	Box temp;
	for(int i=0;i<n;i++)
	{
		int type;
		cin>>type;
		if(type ==1)
		{
			cout<<temp<<endl;
		}
		if(type == 2)
		{
			int l,b,h;
			cin>>l>>b>>h;
			Box NewBox(l,b,h);
			temp=NewBox;
			cout<<temp<<endl;
		}
		if(type==3)
		{
			int l,b,h;
			cin>>l>>b>>h;
			Box NewBox(l,b,h);
			if(NewBox<temp)
			{
				cout<<"Lesser\n";
			}
			else
			{
				cout<<"Greater\n";
			}
		}
		if(type==4)
		{
			cout<<temp.CalculateVolume()<<endl;
		}
		if(type==5)
		{
			Box NewBox(temp);
			cout<<NewBox<<endl;
		}

	}
}

int main()
{
	check2();
}

/*Design a class named Box whose dimensions are integers and private to the class. The dimensions are labelled: length , breadth , and height .

The default constructor of the class should initialize , , and to .

The parameterized constructor Box(int length, int breadth, int height) should initialize Box's and to length, breadth and height.

The copy constructor BoxBox ) should set and to 's and , respectively.

Apart from the above, the class should have functions:

    int getLength() - Return box's length
    int getBreadth() - Return box's breadth
    int getHeight() - Return box's height
    long long CalculateVolume() - Return the volume of the box

Overload the operator for the class Box. Box Box if:

    <
    < and ==
    < and == and ==

Overload operator for the class Box().
If is an object of class Box:

should print , and on a single line separated by spaces.

Constraints


Two boxes being compared using the operator will not have all three dimensions equal.*/
