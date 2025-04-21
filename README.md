## Pendulum stabilization with adaptive controller

## Overview

We consider the system

$$
\dot{\vartheta} = \omega \quad \dot{\omega} = -\frac{3g}{2l}\sin(\vartheta) + \frac{3}{ml^2}\tau
$$

## 🚀 Quick Start

### Prerequisites

If you don't have [uv](https://github.com/astral-sh/uv) (a fast Python package installer and resolver) installed, run:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Running the Simulation

To run the :

```bash
# This should fail to stabiolize due to the fact that default pendulum system has friction
uv run run/eval.py --eval-type energy_based --friction-coeff=0.0
# This now stabilizes due to the fact that controller now awares of friction coeff
uv run run/eval.py --eval-type energy_based --friction-coeff=0.08
# This now will stabailize because friction coeff is adapted in online setting
uv run run/eval.py --eval-type adaptive
```

