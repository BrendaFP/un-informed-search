def convert_array(array):
    array = array.replace('(', '').replace(')', '').replace(' ', '').split(',')
    array = list(filter(None, array))
    return array
    
if __name__ == "__main__":
    max_height = int(input())
    initial = list(map(convert_array,input().split(';')))
    goal = list(map(convert_array,input().split(';')))
  
    print(max_height)

    for x in range(len(initial)): 
        print initial[x],
    for x in range(len(goal)): 
        print goal[x], 