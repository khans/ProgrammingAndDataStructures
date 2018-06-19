class Solution:
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.rows = 0
        self.cols = 0
        
        self.rows = len(board)
        
        if self.rows != 0:
            self.cols = len(board[0])
        
         
        N = []
        nl = []
        for i in range(self.rows):
            for j in range(self.cols):
                if self.willBeAlive(board,i,j):
                    nl.append(1)
                else:
                    nl.append(0)
            N.append(nl)
            print(nl)
            nl = []
           
        
        for i in range(len(N)):
            for j in range(len(N[0])):
                board[i][j] = N[i][j]
        N = []
        return 
    
    
    def willBeAlive(self,board,ci,cj):
        if self.boundary((ci,cj)):
            neighbors = [(ci-1,cj-1),(ci-1,cj),(ci-1,cj+1),(ci,cj-1),(ci,cj+1),(ci+1,cj-1),(ci+1,cj),(ci+1,cj+1)]
            total = 0
            for each in neighbors:
                if(self.boundary(each)):
                    total += board[each[0]][each[1]]
            
            status = board[ci][cj]
            if (status == 1):
                if (total <=1 or total >3):
                    return False
                return True
            else:
                if(total == 3):
                    return True
                return False
    def boundary(self,t):
        if ((t[0] <0 or t[0]>=self.rows) or (t[1] < 0 or t[1] >= self.cols)):
            return False
        return True    