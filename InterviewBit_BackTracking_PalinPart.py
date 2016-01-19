class Solution:
    # @param A : a string
    # @return a list of strings
    def bazinga(self,A,stack):
        if len(A)==0:
            self.pic.append(stack)
            return stack
        for i in range(1,len(A)+1):
            if A[:i]==A[:i][::-1]:
                self.bazinga(A[i:],stack+[A[:i]])
        
    def partition(self, A):
        if A=='':   return ''
        self.pic = []
        stack = []
        self.bazinga(A,stack)
        return self.pic
        
            
if __name__=='__main__':
    n = int(input())
    for i in range(n):
        S = Solution()
        c = input()
        print  (S.partition(c))

'''


Given a string s, partition s such that every string of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

  [
    ["a","a","b"]
    ["aa","b"],
  ]

    Ordering the results in the answer :

    Entry i will come before Entry j if :

        len(Entryi[0]) < len(Entryj[0]) OR
        (len(Entryi[0]) == len(Entryj[0]) AND len(Entryi[1]) < len(Entryj[1])) OR
        *
        *
        *
        (len(Entryi[0]) == len(Entryj[0]) AND … len(Entryi[k] < len(Entryj[k]))

In the given example,
["a", "a", "b"] comes before ["aa", "b"] because len("a") < len("aa")
'''
