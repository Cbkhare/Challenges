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

class Student{
    private:
    int age, standard;
    string first_name, last_name;
    
    public:
    void set_age(int a){age =a;}
    void set_standard(int s) {standard=s;}
    void set_first_name(string f) {first_name=f;}
    void set_last_name(string l) {last_name=l;}
    
    int get_age() {return age;}
    int get_standard() {return standard;}
    string get_first_name() {return first_name;}
    string get_last_name() {return last_name;} 
    
    string to_string(){
        stringstream ss;
        ss<<age<<","<<first_name<<","<<last_name<<","<<standard;
        return ss.str();
    }
};
int main() {
    int age, standard;
    string first_name, last_name;
    
    cin >> age >> first_name >> last_name >> standard;
    
    Student st;
    st.set_age(age);
    st.set_standard(standard);
    st.set_first_name(first_name);
    st.set_last_name(last_name);
    
    cout << st.get_age() << "\n";
    cout << st.get_last_name() << ", " << st.get_first_name() << "\n";
    cout << st.get_standard() << "\n";
    cout << "\n";
    cout << st.to_string();
    
    return 0;
}

/*Classes in C++ are user defined types declared with keyword class that has data and functions . Although classes and structures have the same type of functionality, there are some basic differences. The data members of a class are private by default and the members of a structure are public by default. Along with storing multiple data in a common block, it also assigns some functions (known as methods) to manipulate/access them. It serves as the building block of Object Oriented Programming.

It also has access specifiers, which restrict the access of member elements. The primarily used ones are the following:

    public: Public members (variables, methods) can be accessed from anywhere the code is visible.
    private: Private members can be accessed only by other member functions, and it can not be accessed outside of class.

Class can be represented in the form of

class ClassName {
    access_specifier1:
        type1 val1;
        type2 val2;
        ret_type1 method1(type_arg1 arg1, type_arg2 arg2,...)
        ...
    access_specifier2:
        type3 val3;
        type4 val4;
        ret_type2 method2(type_arg3 arg3, type_arg3 arg3,...)
        ...
};

It's a common practice to make all variables private, and set/get them using public methods. For example:

class SampleClass {
    private:
        int val;
    public:
        void set(int a) {
            val = a;
        }
        int get() {
            return val;
        }
};

We can store details related to a student in a class consisting of his age (int), first_name (string), last_name (string) and standard (int).

You have to create a class, named Student, representing the student's details, as mentioned above, and store the data of a student. Create setter and getter functions for each element; that is, the class should at least have following functions:

    get_age, set_age
    get_first_name, set_first_name
    get_last_name, set_last_name
    get_standard, set_standard

Also, you have to create another method to_string() which returns the string consisting of the above elements, separated by a comma(,). You can refer to stringstream for this.

Input Format

Input will consist of four lines.
The first line will contain an integer, representing the age. The second line will contain a string, consisting of lower-case Latin characters ('a'-'z'), representing the first_name of a student.
The third line will contain another string, consisting of lower-case Latin characters ('a'-'z'), representing the last_name of a student.
The fourth line will contain an integer, representing the standard of student.

Note: The number of characters in first_name and last_name will not exceed 50.

Output Format

The code provided by HackerRank will use your class members to set and then get the elements of the Student class.

Sample Input

15
john
carmack
10

Sample Output

15
carmack, john
10

15,john,carmack,10
*/
