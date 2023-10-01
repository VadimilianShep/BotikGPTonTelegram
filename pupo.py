class Tree:
    def __init__(self, info, root = None, depth = -1, dvi = 0, osnov = None):
        self.root = root
        self.branches = []
        self.info = info
        self.depth = depth
        self.dv = dvi
        self.used = False
        self.osnov = osnov
    
    def newBranch(self, info, dv):
        self.branches.append(Tree(info, self, depth=self.depth+1, dvi=dv, osnov=self.osnov))
    
    def __str__(self):
        return str(self.info)
    
def treePrint(tree): #это обход на самом деле и получение массива из всех нод
    lst = []
    lst.extend(tree.branches)
    for branch in tree.branches:
        lst.extend(treePrint(branch))
    return lst

def printMatrix(matrix):
    for row in matrix:
        print()
        for i in row:
            print(i, end=" ")
            
def ocenochnFunc(real):
    res = 0
    for i in range(len(template)):
        for x in range(len(template[i])):
            if template[i][x] != real.info[i][x]:
                res+=1
    return res + real.depth

def tradeUP(matrix, i, x):
    temp = matrix[i][x]
    matrix[i][x] = matrix[i-1][x]
    matrix[i-1][x] = temp
    return matrix

def tradeDown(matrix, i, x):
    temp = matrix[i][x]
    matrix[i][x] = matrix[i+1][x]
    matrix[i+1][x] = temp
    return matrix

def tradeLeft(matrix, i, x):
    temp = matrix[i][x]
    matrix[i][x] = matrix[i][x-1]
    matrix[i][x-1] = temp
    return matrix

def tradeRight(matrix, i, x):
    temp = matrix[i][x]
    matrix[i][x] = matrix[i][x+1]
    matrix[i][x+1] = temp
    return matrix

def deepcop(lst): #это клонирование
    return[elem if not isinstance(elem, list) else deepcop(elem) for elem in lst]

def cleaning(lst): #это удаление из массива нод у которых есть потомки
    counter = 0
    length = len(lst)
    while(counter < length):
        if(len(lst[counter].branches) != 0):
            lst.remove(lst[counter])
            length -= 1
        else:
            counter += 1
    return lst
            

template = [[1,2,3],   #то, что должно получиться
            [4,5,6],
            [7,8,'_']]

real = [[2,4,3],   #то, что есть изначально
        [1,8,5],
        [7,'_',6]]

tree = Tree(real)
current = Tree(real)
current.osnov = current

while(ocenochnFunc(current) != current.depth):
    ii = 0
    xx = 0
    nodes = []
    for i in range(len(template)):
        for x in range(len(template[i])):
            if current.info[i][x] == '_':
                ii = i
                xx = x
                break
    if(len(current.branches) == 0):
        if(ii != 0 and current.dv != 4):
            current.newBranch(tradeUP(deepcop(current.info), ii, xx), 1)
        if (xx != 0 and current.dv != 3):
            current.newBranch(tradeLeft(deepcop(current.info), ii, xx), 2)
        if (xx < len(template[0]) - 1 and current.dv != 2):
            current.newBranch(tradeRight(deepcop(current.info), ii, xx), 3)
        if(ii < len(template[0]) - 1 and current.dv != 1):
            current.newBranch(tradeDown(deepcop(current.info), ii, xx), 4)
    nodes = treePrint(current.osnov)
    nodes = cleaning(nodes)
    best = nodes[0]
    for node in nodes:
        if(len(node.branches) == 0 and ocenochnFunc(node) < ocenochnFunc(best)):
            best = node
    current = best
    printMatrix(current.info)
    print()
    print(f"Счет:{ocenochnFunc(current)}")