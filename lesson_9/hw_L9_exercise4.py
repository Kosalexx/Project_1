from math import sqrt


def distance(point_1: tuple, point_2: tuple, *points: tuple) -> str:
    """Returns the distance between points with passed coordinates. """

    x1, y1 = point_1[0], point_1[1]
    x2, y2 = point_2[0], point_2[1]
    result = sqrt((x2 - x1)**2 + (y2 - y1)**2)
    x1, y1 = x2, y2
    for new_point in points:
        x2 = new_point[0]
        y2 = new_point[1]
        result += sqrt((x2 - x1)**2 + (y2 - y1)**2)
        x1, y1 = x2, y2

    return f'The distance between the selected points: {round(result, 2)}'


number_points = int(input('Enter the number of points (>= 2): '))
points_list = []
for _ in range(number_points):
    point = tuple(int(num) for num in input('Enter coordinates of points ('
                                            'separated by space): ').split())
    points_list.append(point)

print(distance(*points_list))
