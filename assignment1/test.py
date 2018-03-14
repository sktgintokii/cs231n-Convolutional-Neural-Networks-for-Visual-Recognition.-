import numpy as np

x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6], [7, 8], [9, 10]])

print(np.sum((x ** 2)[:, np.newaxis] + y ** 2 - 2 * x[:, np.newaxis] * y, axis=2))

dist = np.zeros((len(x), len(y)))
for i in xrange(len(x)):
    for j in xrange(len(y)):
        dist[i][j] = np.sqrt(np.sum((x[i] - y[j]) ** 2))
print(dist)

print(x[0][:1])