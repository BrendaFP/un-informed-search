import random
from queue import PriorityQueue

class Node:
    def __init__(self, cont, cost, state, path):
        self.cont = cont
        self.state = state
        self.cost = cost
        self.path = path
    
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.cont == other.cont
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self.cont < other.cont
        return NotImplemented   
        
def convert_array(array):
    array = array.replace('(', '').replace(')', '').replace(' ', '').split(',')
    array = list(filter(None, array))
    return array

def is_goal(current, goal):
    for i in range(len(current)):
        if goal[i] != ['X']:
            if(goal[i] != current[i]):
                return False
    return True

def expand(state, max_height):
    nodes = []
    for i in range(len(state)):
        for j in range(len(state)):
            if i != j and (len(state[j]) < max_height) and len(state[i])>0:
                new_state = [x[:] for x in state]
                new_state[j].append(new_state[i][-1])
                new_state[i] = new_state[i][:-1]
                cost = abs(i-j) + 1
                nodes.append((cost,new_state,(i,j)))
                #print(nodes)
    return nodes

def incons_heuristic():
    heu = random.randint(1,100)
    return heu

if __name__ == "__main__":
    visited = set()
 
    max_height = int(input())
    initial = list(map(convert_array,input().split(';')))
    goal = list(map(convert_array,input().split(';')))

    for x in range(len(initial)):
        if(len(initial[x])>max_height):
            print("No solution found")
            exit()
        
    for x in range(len(goal)):
        if(len(goal[x])>max_height):
            print("No solution found")
            exit()
        
    q = PriorityQueue()
    q.put(Node(0, 0, initial, []))

    while not(q.empty()):
        current = q.get()
        #print(current.state)
        aux = "%s" % current.state
        
        if aux not in visited:
            visited.add(aux)
            #print("visited",visited,aux)
            if(is_goal(current.state,goal)):
                print(current.cost)
                final_path = map(str, current.path)
                print('; '.join(final_path))
                exit()
        
            nodes = expand(current.state, max_height)
            
            for x in nodes:
                auxCost = x[0] + current.cost
                auxCont = auxCost
                auxState = x[1]
                auxPath = current.path[:]
                auxPath.append(x[2])
                
                new_node = Node(auxCont+incons_heuristic(), auxCost, auxState, auxPath)        
                q.put(new_node)
    print(int(current.cost))
    final_path = map(str, current.path)
    print('; '.join(final_path))
    exit()
