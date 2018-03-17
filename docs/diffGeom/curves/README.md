# Curves

## Prerequisites before continuting
Before reading ahead, you should have a firm grasp on basic calculus (derivatives and integrals) as well as a good handle on the dot product and cross product.

## Theory

### General N-Dimensional Curves
We will be working with parameterized curves. That is, if we have an n-dimensional curve, denoted by <a href="http://www.codecogs.com/eqnedit.php?latex=\inline&space;\overrightarrow{\alpha}(t)" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\inline&space;\overrightarrow{\alpha}(t)" title="\overrightarrow{\alpha}(t)" /></a>, then we shall define our curve by: 
<p align="center">
<img src="http://latex.codecogs.com/gif.latex?\overrightarrow{\alpha}(t)&space;=&space;(\alpha_1(t),&space;\alpha_2\(t),\alpha_3(t),&space;\cdots&space;,\alpha_n(t))" title="\overrightarrow{\alpha}(t) = (\alpha_1(t), \alpha_2\(t),\alpha_3(t), \dots,\alpha_n(t))" />
</p>

where <img src="http://latex.codecogs.com/gif.latex?\inline&space;{\alpha_1}(t),{\alpha_2}(t),{\alpha_3}(t),\dots,\alpha_n(t)" title="{\alpha_1}(t),{\alpha_2}(t),{\alpha_3}(t),\dots,\alpha_n(t)" />  are continuous, differentiable functions in <img src="http://latex.codecogs.com/gif.latex?\inline&space;\mathbb{R}^n" title="\mathbb{R}^n" />.

The next thing we may want to do is find the derivative of our curve at each point. To do that, we shall simply differentiate each part of our parameterization:
<p align="center">
<img src="http://latex.codecogs.com/gif.latex?\overrightarrow{\alpha}'(t)&space;=&space;(\alpha_1'(t),&space;\alpha_2'(t),\alpha_3'(t),&space;\dots&space;,\alpha_n'(t))" title="\overrightarrow{\alpha}'(t) = (\alpha_1'(t), \alpha_2'(t),\alpha_3'(t), \dots,\alpha_n'(t) )" />
 </p>
 
Finding the length of our curve, deonted <img src="http://latex.codecogs.com/gif.latex?\inline&space;\left&space;\|&space;\overrightarrow{\alpha}(t))&space;\right&space;\|" title="\left \| \overrightarrow{\alpha}(t)) \right \|" /> ,follows directly from the dot product:
 <p align="center">
 <img src="http://latex.codecogs.com/gif.latex?{\left&space;\|&space;\overrightarrow{\alpha}(t)\right\|}&space;=&space;\sqrt{\overrightarrow{\alpha}(t)&space;\cdot&space;\overrightarrow{\alpha}(t)}" title="{\left \| \overrightarrow{\alpha}(t)\right\|} = \sqrt{\overrightarrow{\alpha}(t) \cdot \overrightarrow{\alpha}(t)}" />
</p>

Given two curves, we want to be able to find the angle between them, this is especially useful if we find out we form a constant angle between these curves at all points. So, given two curves, <img src="http://latex.codecogs.com/gif.latex?\inline&space;\overrightarrow{\alpha}(t)" title="\overrightarrow{\alpha}(t)" /> and <img src="http://latex.codecogs.com/gif.latex?\inline&space;\overrightarrow{\gamma}(t)" title="\overrightarrow{\gamma}(t)" />, we have:
<p align="center">
	<img src="http://latex.codecogs.com/png.latex?cos(\theta)=\frac{\overrightarrow{\alpha}\cdot&space;\overrightarrow{\gamma}}{\left&space;\|&space;\overrightarrow{\alpha}\right&space;\|&space;\left&space;\|&space;\overrightarrow{\gamma}\right&space;\|}" title="cos(\theta)=\frac{\overrightarrow{\alpha}\cdot \overrightarrow{\gamma}}{\left \| \overrightarrow{\alpha}\right \| \left \| \overrightarrow{\gamma}\right \|}" />
</p>


The last tool we want to setup is the arc length function, denoted <img src="http://latex.codecogs.com/gif.latex?\inline&space;s(t)" title="s(t)" /> :
<p align="center">
	<img src="http://latex.codecogs.com/gif.latex?s(t)=\int_a^b&space;\left&space;\|&space;\overrightarrow&space;\alpha'(s)\right\|dt" title="s(t)=\int_a^b \left \| \overrightarrow \alpha'(s)\right\|dt" />
</p>
Applications of this will be seen in our upcoming discussion of unit speed curves.

<img src="http://latex.codecogs.com/gif.latex?\inline&space;{\left&space;\|&space;\overrightarrow{\alpha}'(t)\right\|}&space;=&space;1" title="{\left \| \overrightarrow{\alpha}'(t)\right\|} = 1" />

<img src="http://latex.codecogs.com/gif.latex?\int_0^t&space;\left&space;\|&space;\overrightarrow&space;\alpha'(s)\right\|dt&space;=&space;t" title="\int_0^t \left \| \overrightarrow \alpha'(s)\right\|dt = t" />

### 3-Dimensional Curves

#### Unit Speed Curves

<p align="center">
<img src="http://latex.codecogs.com/gif.latex?\overrightarrow{N}(s)=\frac{\overrightarrow{T}'(s)}{\left&space;\|&space;\overrightarrow{T}'(s)\right\|}" title="\overrightarrow{N}(s)=\frac{\overrightarrow{T}'(s)}{\left \| \overrightarrow{T}'(s)\right\|}" />
</p>

<a href="http://www.codecogs.com/eqnedit.php?latex=\overrightarrow{T}(s)=&space;\overrightarrow&space;\alpha'(s)\right\|" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\overrightarrow{T}(s)=&space;\overrightarrow&space;\alpha'(s)\right\|" title="\overrightarrow{T}(s)= \overrightarrow \alpha'(s)\right\|" /></a>

<a href="http://www.codecogs.com/eqnedit.php?latex=\overrightarrow{B}(s)=&space;\overrightarrow&space;T(s)\right\|&space;\times&space;\overrightarrow&space;N(s)\right\|" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\overrightarrow{B}(s)=&space;\overrightarrow&space;T(s)\right\|&space;\times&space;\overrightarrow&space;N(s)\right\|" title="\overrightarrow{B}(s)= \overrightarrow T(s)\right\| \times \overrightarrow N(s)\right\|" /></a>

<img src="http://latex.codecogs.com/gif.latex?\kappa(s)=&space;\left&space;\|&space;\overrightarrow&space;T'(s)\right\|" title="\kappa(s)= \left \| \overrightarrow T'(s)\right\|" />

<img src="http://latex.codecogs.com/gif.latex?\tau(s)=&space;\overrightarrow&space;B'(s)\right\|&space;\cdot&space;\overrightarrow&space;N(s)\right\|" title="\tau(s)= \overrightarrow B'(s)\right\| \cdot \overrightarrow N(s)\right\|" />
