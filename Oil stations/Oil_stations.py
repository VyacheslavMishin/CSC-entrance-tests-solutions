def min_oil_stations(accessible_distance, oil_stations_coordinates, full_distance):
    minimal, curr_station_index, curr_coord, index = 0, -1, 0, 0

    while index < len(oil_stations_coordinates):
        if oil_stations_coordinates[index] - curr_coord <= accessible_distance:
            index += 1
            continue
        elif index != curr_station_index + 1:
            curr_station_index = index - 1
            curr_coord = oil_stations_coordinates[index - 1]
            minimal += 1
        else:
            return -1

    if full_distance - curr_coord <= accessible_distance:
        return minimal
    elif full_distance - oil_stations_coordinates[index - 1] <= accessible_distance:
        return minimal + 1
    else:
        return -1


dist = int(input())
accessible_dist = int(input())
all_oil_stations = int(input())
oil_stations_coord = list(map(int, input().split()))

print(min_oil_stations(accessible_dist, oil_stations_coord, dist))
