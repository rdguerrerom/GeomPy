# Dynamical Systems
## Prerequisites before continuing
Before reading ahead, you should have a firm grasp on derivatives, integrals, and fairly basic differential equations

## Theory

### 1 Dimensional Dynamical Systems
We will be talking about 1D __continuous__ dynamical systems. These describe the dynamics on the real line, and the dynamics can be described by the orinary differential equation (ODE):
<p align="center">
  <img src="https://latex.codecogs.com/gif.latex?\dot{x}&space;=&space;f(x)" title="\dot{x} = f(x)" />
</p>
There are two main ways that we will approach our study of the dynamics of the 1D systems:

1. We can solve the equation analytically by solving an ODE

2. We can approach the evaluation of the system qualitatively

#### 1. Analytic Approach
This approach is fairly simple when it works out nicely, and if it does not, can be extremely difficult. Our system can be written as:
<p align="center">
  <img src="https://latex.codecogs.com/gif.latex?\frac{dx}{dt}&space;=&space;f(x)" title="\frac{dx}{dt} = f(x)" />
</p>
And then using the technique of seperation of variables, we can theoretically solve the system by:
<p align="center">
  <img src="https://latex.codecogs.com/gif.latex?\int&space;\frac{dx}{f(x)}&space;=&space;\int&space;dt&space;=&space;t&plus;C" title="\int \frac{dx}{f(x)} = \int dt = t+C" />
</p>
This method does require some integration but can give a lot of information if we are able to solve it explicitly. We won't focus too much on this analytic approach, we will spend most of our time focusing on the qualitative approach.

#### 2. Qualitative Approach
To analyze the system qualitatively, there are two general steps:

1. Find fixed points of the system, where fixed points are defined by:
<p align="center">
  <img src="https://latex.codecogs.com/gif.latex?x^*&space;\Rightarrow&space;f(x^*)&space;=&space;0" title="x^* \Rightarrow f(x^*) = 0" />
</p>

2. Find the sign of the system in between the fixed points (will elaborate below)

Once we have our fixed points, we want to figure out where the system is negative and where the system is positive, that will determine the __stability__ of the fixed point. So, remember that our dynamical system is described by:
<p align="center">
  <img src="https://latex.codecogs.com/gif.latex?\dot{x}&space;=&space;f(x)" title="\dot{x} = f(x)" />
</p>
There are three different types of stability:

1. __Stable__ : We have a stable fixed point if: 
<p align="center">
<img src="https://latex.codecogs.com/gif.latex?f(x^*&space;-&space;\epsilon&space;)&space;>&space;0" title="f(x^* - \epsilon ) > 0" />
and
<img src="https://latex.codecogs.com/gif.latex?f(x^*&space;&plus;&space;\epsilon&space;)&space;<&space;0" title="f(x^* + \epsilon ) < 0" />
</p>

2. __Unstable__ : We have an unstable fixed point if:
<p align="center">
<img src="https://latex.codecogs.com/gif.latex?f(x^*&space;-&space;\epsilon&space;)&space;<&space;0" title="f(x^* - \epsilon ) < 0" />
and
<img src="https://latex.codecogs.com/gif.latex?f(x^*&space;&plus;&space;\epsilon&space;)&space;>&space;0" title="f(x^* + \epsilon ) > 0" /> 
</p>

3. __Semi-Stable__ : We have a semi-stable fixed point if:
<p align="center">
<img src="https://latex.codecogs.com/gif.latex?f(x^*&space;-&space;\epsilon&space;)&space;<&space;0" title="f(x^* - \epsilon ) < 0" />
and
<img src="https://latex.codecogs.com/gif.latex?f(x^*&space;&plus;&space;\epsilon&space;)&space;<&space;0" title="f(x^* + \epsilon ) < 0"  /> 
</p>
<p align="center"> or </p>
<p align="center">
<img src="https://latex.codecogs.com/gif.latex?f(x^*&space;-&space;\epsilon&space;)&space;>&space;0" title="f(x^* - \epsilon ) > 0" />
and
<img src="https://latex.codecogs.com/gif.latex?f(x^*&space;&plus;&space;\epsilon&space;)&space;>&space;0" title="f(x^* + \epsilon ) > 0" /> 
</p>

There is another way to evaluate stability, and that is by a __second derivative test__. Once you find fixed points, this test can tell you (most of the time) whether the fixed point is stable or unstable:

- __Stable__ : Stable fixed point if:
<p align="center">
  <img src="https://latex.codecogs.com/gif.latex?{f}'(x^*)&space;<&space;0" title="{f}'(x^*) < 0" />
</p>

- __Unstable__ : Unstable fixed point if:
<p align="center">
  <img src="https://latex.codecogs.com/gif.latex?{f}'(x^*)&space;>&space;0" title="{f}'(x^*) > 0" />
</p>

- __Not Sure__ : Here, we must evaluate stability using the qualitative approach described above. We cannot tell what type of fixed point we have if:
<p align="center">
  <img src="https://latex.codecogs.com/gif.latex?{f}'(x^*)&space;=&space;0" title="{f}'(x^*) = 0" />
</p>
