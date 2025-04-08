import numpy as np
import matplotlib.pyplot as plt

# Constants
h0 = 10  # Initial height (meters)
G = 6.67e-11  # Gravitational constant (m^3 kg^-1 s^-2)

# Earth
M_earth = 5.97e24  # kg
r_earth = 6_371_000  # meters
g_earth = G * M_earth / r_earth**2  # ~9.8 m/s^2
r0_earth = r_earth + h0

# Jupiter
M_jupiter = 1.898e27  # kg
r_jupiter = 69_911_000  # meters
g_jupiter = G * M_jupiter / r_jupiter**2  # ~24.79 m/s^2
r0_jupiter = r_jupiter + h0

# Sun
M_sun = 1.989e30  # kg
r_sun = 696_000_000  # meters
g_sun = G * M_sun / r_sun**2  # ~274 m/s^2
r0_sun = r_sun + h0

# Time to hit surface
t_max_earth = np.sqrt(2 * h0 / g_earth)  # ~1.43 s
t_max_jupiter = np.sqrt(2 * h0 / g_jupiter)  # ~0.90 s
t_max_sun = np.sqrt(2 * h0 / g_sun)  # ~0.27 s
t_earth = np.linspace(0, t_max_earth, 100)
t_jupiter = np.linspace(0, t_max_jupiter, 100)
t_sun = np.linspace(0, t_max_sun, 100)

# Spatial paths
h_earth = h0 - 0.5 * g_earth * t_earth**2
h_jupiter = h0 - 0.5 * g_jupiter * t_jupiter**2
h_sun = h0 - 0.5 * g_sun * t_sun**2

# Spacetime paths (relative to surface)
r_earth_rel = (r0_earth - 0.5 * g_earth * t_earth**2) - r_earth
r_jupiter_rel = (r0_jupiter - 0.5 * g_jupiter * t_jupiter**2) - r_jupiter
r_sun_rel = (r0_sun - 0.5 * g_sun * t_sun**2) - r_sun

# Plot 1: Spatial Path Comparison
plt.figure(figsize=(12, 6))
plt.plot(t_earth, h_earth, 'b-', label=f'Earth (g = {g_earth:.1f} m/s²)')
plt.plot(t_jupiter, h_jupiter, 'y-', label=f'Jupiter (g = {g_jupiter:.2f} m/s²)')
plt.plot(t_sun, h_sun, 'r-', label=f'Sun (g = {g_sun:.0f} m/s²)')
plt.xlabel('Time (s)')
plt.ylabel('Height above surface (m)')
plt.title('Geodesic: Free Fall from 10m (Earth vs. Jupiter vs. Sun)')
plt.grid(True)
plt.legend()
plt.show()

# Plot 2: Spacetime Path Comparison
plt.figure(figsize=(12, 6))
plt.plot(t_earth, r_earth_rel, 'b-', label=f'Earth (g = {g_earth:.1f} m/s²)')
plt.plot(t_jupiter, r_jupiter_rel, 'y-', label=f'Jupiter (g = {g_jupiter:.2f} m/s²)')
plt.plot(t_sun, r_sun_rel, 'r-', label=f'Sun (g = {g_sun:.0f} m/s²)')
plt.xlabel('Time (s)')
plt.ylabel('Height above surface (m)')
plt.title('Spacetime Geodesic: Free Fall from 10m (Earth vs. Jupiter vs. Sun)')
plt.grid(True)
plt.legend()
plt.ylim(0, 10)  # Zoom in
plt.show()

# Print key values
print(f"Earth: Time = {t_max_earth:.2f} s, Speed = {g_earth * t_max_earth:.1f} m/s")
print(f"Jupiter: Time = {t_max_jupiter:.2f} s, Speed = {g_jupiter * t_max_jupiter:.1f} m/s")
print(f"Sun: Time = {t_max_sun:.2f} s, Speed = {g_sun * t_max_sun:.1f} m/s")
