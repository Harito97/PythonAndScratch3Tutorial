# pip install scikit-learn
from sklearn.cluster import KMeans
import numpy as np


def _projection(x, y):
    # Tính tọa độ trung điểm
    mid_x = (x + y) / 2
    mid_y = (x + y) / 2
    return (mid_x, mid_y)


def perpendicular_projection(A):
    projections = []
    for point in A:
        x, y = point
        # Tìm tọa độ hình chiếu trên đường thẳng y = x
        proj = _projection(x, y)
        projections.append(proj)
    return projections


def cluster_centers(points, k):
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(points)
    return kmeans.cluster_centers_, kmeans.labels_


def round_centers(centers):
    rounded_centers = []
    for center in centers:
        rounded_center = []
        for coord in center:
            rounded_coord = round(coord * 2) / 2
            rounded_center.append(rounded_coord)
        rounded_centers.append(rounded_center)
    return rounded_centers


def max_distance_to_center(points, labels, centers):
    max_distances = []
    for i in range(len(centers)):
        cluster_points = np.array(
            [points[j] for j in range(len(points)) if labels[j] == i]
        )
        distances = np.linalg.norm(cluster_points - centers[i], axis=1)
        max_distances.append(np.max(distances))
    return max_distances


def count_points_in_circle(center, R, m):
    xi, yi = center[0], center[1]
    if R == 0:
        return {(xi, yi)}
    count = set()
    for x in range(max(0, int(xi - R)), min(m + 1, int(xi + R + 1))):
        for y in range(max(0, int(yi - R)), min(m + 1, int(yi + R + 1))):
            # if x == 4 and y == 4:
            #     print(
            #         "Có (4, 4) trong vòng lặp.",
            #         (x - xi) ** 2 + (y - yi) ** 2 <= R**2,
            #         f"{xi, yi, x, y, R}",
            #     )
            if (x - xi) ** 2 + (y - yi) ** 2 <= R**2:
                count.add((x, y))
    return count


def process(k, objects):
    temp = [(i * 0.5, i * 0.5) for i in range(2 * m + 1)]
    projections = perpendicular_projection(objects)
    projections += temp
    centers, labels = cluster_centers(projections, k)
    centers = round_centers(centers)
    R_array = max_distance_to_center(objects, labels, centers)
    result = set()
    # print(objects + temp, labels, centers, R_array)
    for center, R in zip(centers, R_array):
        result = result | count_points_in_circle(
            center, R, m
        )  # union operator of 2 set (or can use new_set = set1.update(set2))
    # print(result)
    return len(result)


if __name__ == "__main__":
    """
    Test 1:
    5 4 3
    1 1
    2 3
    3 3
    2 3
    3 4
    Test 2:
    6 4 3
    1 1
    2 3
    3 3
    2 3
    3 4
    2 4
    """
    n, m, k = map(int, input().strip().split())
    objects = [tuple(map(int, input().strip().split())) for _ in range(n)]
    print(process(k, objects))  # output 8 with test 1 - output 10 with test 2 -> correct
