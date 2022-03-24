
# 2d tracking filter
Goal: estimate the position and velocity of a moving obj based on *REMOTE* measurements

##  1-d demo 
* Assuming constant acceleration:
  $$ v = v_0 + at $$
  $$ p = p_0 + t v_0 + \frac{1}{2} at^2 $$

* In matrix form: 
$$
\begin{bmatrix}
p \\
v 
\end{bmatrix}
= 
\begin{bmatrix}
1 & t \\
0 & 1 
\end{bmatrix}

\begin{bmatrix}
p_0 \\
v_0
\end{bmatrix}

+
\begin{bmatrix}
\frac{1}{2} t^2 \\
t
\end{bmatrix} 
a
$$

* We could also transform this to discrete time: $t = \Delta t$
$$
\begin{bmatrix}
p \\
v 
\end{bmatrix}_k
= 
\begin{bmatrix}
1 & \Delta t \\
0 & 1 
\end{bmatrix}

\begin{bmatrix}
p\\
v
\end{bmatrix}_{k-1}

+
\begin{bmatrix}
\frac{1}{2} \Delta t^2 \\
\Delta t
\end{bmatrix} 
[a]
$$

## 2-d tracker demo
Dep var becomes:
$$
\begin{bmatrix}
p_x \\
p_y \\
v_x \\
v_y 
\end{bmatrix}
$$

## Process model 
$$X_k = F x_{k-1} + G \mu_{k-1}$$

Because we don't have G (no census on board), we drop the input and replace G with L, which is just noise. 

$$X_k = F x_{k-1} + L w_{k-1}$$
which is a linear combination of state transition matrix and input noise matrix. 

## Prediction step (state)

* We begin the estimation step with the initial condition $\hat{x_0}^+$, which is the best estimate of the initial state of the system.
* We want to propagate forward to find $\hat{x_1}^- = E(x_1)$, so can use the state space model of the system.
  $$  \hat{x_1}^- =F_0 \hat{x_0}^{+} + G_o u_0$$
* In general: 
 $$  \hat{x_k}^- =F_{k-1} \hat{x_{k-1}}^{+} + G_{k-1} u_{k-1}$$

 ## Prediction step (covariance)
 * To account for new uncertainty in the system due to the process model noise we add a new covariance term:
 $$ P_1^{-} = F_0 P_0^+ F_0^T + L_0 Q_0 L_0^T$$
* It is usually assumed that process noise is additive, and so $L_k = I$, which means the eq can be simplified to:  
$$ P_1^{-} = F_0 P_0^+ F_0^T + Q_0$$

* Thus, in summary of prediction step: update both mean and covariance 
 $$  \hat{x_k}^- =F_{k-1} \hat{x_{k-1}}^{+} + G_{k-1} u_{k-1}$$
 $$ P_k^{-} = F_{k-1} P_{k-1}^+ F_{k-1}^T + Q_{k-1}$$


 ## System model (prediction step summary)
 1. Process model
  $$X_k = F x_{k-1} + L \mu_{k-1}$$
 2. Process noise model 
 $$ P_k^{-} = F P_{k-1}^+ F^T + L Q L^T$$

## Update step (state)
* Recall measurement model:
  $$z_k = H_k x_k + M_k v_k$$
* And recall "+" denotes a posteriori, and "-" denotes a priori. In the proces stage, we use a posteriori to come up to prediction, now in the update step, we update the state prediction $\hat{x_k}^-$, with the current measurement, $z_k$, to generate updated state estimate $\hat{x_k}^+$, which will be a weighted estimated because the error between measurement $z_k$ and predicted measurement calculated from $H_k \hat{x_k}^-$.
* Innovation 
  $$\tilde{y_k} = z_k  - H_k \hat{x_k}$$
* Innovation covariance
  $$S_k = H_k P_k^-H_k^T + R_k$$ 
  when $M = I$.
  More generally, 
  $$R_k = M_k R_k M_k^T$$ 
* Notations summary 

  $z_k \sim$ measurement vector

  $\hat{z_k} \sim$ predicted measurement vector

  $\tilde{y_k} \sim$ measurement innovation (error) vector

  $S_k \sim$ innovation covariance matrix   

* Kalman Gain matrix $K_k$
  
  Update function:

  $$\hat{x_k}^+ = \hat{x_k}^- + K_k \tilde{y_k}$$
  where Kalman gain is defined as:
  $$K_k = P_K^- H_k^T S_k^{-1}$$

  Note: it looks exactly like recursive least squares equation. 


## Update step (covariance)
* The covariance of the estimate must change.
* Covariance update:
  $$ P_k^+ = (I - K_k H_k) P_k^- $$


## Update step (summary)

1. Updated (a posteriori) state estimate:
  $$ \tilde{x_k}^+ =  \tilde{x_k}^- + K_k (z_k - H_k \hat{x_k}^-)$$

2. Updated (a posteriori) coveriance estimate:
   $$P_k^+ = (I - K_k H_k) P_k^-$$

3. Kalman gain:
   $$K_k = P_k^- H_k^T S_k^{-1}$$

4. Innovation covariance:
   
   $$ S_k = H_k P_k^{-1} H_k^T + R_k$$

## 2-d tracker demo 

Simplified measurement model:
$$ z_k = H x_k + v_k$$

* $z_k$ is just a 2 x 1 matrix representing the measurement of position of x and y: $[p_x, p_y]^T$
* $H = [[1, 0, 0, 0], [0, 1, 0, 0]]$
* Additive noise $v_k \sim N(0,R)$ with $\sigma_x = \sigma_y = \sigma_{means}$

## Some quick remarks
1. Covariance profile
   Recall prediction step:
   $$P_k^{-1} = F_{k-1} P_{k-1}^+ F_{k-1}^T + Q_{k-1}$$
   as well as update step:
   $$S_k = H_k P_k^{-1} H_k^T + R_k $$

  - Generally, Q and R capture variance in the noise term in process and measurement process. So, larger Q, larger R --> slow update. Ideally, smaller Q, smaller R --> faster update. 
  - We can work out an error budget. 