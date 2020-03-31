class Solution(object):
    def createGrp(self, L):
        g = {} 
        for pair in L:
            if pair[0] not in g: 
                g[pair[0]] = set([pair[1]])
            else: 
                g[pair[0]].update([pair[1]])
        return g 

    def checkCycle(self, g, cn, visitd, recSt):
        #print (visitd, recSt, cn, visitd[cn], recSt[cn])
        if cn not in g:
            return False
        if visitd[cn]==1 and recSt[cn]==1:
            return True
        visitd[cn]=1
        recSt[cn]=1
        st = False
        for n in g[cn]:
            #print (n)
            st = self.checkCycle(g, n, visitd, recSt)
            if st:
                return st
        recSt[cn] = 0
        return st
        
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        n = numCourses
        g = self.createGrp(prerequisites)
        for i in g:
            c = self.checkCycle(g, i,  [0]*n, [0]*n)
            if c:
                return False
        else:
            return True
        
        
