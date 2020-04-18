class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return []
        main =[]
        temp = [root]
        while (len(temp)>0):
            c = []
            nt = []
            for i in temp:
                c.append(i.val)
                nt.extend(i.children)
            main.append(c)
            temp = nt
        return main 
