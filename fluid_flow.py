# ============================================================
# Bernoulli Flow Simulation
# Author: aaditrip1
# Description: Models 2D fluid flow through a diverging channel
# defined by two parabolic curves. Applies the continuity equation
# (Q = v*A) to compute velocity and Bernoulli's principle to derive
# pressure distribution. Outputs 5 plots: channel geometry,
# velocity distribution, velocity gradient, pressure distribution,
# and pressure gradient.
# Dependencies: numpy, matplotlib, scipy
# ============================================================

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Define the functions
def f(x):
    return 0.001 * x**2 + 20

def q(x):
    return -0.001 * x**2 + 10

# Define the absolute difference between the functions
def diff(x):
    return abs(f(x) - q(x))

# Integration range
a, b = 0, 100

# Integrate the absolute difference to find the area between the functions
area, _ = quad(diff, a, b)
print(f'The area between the two functions from x={a} to x={b} is: {area}')

# Generate x values
x = np.linspace(a, b, 101)

# Compute y values for each function
y_f = f(x)
y_q = q(x)

# Compute the absolute difference at each x value
A = diff(x)

# Define the flow rate
Q = 5000  # cm^3/s

# Define density of the liquid
rho = 1  # g/cm^3

# Define initial velocity
v0 = 500  # cm/s

# Define initial pressure
P0 = 0.5 * rho * v0**2

# Define constant
C = P0 + 0.5 * rho * v0**2

# Define the velocity function
def velocity(A):
    return Q / A

# Compute velocity values
v = velocity(A)

# Compute the change in pressure
def compute_pressure(C, v, rho):
    return C - (0.5 * rho * v**2)

# Compute pressure values
P = compute_pressure(C, v, rho)

# Create the subplots
fig, axs = plt.subplots(5, 1, figsize=(10, 30))

# Plot 1: Channel geometry
axs[0].plot(x, y_f, label='f(x) = 0.001x^2 + 20', color='black')
axs[0].plot(x, y_q, label='q(x) = -0.001x^2 + 10', color='black')
axs[0].fill_between(x, y_f, y_q, where=(y_f > y_q), color='grey', alpha=0.5, label='Area between f(x) and q(x)')
axs[0].set_title('Area between f(x) and q(x)')
axs[0].set_xlabel('x (centimeters)')
axs[0].set_ylabel('y')
axs[0].legend()
axs[0].grid(True)

# Plot 2: Velocity scatter
scatter = axs[1].scatter(x, v, c=v, cmap='Blues', label='Velocity')
axs[1].set_title('Velocity as a function of x')
axs[1].set_xlabel('x (centimeters)')
axs[1].set_ylabel('Velocity (cm/s)')
axs[1].legend()
axs[1].grid(True)
cbar = fig.colorbar(scatter, ax=axs[1])
cbar.set_label('Velocity (cm/s)')

# Plot 3: Area with velocity gradient
sm = plt.cm.ScalarMappable(cmap='Blues', norm=plt.Normalize(vmin=v.min(), vmax=v.max()))
for i in range(len(x) - 1):
    axs[2].fill_between(x[i:i+2], y_f[i:i+2], y_q[i:i+2],
                        color=plt.cm.Blues((v[i] - v.min()) / (v.max() - v.min())), alpha=0.5)
axs[2].plot(x, y_f, color='black')
axs[2].plot(x, y_q, color='black')
axs[2].set_title('Area with Velocity Gradient')
axs[2].set_xlabel('x (centimeters)')
axs[2].set_ylabel('y')
axs[2].grid(True)
cbar = fig.colorbar(sm, ax=axs[2])
cbar.set_label('Velocity (cm/s)')

# Plot 4: Pressure
axs[3].plot(x, P, label='Pressure', color='red')
axs[3].set_title('Pressure as a function of x')
axs[3].set_xlabel('x (centimeters)')
axs[3].set_ylabel('Pressure (g/cm^2)')
axs[3].legend()
axs[3].grid(True)
scatter = axs[3].scatter(x, P, c=P, cmap='Reds')
cbar = fig.colorbar(scatter, ax=axs[3])
cbar.set_label('Pressure (g/cm^2)')

# Plot 5: Area with pressure gradient
sm = plt.cm.ScalarMappable(cmap='Reds', norm=plt.Normalize(vmin=P.min(), vmax=P.max()))
for i in range(len(x) - 1):
    axs[4].fill_between(x[i:i+2], y_f[i:i+2], y_q[i:i+2],
                        color=plt.cm.Reds((P[i] - P.min()) / (P.max() - P.min())), alpha=0.5)
axs[4].plot(x, y_f, color='black')
axs[4].plot(x, y_q, color='black')
axs[4].set_title('Area with Pressure Gradient')
axs[4].set_xlabel('x (centimeters)')
axs[4].set_ylabel('y')
axs[4].grid(True)
cbar = fig.colorbar(sm, ax=axs[4])
cbar.set_label('Pressure (g/cm^2)')

plt.tight_layout()
plt.show()