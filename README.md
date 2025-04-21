# Pendulum Stabilization with Adaptive Controller

## Overview

This project demonstrates the stabilization of a pendulum system using adaptive control techniques. The simulation explores different control strategies, including energy-based control and adaptive parameter estimation.

The derivation is described in [derivation.png](./derivation.png).

## System Dynamics

The pendulum system with friction is modeled by the following equations:

$$
\dot{\vartheta} = \omega \quad \dot{\omega} = -\frac{3g}{2l}\sin(\vartheta) + \frac{3}{ml^2}\tau - C \omega^2 \text{sign}(\omega)
$$

where:
- $m = 0.337$ kg — pendulum mass
- $l = 0.127$ m — pendulum length
- $g = 9.81$ m/s² — gravity constant
- $C = 0.08$ — friction coefficient
- $(\vartheta, \omega)$ — angle and angular velocity (state variables)
- $\tau$ — torque (control action)

## Features

- Energy-based control with known friction parameters
- Adaptive control that estimates friction coefficients online
- Comparative analysis of control strategies

## Prerequisites

- Python 3.8+
- [uv](https://github.com/astral-sh/uv) for package management

If you don't have uv installed, run:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/yourusername/adaptive-pendulum.git
cd adaptive-pendulum
```

## Running the Simulation

Three simulation modes are available:

```bash
# 1. Energy-based control with zero friction coefficient (fails to stabilize)
uv run eval.py --eval-type energy_based --friction-coeff=0.0

# 2. Energy-based control with correct friction coefficient (stabilizes)
uv run eval.py --eval-type energy_based --friction-coeff=0.08

# 3. Adaptive control (stabilizes by estimating friction parameters online)
uv run eval.py --eval-type adaptive
```

## Results

The simulations demonstrate:
### Standard energy-based control Standard energy-based control fails when friction is present but not accounted for
<p align="center">
  <img src="videos/energy_based_friction_coef_0.0/output.gif" alt="succed_eb">
</p>


### Energy-based control succeeds when the exact friction coefficient is known
<p align="center">
  <img src="videos/energy_based_friction_coef_0.08/output.gif" alt="succed_eb">
</p>

### Adaptive control successfully stabilizes the pendulum by learning the friction coefficient during operation

<p align="center">
  <img src="videos/adaptive/output.gif" alt="failed">
</p>
