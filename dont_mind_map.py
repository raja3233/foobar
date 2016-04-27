def answer(subway):
    dest = [{},{},{}]
    max_route_length = len(subway)
    import itertools
    directions = '01234'
    for closed_station in range(-1, len(subway)):
        for path_length in range(2,6):
            current_directions =directions[:len(subway[0])]
            for route in itertools.product(current_directions,repeat = path_length):
                dest[0][route] = destination(route,0,subway,closed_station)
                dest[2][route] = destination(route,2,subway,closed_station)
                dest[1][route] = destination(route,1,subway,closed_station)
            for route in dest[0]:
                if (dest[0][route] == dest[1][route]) and closed_station == -1:
                    satisfy = True
                    for station in range(2,3):
                        if (dest[0][route] != destination(route,station,subway,closed_station)):
                            satisfy = False
                    if satisfy:
                        return -1
                elif closed_station == 1 and (dest[0][route] == dest[2][route]):
                    satisfy = True
                    if len(subway) == 3:
                        return closed_station
                    elif (dest[0][route] != destination(route,3,subway,closed_station)):
                            satisfy = False
                    if satisfy:
                        return closed_station
                elif closed_station != -1 and (dest[0][route] == dest[1][route]):
                    satisfy = True
                    for station in range(2,3):
                        if (dest[0][route] != destination(route,station,subway,closed_station)):
                            satisfy = False
                    if satisfy:
                        return closed_station
    return -2



def destination(path, station, subway,closed_station):
    current_station = station
    for direction in path:
        direction = int(direction)
        previous_station = current_station
        current_station = subway[current_station][direction]
        if current_station == closed_station:
            if subway[current_station][direction] == closed_station:
                current_station = previous_station
            else:
                current_station = subway[current_station][direction]
    destination = current_station
    return destination





