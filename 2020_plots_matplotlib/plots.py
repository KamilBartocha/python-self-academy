import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(start=-10, stop=10, num=100)

plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))

plt.show()

fig = plt.figure()

plt.plot(x, x/2, '-')
plt.plot(x, np.sin(x), '*')
plt.plot(x, np.cos(x), '--')
plt.show()

plt.figure()  # create a plot figure

# create the first of two panels and set current axis
plt.subplot(2, 1, 1) # (rows, columns, panel number)
plt.plot(x, np.sin(x))

# create the second panel and set current axis
plt.subplot(2, 1, 2)
plt.plot(x, np.cos(x))
plt.show()
plt.style.use('seaborn-whitegrid')

fig = plt.figure()
ax = plt.axes()
plt.show()

fig = plt.figure()
ax = plt.axes()

