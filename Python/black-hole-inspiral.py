import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from mpl_toolkits.mplot3d import Axes3D

def simulate_black_hole_inspiral(initial_r=50, initial_v=17.5, mass=10, steps=60000, dt=0.001):
    """Simulates realistic inspiral into a Schwarzschild black hole"""
    # Initialize arrays
    r = np.zeros(steps)
    theta = np.zeros(steps)
    r[0] = initial_r
    v_r = 0
    v_theta = initial_v / initial_r
    R_s = 2 * mass  # Schwarzschild radius
    
    # Simulation loop with gravitational wave decay
    for i in range(steps-1):
        # General Relativity correction (1/r^3 term)
        gr_correction = 3 * mass * (v_theta**2) / (r[i]**2)
        
        # Gravitational wave energy loss (Peters 1964 approximation)
        gw_loss = - (32/5) * (mass**2) * (r[i]**4) * (v_theta**6) * 1e-5
        
        # Total acceleration
        accel = -mass/r[i]**2 - gr_correction + gw_loss
        
        # Update velocities and positions
        v_r += accel * dt
        r[i+1] = max(r[i] + v_r*dt, R_s*1.01)  # Stop at 1% outside horizon
        
        # Angular momentum evolution
        v_theta *= (1 - 0.0001*r[i]*dt)  # Radius-dependent decay
        
        theta[i+1] = theta[i] + v_theta*dt
        
        if r[i+1] <= R_s*1.01:
            break
    
    # Convert to Cartesian
    x = r[:i+2] * np.cos(theta[:i+2])
    y = r[:i+2] * np.sin(theta[:i+2])
    
    return x, y, R_s, mass

def plot_inspiral(x, y, R_s, mass):
    """Creates publication-quality visualization with enhanced color visibility"""
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111)
    
    # Enhanced color-mapped spiral
    points = np.array([x, y]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)
    
    # Use more vibrant colormap and wider linewidth
    lc = LineCollection(segments, cmap='viridis',  # More perceptually uniform than plasma
                      norm=plt.Normalize(0, len(x)),
                      linewidth=3.5,  # Thicker lines
                      alpha=0.95)     # Less transparency
    lc.set_array(np.linspace(0, 100, len(x)))
    ax.add_collection(lc)
    
    # Black hole features with better visibility
    ax.add_artist(plt.Circle((0,0), R_s, color='red', 
                          fill=False, linestyle='-', linewidth=3))  # Solid line
    ax.add_artist(plt.Circle((0,0), R_s*2, color='gold',  # Brighter accretion disk
                          fill=False, alpha=0.5, linewidth=6))
    ax.scatter(0, 0, color='black', s=500, zorder=10)
    
    # 3D subplot with matching colors
    ax_3d = fig.add_axes([0.68, 0.68, 0.25, 0.25], projection='3d')
    z = np.linspace(0, 10, len(x))
    ax_3d.plot(x, y, z, c='lime', alpha=0.9, linewidth=2)  # Brighter 3D line
    ax_3d.set_xticks([])
    ax_3d.set_yticks([])
    ax_3d.set_zticks([])
    ax_3d.set_title("Spacetime View", fontsize=9, pad=0)
    ax_3d.grid(False)
    
    # Automatic zoom to show full color range
    spiral_radius = max(np.max(np.abs(x)), np.max(np.abs(y)))
    view_radius = max(spiral_radius, R_s*2.5)  # Ensure we see full spiral and disk
    
    ax.set_xlim(-view_radius, view_radius)
    ax.set_ylim(-view_radius, view_radius)
    
    # Colorbar with better labeling
    cbar = fig.colorbar(lc, ax=ax, pad=0.02, shrink=0.8)
    cbar.set_label("Time Progression", rotation=270, labelpad=20, fontsize=12)
    
    plt.title(f"Black Hole Inspiral (Mass = {mass} $M_\odot$)", fontsize=16, pad=20)
    plt.savefig('black_hole_inspiral_enhanced.png', dpi=300, bbox_inches='tight')
    plt.show()

# Run simulation and plot
x, y, R_s, mass = simulate_black_hole_inspiral()
plot_inspiral(x, y, R_s, mass)
