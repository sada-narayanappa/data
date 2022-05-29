# Components of Time Series
<br/>
#### Seasonality

*Seasonality* cyclical variations in time series data as shown in the figure below. 
Some examples are sales during Christmas or ice-cream sales during summer etc.

**To do ** : How to detect seasonality? Investigate The power spectrum (or periodogram) plots the power versus frequency. 

---
*Trend* refers to the magnitude of the signal. 

**Seasonality and Trend**
<img src="/static/media/articles/ts-season.jpg" alt="drawing" style="width:350px;"/>

---
*Cyclical* a pattern seems to 

---
*Auto Correlated*: is the presence of correlation with its past values.

An autocorrelation function measures the degree of similarity of the present series with that of its lagged series (past values). The ACF graph for the AQI index shows spike above the blue region, which is an indication that the series is autocorrelated. Similarly, you can check autocorrelation for other series of the dataset also.

<img src='https://miro.medium.com/max/798/1*FeL_VxFWGE9V11HNjDC9ag.png' />

---
*Stationary* series in which mean, standard deviation and autocorrelation remains same.
To check the stationarity one can use Johansen cointegration test and inspect the returned eigenvalues. If the eigenvalues are less than one, than the series is said to be stationary.


 


