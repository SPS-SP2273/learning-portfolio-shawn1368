# %%
# Initialisation
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# %%
a = np.arange(5)
print(a)
# %%
c = np.eye(10)
print(c)
# %%
d = np.empty((2, 3))
print(d)
# %%
e = np.diag([4,9,2])
print(e)
# %%
f = np.arange(20)
np.select([f > 3], [f])
# %%
np.meshgrid([2,2], [3, 1, 2])
# %%
T = np.linspace(0, np.pi * 5, 100)
Y = np.cos(T)

fig1, ax1 = plt.subplots()
ax1.plot(T, Y)
# %%
rand_2d_arr = np.random.randint(0, 101, (32, 32))

fig2, ax2 = plt.subplots()
ax2.imshow(rand_2d_arr, cmap="gray")
# %%
zero_array = np.zeros((6, 5))

for i in range(2, 7):
    zero_array[i - 1, i - 2] = i

print(zero_array)    
# %%
rep_array = np.tile([[4, 3], [2, 1]], (2, 3))
print(rep_array)