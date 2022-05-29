# Time Series Analysis
<br/>

## What is time series data
A time series data is a sequential set of data points, measured over successive time period (usually on equal intervals).  For example if we take measurements of heart rate, blood pressure (BP), sugar level every 5 minutes from an individual, it can be represented as time series data as shown below 
<pre>
<table border=1>
<tr><th>time</th><th> heart_rate </th><th>blood_pressure</th><th>blood_sugar_level</th></tr>
 <tr><td> 01/01/2011 10:00:00  </td><td> 76 </td><td> 119/76 </td><td> HIGH </td></tr>
 <tr><td> 01/01/2011 10:05:00 </td><td> 77 </td><td> 119/76 </td><td> HIGH</td></tr>
 <tr><td> 01/01/2011 10:10:00 </td><td> 76 </td><td> 129/77 </td><td> LOW </td></tr>
</table>
</pre> 

we refer to variables heart_rate, blood_pressure, etc. as measurerands or sensors (sensor readings/measurements). 

A time series Data shown above it multivariate. if we consider only a single column (such as heart_rate) then we call it as univariate. 

A time series may consist of readings that can be continuous or categorical. A *continuous* means, it takes on any value from real $\mathbb{R}$  
some measurands may take on values from a fixed set of possible values - for ex: binary {0,1} that represents a status or state - we refer those measurands as *categorical*  

From the example above, *heart rate* and *blood_pressure* can be viewed as continuos and blood sugar level is categorical; in the example it takes values from {HIGH, LOW}
Usually time series dataset, the consecutive observations are recorded at equally spaced time intervals such as hourly, daily, weekly, monthly or yearly time
separations. 


A time series data analysis is to discover the insights. The time series data can be analysed using descriptive statistics; several inferences can be made on it. 

## Examples of Time series Data

Time series appears more frequently than any other dataset and forms a very critical type of data analysis applicable to a large domains.

Some examples include:

>* Stock Market data 
* Daily airline passengers (many variations of these)
* Monitoring data from survillance 
* Satellite telemetry data
* etc.


There are many insights can be found using the time series data. Few examples are:

>* Understand the descriptive statistics such as firt and second order statistical moments such as mean, mode, variance etc.
* If a sensor exhibit trend, seasonaility, cyclical nature ( will be explained later)
* If a sensor is stationary or show variability (explained later)
* continuous or categorical
* duratin when it is valid 
* if a pair of sensors are mutually related
* if sensors represent action or status
* Describe the logical model (or the underlying dynamic nature of the system)

Several inferential statistics may consists of:

>* if sensor hs interaction with other sensor and predict the strength of the interaction
* apply predictions to predict one or more ahead 
* detect anomaly
* Detect Novelty
* Detect fault
* predictive maintenance 
* Predict fault/failure 
* Detect usage and forecast reamining life


Time series sensors can be described by its intended function, modalities, duration when it is active, valid range of operational values etc.



## Algorithms

There are many algorthms that exists to analyze time series data; we will go through each in its own right in this book

The most popular are:

>* Autoregressive Integrated Moving Average (ARIMA). 
* ARIMAX 
* ARX 
* System Invariant Analysis Technoology (SIAT) based on ARX
* Seasonal ARIMA (SARIMA) 
* Deep Neural Network based models:
>> LSM, CNN, Autoencoders, Feed Forward Networks (FNN), Time Lagged Neural Network (TLNN)
* Hidden Markov Models
* Markov Chains
* Non linear ArCH models
* SVM 


