import numpy as np
from quantpsych.prospect import prelec

def prelec(p, delta):
    return np.power(np.exp(-(-np.log(p))), delta)


alpha = 0.88
delta = 0.60



x = np.linspace(0,10,101)
PTV = np.power(x, alpha)

import matplotlib.pyplot as plt

plt.plot(x, PTV)
plt.xlabel("Actual Value")
plt.ylabel("Perceived Value")
plt.show()

p = np.linspace(0,1, 101)[1:]
wp = prelec(p, delta)

plt.plot(p,wp, "r-")
plt.plot(p, p, "b-")
plt.show()


a = 0.5
x = [100, 135, 200, 80, 200, 600, 1000]
p = [0.3, 0.4, 0.3, 0.2, 0.1, 0.05, 0.001]
CE = [9.93, 20.91, 19.65, 4.29, 4.06, 4.88, 0.88]

U_x = np.power(x, a)
U_CE = np.power(CE, a)
w = U_CE/U_x

d_range = np.linspace(0, 2, 201)[1:]
AllError = []
for d in d_range:
    wp = prelec(p, d)
    error = np.power(np.sum(wp - w),2)
    AllError.append(error)
print(AllError)

ErrorMin = min(AllError)
index = np.argmin(AllError)
Optimal_d = d_range[index]

p_plot = np.linspace(0,1, 101)[1:]
wp_plot = prelec(p_plot, Optimal_d)

plt.plot(p_plot, wp_plot, "r-")
plt.plot(p_plot, p_plot, "b-")
plt.show()
