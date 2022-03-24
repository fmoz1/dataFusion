# Kalman filter tuning 
# Kalman filter validation 
How can we tell if the filter is working?
- Compare KF state estimates with the true states
  + Use a simulation
  + Use an external reference system 
  
  State estimation error:
  $$ \tilde{x} = x - \hat{x} $$ 
  State estimation covariance: 
  $$ P = [(x-\hat{x}) ( x - \hat{x})^T] $$

- Compare innovation statistical properties
  + Zero mean
  + Innovation sequence variance should be similar to predicted innovation covariance in terms of *magnitude*
   
   Predicted covariance
   $$S_i = \begin{bmatrix}
    \sigma_x^2 & \sigma_x \sigma_y \\ 
    \sigma_y \sigma_x & \sigma_y^2 \\
   \end{bmatrix}$$

   $$ \sigma_x^2 = \frac{1}{N} \sum_{i=1}^N (x_i)^2$$

# Kalman filter tuning 
How can we tune the filter?
* Initial conditions:
  + $\hat{x_0}$: best guess or assumption about the initial state
  + $P_0$: variance which is large enough to encompass the truth 
* Covariance matrices
  + $R$: sensor measuremnt covariance --> properties of sensor 
    * Example: a sensor has two measurements 
        $$z_1 = x_1 +/- a$$
        $$z_2 = x_2 +/- b$$ 
        Hence, $\sigma_{z_1} = 3a, \sigma_{z_2} = 3b$

  + $Q$: process model covariance --> small enough to allow the filter to work in all situations 

## Performance
Correctly tuned and consistent filter, the performance can be judged based on:
* Overall estimation error
* Size of the state covariances 
  + Smaller covariances ==> better position estimates

## 2-d tracker demo 