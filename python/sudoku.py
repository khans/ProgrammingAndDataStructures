def sudoku2(grid):
    # check 3*3 grids:
    uniques = []
    #check rows first
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == '.':
                pass
            elif grid[i][j] not in uniques:
                uniques.append(grid[i][j])
            else:
                return False
        uniques = []
            
    #check columns:
    for j in range (len(grid)):
        for i in range(len(grid)):
            if grid[i][j] == '.':
                pass
            elif grid[i][j] not in uniques:
                uniques.append(grid[i][j])
            else:
                return False
        uniques = []
    
    #check 3*3 grids
    numGrids = len(grid)
    g = 0
    iStart = 0; iEnd = 3
    jStart = 0; jEnd = 3
    
    while (g < numGrids):
        if (g>0 and g%3 == 0):
            iStart += 3
            iEnd += 3
            jStart = 0
            jEnd = 3
        
        if jEnd <= numGrids:
            for i in range(iStart,iEnd):
                for j in range(jStart,jEnd):
                    if grid[i][j] == '.':
                        pass
                    elif grid[i][j] not in uniques:
                        uniques.append(grid[i][j])
                    else:
                        return False
            jStart += 3; jEnd +=3
            uniques = []
            g += 1    
        
    
    return True
                
    
    

