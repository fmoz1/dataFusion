# Linear Dynamic Systems
## Differential Equations
* ODE 
  $$ \frac{d}{dx}f(x)$$
* PDE 
  $$\frac{\partial}{\partial x}f(x,y)$$
* n-th order equation order
  $$f_n (.)\frac{d^n y}{d x^n} + ... + f_1(.) \frac{dy}{dx} + f(0)(.)y = g(.)$$
* Linear vs non-linear
  + Linear equations satisfy: (i) additivity (ii) homogeneity 
  + Linear ODE: e.g. $\frac{dy}{dx} + cy + x^2 =0$

## State-space representation 
* Newton's dot notation
  $$ \dot x = \frac{dx}{dt} $$

* A system of equations with n states and m inputs
  $$ \dot x_1  = f_1 (t, x_1, x_2, ...., x_n, \mu_1, \mu_2 .... \mu_m)$$
  $$ \dot x_2  = f_1 (t, x_1, x_2, ...., x_n, \mu_1, \mu_2 .... \mu_m)$$
  $$ \dot x_3  = f_1 (t, x_1, x_2, ...., x_n, \mu_1, \mu_2 .... \mu_m)$$
  $$...$$
  $$ \dot x_n  = f_1 (t, x_1, x_2, ...., x_n, \mu_1, \mu_2 .... \mu_m)$$

* A simplified version 
  $$ \dot x(t) = f(t, x(t), \mu(t))$$
  where $\dot x(t)$ is called the state rate.

  State vector:
  $$ x(t) = [x_1(t), x_2(t), ..., x_n(t)]^T $$

  Input vector:
  $$ x(t) = [\mu_1(t), \mu_2(t), ..., \mu_n(t)]^T $$

## D.E and state space
* The state variabels are the DV of the state equations.
* Recall Newton's Equation:
  $$ F(t) = m \ddot x(t)$$
  $$ \dot x(t) = f(t, x(t), \mu(t))$$
* How can we combine both?
  Recall $\ddot x(t) = a(t), \dot x(t) =v(t)$.
  So, we can form 
  
  1. a state rates vector
$$
\dot x(t) = \begin{bmatrix}
\dot v(t) \\ 
\dot x(t)
\end{bmatrix}
$$
2. a state vector
3. input vector
$$ \mu(t) = [F(t)]$$

* Thus, we can turn higher order ODE into first order state space representation.
* The states are all the lower order derivatives. 
  
  ## Continuous vs. discrete time
* The D.Es shown so far have been in "continuous" time
* Many states are known at a discrete set of point in time, e.g., $t_0, ..., t_k, t_{k+1}$

* Categorization 
  ```mermaid 
  flowchart TB
  state_space_representation --> continuous
    state_space_representation --> discrete
    continuous --> nonlinear_c
    continuous --> linear_c
    discrete --> nonlinear_d
    discrete --> linear_d
  ```
1. Continuous non-linear model
$$ \dot x(t)  = f(t, x(t), \mu(t)) $$ 
a very general function

2. Continuous linear model
 $$ \dot x(t)  = A(t) x(t) + B(t) \mu(t) $$ 

3. Discrete non-linear model
$$ x_{k+1} = f(t_k, x_k, \mu_k)$$ 
most general function among four

4. Discrete linear model 
5. $$ x_{k+1} = F_k x_k + G_k \mu_k$$ 

## Continuous to discrete model conversions 
We can link continuous to discrete through
Current time step: 
$$ t = t_k$$
Previous time step: 
$$ t_0 = t_{k-1}$$ 
Time step size: 
$$ \Delta t = t_k - t_{k-1}$$

Continuos to discrete conversion:

$$ x(t_k) = e^{A \Delta t } X(t_{k-1}) + e^{A \Delta t} \int_0^{\Delta t} e^{-A \alpha} d \alpha B u(t_{k-1})$$

$$ x_k = F x_{k-1} + G \mu_{k-1} $$

Thus,
$$ F = e^{A \Delta t}$$
$$ G = F \int_0^{\Delta t} e^{-A \alpha} d \alpha B = F[I - e^{-A \Delta t}] A^{-1} B $$ 
if $A^{-1}$ exists.

### Matrix Exponential
$$ e^{At} = \sum_{j=0}^{\infty} \frac{(At)^j}{j!}$$

First-order approximation 
$$ e^{At} \approx I + At$$

## Simulation of models 
* Usually, we are not able to solve integrals by finding an exact analytical solution. 
* Simulation = numerical integration. 

### Continuous time simulation
$$ \Delta x = \frac{dx}{dt} \Delta t $$

Thus, with Newton's dot notation, this becomes Euler's first order integration.

$$ x(t + \Delta t) = x(t) + \dot x(t) \Delta t $$ 

Features:
* Simplest integration method
* Least accurate
* Time step must be small to capture dynamics
* Can be numerically unstable (accuracy gets exponentially worse over time)
  

Procedures:
1. Assume an initial condition $x(0)$
2. Calculate the equation rate
   $$ \dot x(t) = f(t, x(t), \mu(t) $$
3. Integrate the time step 
   $$ x(t + \Delta t) = x(t) + \dot x(t) \Delta t $$
   with $t \rightarrow t + \Delta t$
4. Repeat the steps 2-3 as needed
   

### Second order mechanical system

e.g. unforced (*no input*) mass-spring-damper system

$$
\begin{bmatrix}
\dot v \\ 
\dot x
\end{bmatrix} =
\begin{bmatrix}
-\frac{b}{m} & -\frac{k}{m} \\
1 & 0\\ 
\end{bmatrix}

\begin{bmatrix}
v \\ 
x
\end{bmatrix}
$$

Demo using different time step sizes:
* Euler integration very susceptible to time step size 
* When time step becomes large, it becomes very inaccurate and even gets unstable results


### Discrete time simulation
No integration is nedded.

Procedures:
1. Assume an initial condition $x_9$
2. Step the solution 
   $$ x_{k+1} = F x_k + G \mu_k $$
   with $k\rightarrow k+1$
3. Repeat

Demo with 2nd order mechanism system in discrete form: 
* Valid
* Even when time step becomes big, $\Delta t = 2.0$, it captures all dynamics without Euler integration. 
* It gets implemented in real life (mathematicians may disagree...)
