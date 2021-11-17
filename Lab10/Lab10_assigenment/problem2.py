"""
Problem 2: 
Write a function to sort a list of points based on their y-coordinates.
 Each point is a list of two values for x- and y-coordinates.
"""

def sortPoints(points):
    points_copy = points.copy()
    points_copy.sort(key=lambda point: point[1])
    return points_copy

def main():
    sample_points = [[4, 34], [1, 7.5], [4, 8.5], [1, -4.5], [1, 4.5], [4, 6.6]]
    print("Sample points: ", sample_points)
    print("______________")
    sorted_sample_points = sortPoints(sample_points)
    print("Sorted points: ", sorted_sample_points)


if __name__ == "__main__":
    main()