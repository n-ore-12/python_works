# Linear Fit Algorithm

This algorithm estimates the line of best fit by finding the slope and intercept between points in a noisy dataset in steps of one, two, three, and n points.

1. The basic model is

``
y = ax + b + e
``

where:

- ``a`` is the true slope
- ``b`` is the true intercept
- ``e`` is normally distributed random noise

The true values of ``a`` and ``b`` are 2 and -2, respectively. 

The function `linegen(x,a,b)` generates values according to the linear equation above. 

Noise is introduced through
```python
e = rng.normal(loc=0, scale=1, size=len(x))
```
where the mean is 0 and standard deviation is 1.


----------


1. The general function `multipoint_parameter_n` estimates the slope and intercept as described above by finding the slope between points in steps of 1, 2, 3 and so on, meaning points separated by 1, 2, 3, and n indeces. It then averages the results and returns an estimate of the slope. 

2. If the final point does not fit within the sequence, the algorithm uses the last used point and the last point in the set,  in order not to discard data. 


## Aim of this experiment

This algorithm is designed with the purpose of finding the most accurate means of linear fitting. 

## Improvements & Suggestions

Currently, the algorithm utilizes only one "batch" of random data. In order to determine how n effects accuracy, independently generated data per each trial would be statistically better. 

Also, the greater the distance between two lines, the more accurate the slope will be to its true value:

- Each slope uses a larger ``x``-interval
- Random fluctuations affect individual ``y`` values much less

However:

- Fewer slope estimates are able to be taken
- Less of the data contributes to the overall estimate

This means that increasing the step size does not necessarily increase accuracy. 

However, I'd like to implement this quantitatively instead of qualitatively, and make it so that this percentage error is calculated. 

Finally, other improvements include:

- Investigating how the noise level affects accuracy per step size
- Investigating how the number of data points affects accuracy per step size




