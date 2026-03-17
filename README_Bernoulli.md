# Bernoulli Flow Simulation

A 2D fluid flow simulation using Python that models fluid behavior through a diverging channel. Applies the continuity equation and Bernoulli's principle to compute velocity and pressure distributions across the channel, then visualizes the results with color-mapped plots.

## Background

The channel is defined by two parabolic curves:
- Upper wall: f(x) = 0.001x² + 20
- Lower wall: q(x) = -0.001x² + 10

As the channel diverges, the cross-sectional area increases, causing velocity to decrease and pressure to increase — consistent with Bernoulli's principle.

## Physics

- **Continuity Equation**: Q = v · A — flow rate is conserved, so velocity decreases as area increases
- **Bernoulli's Principle**: P + ½ρv² = constant — pressure increases as velocity decreases
- **Flow Rate**: Q = 5000 cm³/s
- **Fluid Density**: ρ = 1 g/cm³
- **Initial Velocity**: v₀ = 500 cm/s

## Output

The script generates 5 plots:

1. **Channel Geometry** — the two parabolic walls with shaded area between them
2. **Velocity Distribution** — velocity as a function of x along the channel
3. **Velocity Gradient** — channel geometry color-mapped by velocity
4. **Pressure Distribution** — pressure as a function of x along the channel
5. **Pressure Gradient** — channel geometry color-mapped by pressure

## Dependencies

```
pip install numpy matplotlib scipy
```

## Run

```
python fluid_flow.py
```

## Author

aaditrip1  
github.com/aaditrip1
