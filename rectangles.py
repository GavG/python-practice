#!/usr/bin/env python3

points = [
            (3, 1), (3,2), (3,3),
            (2, 1), (2,2), (2,3),
            (1, 1), (1,2), (1,3),
        ]

def main():

    rectangles = []

    for point in points:
        match = [point, None, None, None]

        for point_x_match in points:
            if point_x_match[0] == point[0] and point_x_match[1] > point[1]:
                match[1] = point_x_match

                for point_y_match in points:
                    if point_y_match[1] == point_x_match[1] and point_y_match[0] > point[0]:
                        match[2] = point_y_match

                        for point_x_y_match in points:
                            if point_x_y_match[1] == point[1] and point_x_y_match[0] == point_y_match[0]:
                                match[3] = point_x_y_match
                                print('--- MATCH ---')
                                print(match)
                                rectangles.append(match)

    #print(rectangles)

if __name__ == "__main__":
    main()
