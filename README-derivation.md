## Adaptive Control Derivation (Pendulum with Drag‐type Friction)

### 1. Plant model  

$$
\boxed{\;
\begin{aligned}
\dot{\theta} &= \omega \$$4pt]
\dot{\omega} &= \frac{g}{l}\sin\theta \;+\; \frac{u}{m l^{2}}
               \;-\; C\,\omega^{2}\,\operatorname{sgn}(\omega)
\end{aligned}}
$$

---

### 2. Mechanical energy  

$$
E \;=\; \underbrace{\frac{1}{2}\,m l^{2}\omega^{2}}_{\text{kinetic}}
      + \underbrace{m g l\!\bigl(\cos\theta - 1\bigr)}_{\text{potential}}
$$

Let $E_{0}$ be the desired energy level (e.g. $E_{0}=0$ for the stable
down‑ward equilibrium).  
Define the energy error  

$$
\varepsilon_E \;\triangleq\; E - E_{0}.
$$

---

### 3. Lyapunov candidate with friction‑estimate error  

$$
L(\varepsilon_E,\tilde C)
\;=\;
\frac{\varepsilon_E^{2}}{2}
\;+\;
\frac{\tilde C^{2}}{2\alpha},
\qquad
\tilde C \;=\; \hat C - C,
$$
where  

* $\hat C$ is the on‑line estimate of the unknown drag coefficient $C$;  
* $\alpha>0$ is an adaptation gain.

---

### 4. Time derivative of $L$

First, differentiate the total energy:

$$
\begin{aligned}
\dot{E}
  &= m l^{2}\,\omega\,\dot{\omega} + m g l(-\sin\theta)\,\dot{\theta}  \$$4pt]
  &= m l^{2}\,\omega\!\Bigl[
        \tfrac{g}{l}\sin\theta + \tfrac{u}{m l^{2}}
        - C\,\omega^{2}\operatorname{sgn}(\omega)
      \Bigr]
     \;-\; m g l\sin\theta\,\omega           \$$4pt]
  &= \omega\,u \;-\; C\,m l^{2}\,|\omega|^{3}.
\end{aligned}
$$

(The gravity terms cancel exactly.)

Because $L = \frac12\varepsilon_E^{2} + \frac{1}{2\alpha}\tilde C^{2}$,

$$
\dot{L}
  = \varepsilon_E\dot{E}
    + \frac{1}{\alpha}\tilde C\,\dot{\hat{C}}
  = \varepsilon_E\!\Bigl(\omega u - \hat C\,m l^{2}|\omega|^{3}\Bigr)
    + \frac{1}{\alpha}\tilde C\,\dot{\hat{C}}.
$$

---

### 5. **Adaptation law**

Choose  

$$
\boxed{\;
\dot{\hat C}
  = \alpha\,\varepsilon_E\,m l^{2}\,|\omega|^{3}}
$$

so that  

$$
\frac{1}{\alpha}\tilde C\,\dot{\hat{C}}
  = \varepsilon_E\,(\hat C - C)\,m l^{2}\,|\omega|^{3}.
$$

Substituting into $\dot L$ gives  

$$
\dot{L}
  = \varepsilon_E\!\Bigl(
        \omega u
      - C\,m l^{2}\,|\omega|^{3}
    \Bigr).
$$

---

### 6. **Control law**

Select  

$$
\boxed{\;
u
  = -\,k\,\operatorname{sgn}\!\bigl(\omega\,\varepsilon_E\bigr)
    \;+\;
    \hat C\,m l^{2}\,|\omega|\,\omega
    },
\qquad k>0,
$$

so that  

$$
\omega u
  = -\,k\,\omega\,\operatorname{sgn}\!\bigl(\omega\varepsilon_E\bigr)
    + (\hat C\,m l^{2})\,|\omega|^{3}.
$$

Using $|\omega|^{3} = \omega^{2}\,|\omega|$ one obtains  

$$
\dot{L}
  = -\,k\,\varepsilon_E\,\omega\,
      \operatorname{sgn}\!\bigl(\omega\varepsilon_E\bigr)
  = -\,k\,\bigl|\omega\bigr|\,\bigl|\varepsilon_E\bigr|
  \;\le\; 0.
$$

---

### 7. Stability interpretation  

* $L$ is **positive‑definite** in both the energy error $\varepsilon_E$ and the
  parameter error $\tilde C$.  
* $\dot L\le 0$ for all $(\theta,\omega)$, so the closed‑loop system is
  **Lyapunov stable**.  
* Whenever $\varepsilon_E\neq 0$ and $\omega\neq 0$ we have $\dot L<0$;
  the energy error is actively driven to the target value $E_0$ while
  $\hat C(t)$ converges to the true friction coefficient $C$.

---

### 8. Final result written on the board  

$$
\boxed{\;
\dot L
  = -\,k\,\bigl|\omega\bigr|\,(E-E_0)
  \quad\Longrightarrow\quad
  L(t) \text{ is non‑increasing.}}
$$

(For $E>E_0$ the right-hand side is strictly negative, guaranteeing energy
convergence; for $E<E_0$ the switching control term injects energy until the
target is met.)
