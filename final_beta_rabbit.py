def answer(food, grid):
    min_required_food = {}
    max_required_food = {}
    n = len(grid)
    total_rooms = n ** 2
    #find min,max food cost from given room to end room
    for room in range(total_rooms - 1, -1, -1):
        min_required_food[room] = _food_cost(room,grid,n,min_required_food,fun=min)
        max_required_food[room] = _food_cost(room,grid,n,max_required_food,fun=max)
    return _remaining_food(food,grid,n,min_required_food,max_required_food,0)


def _remaining_food(food,grid,n,min_required_food,max_required_food,room):
    """Return optimal food left """
    room_row = room / len(grid)
    room_column = room % len(grid)
    if room_row >= n:
        return -1
    elif room_column >= n:
        return -1
    elif room == len(grid)**2 - 1:
        return food
    elif min_required_food[room] == food: #minmum cost required
        return 0
    elif min_required_food[room] > food:  #when provided food is less required
        return -1
    elif max_required_food[room] <= food: #when provided food is more than required
        return food - max_required_food[room]
    else: # when given food is between minimum and max cost
        food = food - grid[room_row][room_column]
        right_path_cost = _remaining_food(food,grid,n,min_required_food,max_required_food,room+1)
        bottom_path_cost = _remaining_food(food,grid,n,min_required_food,max_required_food,room+n)
        if right_path_cost >=0 and bottom_path_cost >=0:
            return min(right_path_cost, bottom_path_cost)
        else:
            return max(right_path_cost, bottom_path_cost)


def _food_cost(room,grid,n,required_food,fun=min):
    '''Returns food cost to reach the last room'''
    right_room = room + 1
    bottom_room = room + n
    bottom_row = right_column = n -1
    room_row = room / n
    room_column = room % n
    if room_row == bottom_row and room_column == right_column:
        return grid[room_row][room_column] + 0
    if room_row == bottom_row:
        return grid[room_row][room_column] + required_food[right_room]
    elif room_column == right_column:
        return grid[room_row][room_column] + required_food[bottom_room]
    else:
        return grid[room_row][room_column] + fun(required_food[right_room], required_food[bottom_room])


