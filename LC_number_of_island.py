class Solution(object):
    def dfs(self,i,j):
        if i in [-1,self.l] or j in [-1,self.b] or self.grid[i][j]=='0' or (i,j) in self.dp:
            return []
        else: 
            self.dp[(i,j)] = 1 
            x = self.dfs(i+1,j)
            y = self.dfs(i,j+1) 
            x1 = self.dfs(i-1, j)
            y1 = self.dfs(i,j-1)
            connected_node = []
            for a in [x,y,x1,y1]:
                if a!=[]:
                    connected_node.extend(a)
            a = [(i,j)]
            a.extend(connected_node)
            #print (a)
            return a
            
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        self.grid = grid
        self.l = len(self.grid)
        if self.l==0:
            return 0
        self.b = len(self.grid[0])
        traversed = set([]) # to perform O(1) lookup operation
        for i in range(self.l):
            for j in range(self.b):
                self.dp={} # to avoid self recursion
                if (i,j) in traversed or self.grid[i][j]=='0':
                    continue 
                count+=1
                a  = self.dfs(i,j)
                if a:
                    traversed.update(a)
        return count 
                
