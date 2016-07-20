#include <iostream>
#include <vector>

using namespace std;

template <typename T>
std::ostream& operator<< (std::ostream& out, const std::vector<T>& v) {
  if ( !v.empty() ) {
    out << '[';
    std::copy (v.begin(), v.end(), std::ostream_iterator<T>(out, ", "));
    out << "\b\b]";
  }
  return out;
}

/*
for (auto const& c : path)
    std::cout << c << ' ';
*/

class Solution{
    public:
        std::vector<int> plusOne(vector<int> &A);
};
vector<int> Solution::plusOne(vector<int> &A) {
    // Do not write main() function.
    // Do not read input, instead use the arguments to the function.
    // Do not print the output, instead return values as specified

    int vsize;
    vsize = A.size();
    int carry=0;
    for (int i = vsize-1; i>=0; i--){
        if (i==vsize-1){
            A[i]+=1;
            }
        else{
            A[i]+=carry;
        }
        if (A[i]>=10){
            A[i]%=10;
            carry = 1;
            if (i==0){
                A.insert(A.begin(),1);
                break;  //break condition
            }
            else{continue;}
        }
        else{
            break;
        } //break condition
    }
    int i =0;
    while (A[i]==0){
        A.erase(A.begin());
    }
}


int main()
{
    Solution Sol;
    int testCaseSize;
    vector<int> testVector;
    std::cin>>testCaseSize;
    for(int i=0; i<testCaseSize; i++){
        std::cin>>testVector[i];
    }
    std::cout<<Sol.plusOne(testVector);
    return 0;
}
