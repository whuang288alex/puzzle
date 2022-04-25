import heapq
import copy

def get_manhattan_distance(from_state, to_state=[1, 2, 3, 4, 5, 6, 7, 0, 0]):
    distance = 0
    for i in range(1,8):
        from_index  =  from_state.index(i)
        from_x = int(from_index / 3)
        from_y = from_index % 3
        
        to_index  =  to_state.index(i)
        to_x = int(to_index / 3)
        to_y = to_index % 3
        
        distance += (abs(from_x - to_x) + abs(from_y-to_y))
    return distance

def print_succ(state):
    succ_states = get_succ(state)
    for succ_state in succ_states:
        print(succ_state, "h={}".format(get_manhattan_distance(succ_state)))


def get_succ(state):

    succ_states = list()
    index = state.index(0) 
    row = int(index / 3)
    column = index % 3

    for i in range(2):
        if row - 1 in range(3) and state[index - 3] != 0:
            new_state = copy.deepcopy(state)
            new_state[index] = state[index -3]
            new_state[index -3] = 0
            succ_states.append(new_state)
        if row + 1 in range(3) and state[index + 3] != 0:
            new_state = copy.deepcopy(state)
            new_state[index] = state[index +3]
            new_state[index + 3] = 0
            succ_states.append(new_state)
        if column - 1 in range(3) and state[index - 1] != 0:
            new_state = copy.deepcopy(state)
            new_state[index] = state[index -1]
            new_state[index -1] = 0
            succ_states.append(new_state)
        if column  + 1 in range(3) and state[index + 1] != 0:
            new_state = copy.deepcopy(state)
            new_state[index] = state[index +1]
            new_state[index + 1] = 0
            succ_states.append(new_state)
        
        if i == 0:
            temp_state = copy.deepcopy(state)
            temp_state[index] = -1
            index = temp_state.index(0) 
            row = int(index / 3)
            column = index % 3   
                
    return sorted(succ_states)


def solve(state, goal_state=[1, 2, 3, 4, 5, 6, 7, 0, 0]):
    pq = []
    visited = []
    index = 0
    h = get_manhattan_distance(state)
    heapq.heappush(pq,(h , state, (0, h, -1)))
    while True:
        if len(pq) == 0:
            break
        
        #Pop the next state
        popped = heapq.heappop(pq) 
        
        #If this is the goal state, trace back
        if popped[1] == goal_state:
            steps = list()
            current = popped
            #Keep tracing back until reaching the initial state
            while True:
                steps.insert(0,current[1])
                if current[2][2] == -1:
                    break
                else:
                    current = visited[current[2][2]]
            #Print out all the steps taken
            for i in range(len(steps)):
                print(str(steps[i]) + ' h='+ str(get_manhattan_distance(steps[i])) + ' moves: '+ str(i))
            print("Max queue length: " + str(len(pq) + 1))
            return
        
        else:
            visited.append(popped)
            g = popped[2][0] + 1
            successors = get_succ(popped[1])
            for succ in successors: 
                check  = -1
                for i in range(len(visited)):
                    if visited[i][1] == succ:
                        check = i
                        break           
                if check == -1 :
                    h = get_manhattan_distance(succ)
                    heapq.heappush(pq,( g + h , succ, (g , h, index)))
                else:
                    if visited[check][2][0] > g :
                        visited[check] = ( g + h , succ, (g , h, index))
            index += 1           
        
if __name__ == "__main__":
    """
    Feel free to write your own test code here to exaime the correctness of your functions. 
    Note that this part will not be graded.
    """
    print(get_manhattan_distance([2,5,1,4,3,6,7,0,0]))
