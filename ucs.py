def convert_array(array):
    array = array.replace('(', '').replace(')', '').replace(' ', '').split(',')
    array = list(filter(None, array))
    return array
    
if __name__ == "__main__":
    max_height = int(input())
    initial = list(map(convert_array,input().split(';')))
    goal = list(map(convert_array,input().split(';')))
  
    #print(max_height)
    #print(len(initial))
    #print(len(goal))
    
    for x in range(len(initial)):
        if(len(initial[x])>=max_height):
            print("No solution found")
            exit()
    for x in range(len(goal)):
        if(len(goal)>=max_height):
            print("No solution found")
            exit()
    
    #for x in range(len(initial)): 
    #    print (initial[x][0])
    #for x in range(len(goal)): 
    #    print (goal[x])


    #sñldkfjñaslkjf
