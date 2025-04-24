import numpy as np
from tqdm import tqdm
from matplotlib import pyplot as plt


def create_matrix(p, size=5):
    q = 1 - p

    matrix = np.diag([p] * size)
    matrix = np.concatenate((np.ones((size, 1)) * q, matrix), axis=1)
    tmp_row = np.array([1] + [0] * size)
    matrix = np.concatenate((matrix, tmp_row.reshape(1, -1)), axis=0)

    return matrix


def get_Pi(size=6):
    return np.random.rand(size, 1).reshape(1, size)


matrix = create_matrix(0.7, size=10)

# Pi = get_Pi()
# for i in tqdm(range(100_00000)):
#     Pi = Pi @ matrix
# print(Pi @ matrix)


def plot_first_coordinate(Pi, matrix, iterations=100):
    p = 0.7
    first_coordinates = []
    tmp_matrix = matrix.copy()
    for _ in range(iterations):
        Pi = Pi @ matrix
        tmp_matrix = tmp_matrix @ matrix
        first_coordinates.append(Pi[0, 0])
        if np.all(tmp_matrix > 0):
            print("All elements are positive, breaking the loop.", _)
            break

    plt.plot(range(iterations), first_coordinates)
    plt.xlabel("Iterations")
    plt.ylabel("First Coordinate")
    plt.axhline(y=((1 - p) / ( 1 - p ** 5)), color="r", linestyle="--")
    plt.title("First Coordinate over Iterations")
    plt.show()


plot_first_coordinate(get_Pi(11), matrix)
