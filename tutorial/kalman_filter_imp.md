# Kalman filter implementation issues

## Numerical accuracy
* Joseph stabilized version is less prone to numerical inaccurcy 

## Divergence issues
* Increase arithmetic precision
* Use a form of square root Kalman filter
* Symmatrize the covariance matrix at each time step 
* Don't initialize P with large numbers
* Use a form of fading-memory filter