import matplotlib.pyplot as plt
import numpy as np

size = 500
iterations = 100

def julia(m, size, iterations, c):
    for i in range(size):
        for j in range(size):
            z = -2 + 4. / size * j + 1j * (1.5 - 3. / size * i)
            for n in range(iterations):
                if np.abs(z) <= 6.0:
                    z = z * z + c
                    m[i, j] = n
                else:
                    break


jul = np.zeros((size, size))
julia(jul, size, iterations, -0.8 + 0.156j)

plt.figure(figsize=(20, 15))
plt.imshow(jul, cmap=plt.cm.hot)
plt.xticks([])
plt.yticks([])
plt.show()