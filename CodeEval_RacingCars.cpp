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
#include <fstream>
#include <istream>
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

char getSlash(int ind, int lastIndex){
	if (lastIndex != -1) {
		if (lastIndex > ind){
				return '/';
			}
		else if (lastIndex < ind) {
				return '\\';
			}
		else { 
			return '|';
			}
		}
	else {   //can be shortened
		return '|';
	}
}

int main(int argc, char** argv)
{
	//Sample code to read in test cases:
	ifstream file;
	string lineBuffer;
	file.open(argv[1]);
	int lastIndex=-1;
	while (!file.eof()) 
	   {
	       getline(file, lineBuffer);
	       if (lineBuffer.length() == 0)
	           continue; //ignore all empty lines
	       else 
	       {
	           int gInd=-1, cInd = -1;
	           for(std::string::size_type i = 0; i < lineBuffer.size(); ++i) {
    				if (lineBuffer[i] == '_'){
    					gInd = i;
					}
					else if (lineBuffer[i]=='C'){
						cInd = i;
					}
				}
				// End of For
				if (cInd != -1){
					lineBuffer[cInd] = getSlash(cInd, lastIndex);
					lastIndex = cInd;
					}
				else {
					lineBuffer[gInd] = getSlash(gInd, lastIndex);
					lastIndex = gInd;
					}
			   }
			std::cout<<lineBuffer<<"\n";
	       }
	
	return 0;	}


/*Racing Chars

Challenge Description:

You are given a file where each line is a section of a race track with obstructions, gates, and checkpoints. Your task is to find a way to pass this track using the following information:

1. Each section contains either one single gate or one gate with a checkpoint.
2. You should drive only through gates or checkpoints.
3. You should drive through a checkpoint rather than a gate.
4. An obstruction is represented by a number sign "#".
5. A gate is represented by an underscore "_".
6. A checkpoint is represented by a letter C.

Input sample:
#########_##
########C_##
#######_####
######_#C###
#######_C###
#######_####
######C#_###
######C_####
#######_####
#######_####

Your program should accept a path to a filename as its first argument. Each line of the file is a new section of a race track.
Output sample:
#########|##
########/_##
#######/####
######_#\###
#######_|###
#######/####
######/#_###
######|_####
#######\####
#######|####
Print out the way of passing this race track starting from the first line in the file. Use a pipe "|" for the straight, use a slash "/" for the left turn, and use a backslash "\" for the right turn.
Constraints:

    The number of lines in a file is 50.
    The width of a section is 12 characters.
*/
