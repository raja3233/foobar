def answer(food, grid):
    min_required_food = {}
    max_required_food = {}
    total_rooms = len(grid) ** 2
    for room in range(total_rooms - 1, -1, -1):
        min_required_food[room] = _food_search(room,grid,min_required_food,fun=min)
        max_required_food[room] = _food_search(room,grid,max_required_food,fun=max)
        print "min_food of {0} = {1}".format(room, min_required_food[room])
        print "max_food of {0} = {1}".format(room, max_required_food[room])
    if min_required_food[0] == food:
        return 0
    elif min_required_food[0] > food:
        return -1
    else:
        return _remaining_food(food,grid,min_required_food,max_required_food,0)

def _remaining_food(foodLeft,grid,min_required_food,max_required_food,room):

    room_row = room / len(grid)
    room_column = room % len(grid)
    foodLeft = foodLeft - grid[room_row][room_column]
    print 'food_left---->',foodLeft
    print 'room--------->',room
    if room == len(grid)**2 - 1:
        if foodLeft >= 0:
            return foodLeft
        else:
            return -1
    else:

        if room_row == len(grid) -1:
            nextroom = room + 1
        elif room_column == len(grid) -1:
            nextroom = room + len(grid)
        else:
            print "print {}-{}={}".format(foodLeft,min_required_food[room +1],foodLeft - min_required_food[room +1])
            if (grid[room_row][room_column + 1] >= grid[room_row + 1][room_column] and
                    (foodLeft - min_required_food[room +1] >= 0 and
                         max_required_food[room + 1] > max_required_food[room +len(grid)])):
                nextroom = room + 1
            else:
                nextroom = room + len(grid)
        print nextroom
        return _remaining_food(foodLeft,grid,min_required_food,max_required_food,nextroom)


def _food_search(room,grid,required_food,fun=min):
    right_room = room + 1
    bottom_room = room + len(grid)
    bottom_row = right_column = len(grid) -1
    room_row = room / len(grid)
    room_column = room % len(grid)
    if room_row == bottom_row and room_column == right_column:
        return grid[room_row][room_column] + 0
    if room_row == bottom_row:
        return grid[room_row][room_column] + required_food[right_room]
    elif room_column == right_column:
        return grid[room_row][room_column] + required_food[bottom_room]
    else:
        return grid[room_row][room_column] + fun(required_food[right_room], required_food[bottom_room])


print answer(12,[[0, 2, 5], [1, 1, 3], [2, 1, 1]])

