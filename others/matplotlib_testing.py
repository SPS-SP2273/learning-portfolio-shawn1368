# %%
# Initialisation
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pylustrator
pylustrator.start()
# %%
# Contour
x = np.linspace(-4, 4, 9)
y = np.linspace(-5, 5, 11)

# The meshgrid function returns
# two 2-dimensional arrays
x_1, y_1 = np.meshgrid(x, y)

ellipse = x_1 * 2 + 4 * y_1 ** 2

plt.contourf(x_1, y_1, ellipse, cmap = 'jet')

plt.colorbar()

plt.show()
#%%
# 3D
x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)

# The meshgrid function returns
# two 2-dimensional arrays
x_1, y_1 = np.meshgrid(x, y)

z_1 = np.sin(np.sqrt(x_1 ** 2 + y_1 ** 2))

fig1, ax1 = plt.subplots(subplot_kw={"projection": "3d"})
surf = ax1.plot_surface(x_1, y_1, z_1, cmap="coolwarm")
# ax1.plot_wireframe(x_1, y_1, z_1)
fig1.colorbar(surf, shrink=0.5, aspect=5)

plt.show()
# %%
# Imshow
Z = np.random.uniform(0, 1, (16, 16))
plt.imshow(Z, cmap="viridis")
plt.colorbar()
plt.show()

# %%
# 3D
x_line = np.linspace(-10, 10, 1000)
y_line = np.linspace(-10, 10, 1000)
X, Y = np.meshgrid(x_line, y_line)
Z = X ** 2 - 2 * Y * X + Y ** 3

fig, ax = plt.subplots()
ax.contourf(X, Y, Z)
# ax.colorbar()
plt.show()
# %%
# Scatter
scatter_data_x = np.random.randint(0, 101, 100)
scatter_data_y = np.random.randint(0, 101, 100)
fig2, ax2 = plt.subplots()
ax2.scatter(scatter_data_x, scatter_data_y)

plt.show()
# %%
# Bar
x_axis = ["Thing 1", "Thing 2", "Thing 3", "Thing 4"]
y_axis = np.array([275, 28, 182, 375])

fig3, ax3 = plt.subplots()
ax3.barh(x_axis, y_axis)
fig3.show()