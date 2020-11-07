import numpy as np

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

cric_data = np.loadtxt("cric_data.tsv", skiprows=1)

# print(cric_data)

Sachin = cric_data[:, 1]
Dravid = cric_data[:, 2]
India = cric_data[:, 3]

# print(Sachin, "Sachin")

# print(Dravid, "Dravid")

# print(India, "India")

# find mean and median for sachin and dravid


def calculateMeanAndMedian(value, name):
    message = f'mean of {name} is: '
    print(message, np.mean(value))
    message = f'median of {name} is: '
    print(message, np.median(value))
    # print("median of" + ' ' + name + ' ' + np.median(value))


# calculateMeanAndMedian(Sachin, "Sachin")
# calculateMeanAndMedian(Dravid, "Dravid")


def countCentury(value, name):
    message = f'Total numbers of centuries score by {name} is: '
    print(message, np.count_nonzero(value > 99))


countCentury(Sachin, "Sachin")
countCentury(Dravid, "Dravid")
# print(a.ndim)
# print(b.ndim)
# print(c.ndim)
# print(d.ndim)


# print(a[0])
# print(c[0, 2], "c")
# print(c.ndim)
# print(d.ndim)

# arr = np.array([1, 2, 3, 4, 5])
# x = arr.copy()
# arr[0] = 42

# arr_2 = np.array([1, 2, 56, 3, 2, 1])
# y = arr.view()
# arr[0] = 23

# # print(arr)
# # print(y)

# arr_3 = np.array([2, 6, 8, 1, 2, 64, ])
# view_1 = arr_3.view()
# copy_1 = arr_3.copy()

# print(view_1.base)
# print(copy_1.base)

# print(arr)
# print(x)
