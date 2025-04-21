
## Adaptive‑control derivation (pendulum with quadratic friction)

### 1. Plant model
$$
\begin{aligned}
\dot{\theta}&=\omega\\
\dot{\omega}&=\frac{g}{l}\sin\theta+\frac{u}{ml^{2}}-C\omega^{2}\operatorname{sgn}(\omega)
\end{aligned}
$$

### 2. Mechanical energy  
$$
E=\frac12ml^{2}\omega^{2}+mgl\bigl(\cos\theta-1\bigr)
$$
Let $E_{0}$ be the desired energy.  
Define the energy error $\,\varepsilon_E=E-E_{0}\,$.

### 3. Lyapunov candidate  
$L=\dfrac{\varepsilon_E^{2}}{2}+\dfrac{\tilde C^{2}}{2\alpha}$ with $\tilde C=\hat C-C$.

### 4. Time derivative of $L$
Total‑energy rate  
$$
\dot{E}=\omega u-Cml^{2}\lvert\omega\rvert^{3}
$$
Derivative of the Lyapunov function  
$$
\dot{L}=\varepsilon_E\bigl(\omega u-\hat Cml^{2}\lvert\omega\rvert^{3}\bigr)+\frac{1}{\alpha}\tilde C\dot{\hat C}
$$

### 5. Adaptation law  
$$
\dot{\hat C}=\alpha\varepsilon_Eml^{2}\lvert\omega\rvert^{3}
$$
Substituting eliminates the $\tilde C$ term in $\dot L$:
$$
\dot{L}=\varepsilon_E\bigl(\omega u-Cml^{2}\lvert\omega\rvert^{3}\bigr)
$$

### 6. Control law  
$$
u=-k\operatorname{sgn}(\omega\varepsilon_E)+\hat Cml^{2}\lvert\omega\rvert\omega,\qquad k>0
$$
Then
$$
\dot{L}=-k\lvert\omega\rvert\lvert\varepsilon_E\rvert\le0
$$

### 7. Result  
$$
\boxed{\dot{L}=-k\lvert\omega\rvert(E-E_{0})}
$$
Hence $L$ is non‑increasing; the energy error $\varepsilon_E$ and the parameter error $\tilde C$ converge to zero.