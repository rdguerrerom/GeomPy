# Curves

## Prerequisites before continuing
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
 
Finding the length of our curve, deonted by <img src="http://latex.codecogs.com/gif.latex?\left&space;\|&space;\overrightarrow{\alpha}'(t)&space;\right&space;\|" title="\left \| \overrightarrow{\alpha}'(t) \right \|" /> , follows directly from the dot product:
 <p align="center">
 <img src="http://latex.codecogs.com/gif.latex?{\left&space;\|&space;\overrightarrow{\alpha}(t)\right\|}&space;=&space;\sqrt{\overrightarrow{\alpha}(t)&space;\cdot&space;\overrightarrow{\alpha}(t)}" title="{\left \| \overrightarrow{\alpha}(t)\right\|} = \sqrt{\overrightarrow{\alpha}(t) \cdot \overrightarrow{\alpha}(t)}" />
</p>

Given two curves, we want to be able to find the angle between them. This is especially useful if we find out that the curves form a constant angle at all points. So, given two curves, <img src="http://latex.codecogs.com/gif.latex?\inline&space;\overrightarrow{\alpha}(t)" title="\overrightarrow{\alpha}(t)" /> and <img src="http://latex.codecogs.com/gif.latex?\inline&space;\overrightarrow{\gamma}(t)" title="\overrightarrow{\gamma}(t)" />, we have:
<p align="center">
	<img src="http://latex.codecogs.com/png.latex?cos(\theta)=\frac{\overrightarrow{\alpha}\cdot&space;\overrightarrow{\gamma}}{\left&space;\|&space;\overrightarrow{\alpha}\right&space;\|&space;\left&space;\|&space;\overrightarrow{\gamma}\right&space;\|}" title="cos(\theta)=\frac{\overrightarrow{\alpha}\cdot \overrightarrow{\gamma}}{\left \| \overrightarrow{\alpha}\right \| \left \| \overrightarrow{\gamma}\right \|}" />
</p>


The last tool we want to setup is the arc length function, denoted by <img src="http://latex.codecogs.com/gif.latex?\inline&space;s(t)" title="s(t)" /> :
<p align="center">
	<img src="http://latex.codecogs.com/gif.latex?s(t)=\int_a^b&space;\left&space;\|&space;\overrightarrow&space;\alpha'(s)\right\|dt" title="s(t)=\int_a^b \left \| \overrightarrow \alpha'(s)\right\|dt" />
</p>
Applications of the arc length function will be seen in our upcoming discussion of unit speed curves.

### 3-Dimensional Curves

Let us restrict our discussion down to the 3-dimensional case and see what information we can pull from this.

#### Unit Speed Curves

We will start the three dimensional discussion with a special case, the unit speed curve case.

A Unit Speed Curve, denoted by <a href="http://www.codecogs.com/eqnedit.php?latex=\inline&space;\overrightarrow{\alpha}(s)" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\inline&space;\overrightarrow{\alpha}(s)" title="\overrightarrow{\alpha}(s)" /></a> , is one in which:
<p align="center">
<img src="http://latex.codecogs.com/gif.latex?\left&space;\|&space;\overrightarrow{\alpha}'(t)&space;\right&space;\|&space;=&space;1" title="\left \| \overrightarrow{\alpha}'(t) \right \| = 1" />
</p>

Note: This is the same as saying:
<p align="center">
<img src="http://latex.codecogs.com/gif.latex?\int_0^t&space;\left&space;\|&space;\overrightarrow&space;\alpha'(s)\right\|ds&space;=&space;t" title="\int_0^t \left \| \overrightarrow \alpha'(s)\right\|ds = t" />
</p>

We want to pull as much information out of our unit speed curves as possible. So, how about we construct a "moving frame" at each point along the curve, this is called the Frenet Frame. Here is a visual to show what we are after:

<p align="center"><a href="https://commons.wikimedia.org/wiki/File:Frenet-Serret-frame_along_Vivani-curve.gif#/media/File:Frenet-Serret-frame_along_Vivani-curve.gif"><img src="https://upload.wikimedia.org/wikipedia/commons/1/14/Frenet-Serret-frame_along_Vivani-curve.gif" alt="Frenet-Serret-frame along Vivani-curve.gif"></a><br>By <a href="https://en.wikipedia.org/wiki/User:Gonfer" class="extiw" title="en:User:Gonfer">Gonfer</a> (<a href="https://en.wikipedia.org/wiki/User_talk:Gonfer" class="extiw" title="en:User talk:Gonfer">talk</a>), <a href="https://creativecommons.org/licenses/by-sa/3.0" title="Creative Commons Attribution-Share Alike 3.0">CC BY-SA 3.0</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=18558097">Link</a></p>

First of all, the Frenet Frame is constructed by three vectors denoted by <img src="http://latex.codecogs.com/gif.latex?\overrightarrow{T}(s)&space;,&space;\overrightarrow{N}(s)&space;,&space;\overrightarrow{B}(s)" title="\overrightarrow{T}(s) , \overrightarrow{N}(s) , \overrightarrow{B}(s)" />. For all parts let's assume that our curve, <img src="http://latex.codecogs.com/gif.latex?\overrightarrow{\alpha}(s)" title="\overrightarrow{\alpha}(s)" /> , is a unit speed curve. Also we develop our definitions of these, be sure to check the following:
* Each vector is perpendicular to the other two
* Each vector is of unit speed

So let's begin finding the components.

The first component is the Tangent vector, denoted by <img src="http://latex.codecogs.com/gif.latex?\overrightarrow{T}(s)" title="\overrightarrow{T}(s)" /> :
<p align="center">
<a href="http://www.codecogs.com/eqnedit.php?latex=\overrightarrow{T}(s)=&space;\overrightarrow&space;\alpha'(s)\right\|" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\overrightarrow{T}(s)=&space;\overrightarrow&space;\alpha'(s)\right\|" title="\overrightarrow{T}(s)= \overrightarrow \alpha'(s)\right\|" /></a>
</p>

Before continuing, we need to give another definition. A regular curve is one in which:
<p align="center">
<img src="http://latex.codecogs.com/gif.latex?\left&space;\|&space;\overrightarrow{T'}(s)\right&space;\|&space;\neq&space;0" title="\left \| \overrightarrow{T'}(s)\right \| \neq 0" />
</p>

at any point on the curve. We will see why this is a necessary restriction, as we cannot divide by 0.


The next component is the Normal vector, denoted by <img src="http://latex.codecogs.com/gif.latex?\overrightarrow{N}(s)" title="\overrightarrow{N}(s)" /> :

<p align="center">
<img src="http://latex.codecogs.com/gif.latex?\overrightarrow{N}(s)=\frac{\overrightarrow{T}'(s)}{\left&space;\|&space;\overrightarrow{T}'(s)\right\|}" title="\overrightarrow{N}(s)=\frac{\overrightarrow{T}'(s)}{\left \| \overrightarrow{T}'(s)\right\|}" />
</p>

The final component, the Binormal vector, denoted by <img src="http://latex.codecogs.com/gif.latex?\overrightarrow{B}(s)" title="\overrightarrow{B}(s)" /> , is found by taking the cross product of the first two components: 
<p align="center">
<a href="http://www.codecogs.com/eqnedit.php?latex=\overrightarrow{B}(s)=&space;\overrightarrow&space;T(s)\right\|&space;\times&space;\overrightarrow&space;N(s)\right\|" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\overrightarrow{B}(s)=&space;\overrightarrow&space;T(s)\right\|&space;\times&space;\overrightarrow&space;N(s)\right\|" title="\overrightarrow{B}(s)= \overrightarrow T(s)\right\| \times \overrightarrow N(s)\right\|" /></a>
</p>

Let us now look at the curvature of our curve, denoted by <img src="http://latex.codecogs.com/gif.latex?\kappa(s)" title="\kappa(s)" /> : 
<p align="center">
<img src="http://latex.codecogs.com/gif.latex?\kappa(s)=&space;\left&space;\|&space;\overrightarrow&space;T'(s)\right\|" title="\kappa(s)= \left \| \overrightarrow T'(s)\right\|" />
</p>

Lastly, the torsion of our curve denoted by <img src="http://latex.codecogs.com/gif.latex?\tau(s)" title="\tau(s)" /> is found by:
<p align="center">
<img src="http://latex.codecogs.com/gif.latex?\tau(s)=&space;\overrightarrow&space;B'(s)\right\|&space;\cdot&space;\overrightarrow&space;N(s)\right\|" title="\tau(s)= \overrightarrow B'(s)\right\| \cdot \overrightarrow N(s)\right\|" />
</p>

Putting all of these definitons together, we can obtain a few cool properties about the derivatives of each component of our Frenet Frame. I will list them here without justification, these can be checked with the tools we have already developed. So, here they are:
<p align="center">
<img src="http://latex.codecogs.com/gif.latex?\overrightarrow{T}'(s)&space;=&space;\kappa(s)\overrightarrow{N}(s)" title="\overrightarrow{T}'(s) = \kappa(s)\overrightarrow{N}(s)" />
</p>
<p align="center">
<img src="http://latex.codecogs.com/gif.latex?\overrightarrow{N}'(s)&space;=&space;-\kappa(s)\overrightarrow{T}(s)&space;-&space;\tau(s)\overrightarrow{B}(s)" title="\overrightarrow{N}'(s) = -\kappa(s)\overrightarrow{T}(s) - \tau(s)\overrightarrow{B}(s)" />
</p>
<p align="center">
<img src="http://latex.codecogs.com/gif.latex?\overrightarrow{B}'(s)&space;=&space;\tau(s)\overrightarrow{N}(s)" title="\overrightarrow{B}'(s) = \tau(s)\overrightarrow{N}(s)" />
</p>

#### Not Necessarily Unit Speed Curves

The unit speed case is a very special one. But, "out in the wild", there is a low chance that a given 3 dimensional curve is in fact a unit speeed curve. So, we need more generalized equations in order to find the Frenet Frame, curvature and torsion.

So, let's let our regular curve be denoted by <img src="http://latex.codecogs.com/gif.latex?\inline&space;\overrightarrow{\alpha}(t)" title="\overrightarrow{\alpha}(t)" /> and let's have it not necesarily be a unit speed curve.

The Tangent Vector, denoted by <img src="http://latex.codecogs.com/gif.latex?\inline&space;\overrightarrow{T}(t)" title="\overrightarrow{T}(t)" /> , is calculated by:
<p align="center">
<img src="http://latex.codecogs.com/gif.latex?\overrightarrow{T}(t)=\frac{\overrightarrow{\alpha}'(t)}{\left&space;\|&space;\overrightarrow{\alpha}'(t)&space;\right&space;\|}" title="\overrightarrow{T}(t)=\frac{\overrightarrow{\alpha}'(t)}{\left \| \overrightarrow{\alpha}'(t) \right \|}" />
</p>

The Binormal Vector, denoted by <img src="http://latex.codecogs.com/gif.latex?\inline&space;\overrightarrow{B}(t)" title="\overrightarrow{B}(t)" /> , is calculated by:
<p align="center">
<img src="http://latex.codecogs.com/gif.latex?\overrightarrow{B}(t)&space;=&space;\frac{\overrightarrow{\alpha}'(t)&space;\times&space;\overrightarrow{\alpha}''(t)}{\left&space;\|&space;\overrightarrow{\alpha}'(t)&space;\times&space;\overrightarrow{\alpha}''(t)&space;\right&space;\|}" title="\overrightarrow{B}(t) = \frac{\overrightarrow{\alpha}'(t) \times \overrightarrow{\alpha}''(t)}{\left \| \overrightarrow{\alpha}'(t) \times \overrightarrow{\alpha}''(t) \right \|}" />
</p>

The Normal Vector, denoted by <img src="http://latex.codecogs.com/gif.latex?\inline&space;\overrightarrow{N}(t)" title="\overrightarrow{N}(t)" /> , is calculated by:
<p align="center">
<img src="http://latex.codecogs.com/gif.latex?\overrightarrow{N}(t)&space;=&space;\overrightarrow{B}(t)&space;\times&space;\overrightarrow{T}(t)" title="\overrightarrow{N}(t) = \overrightarrow{B}(t) \times \overrightarrow{T}(t)" />
</p>

The Curvature of our curve, denoted by <img src="http://latex.codecogs.com/gif.latex?\inline&space;\kappa(t)" title="\kappa(t)" /> , is calculated by:
<p align="center">
<img src="http://latex.codecogs.com/gif.latex?\kappa(t)&space;=&space;\frac{\left&space;\|&space;\overrightarrow{\alpha}'(t)&space;\times&space;\overrightarrow{\alpha}''(t)&space;\right&space;\|}{\left&space;\|&space;\overrightarrow{\alpha}'(t)&space;\right&space;\|^3}" title="\kappa(t) = \frac{\left \| \overrightarrow{\alpha}'(t) \times \overrightarrow{\alpha}''(t) \right \|}{\left \| \overrightarrow{\alpha}'(t) \right \|^3}" />
</p>

And lastly, the Torsion of our curve, denoted by <img src="http://latex.codecogs.com/gif.latex?\inline&space;\tau(t)" title="\tau(t)" /> , is calculated by:
<p align="center">
<img src="http://latex.codecogs.com/gif.latex?\tau(t)&space;=&space;\frac{-(\overrightarrow{\alpha}'(t)&space;\times&space;\overrightarrow{\alpha}''(t))&space;\cdot&space;\overrightarrow{\alpha}'''(t)}{\left&space;\|&space;\overrightarrow{\alpha}'(t)&space;\times&space;\overrightarrow{\alpha}''(t)\right&space;\|^2}" title="\tau(t) = \frac{-(\overrightarrow{\alpha}'(t) \times \overrightarrow{\alpha}''(t)) \cdot \overrightarrow{\alpha}'''(t)}{\left \| \overrightarrow{\alpha}'(t) \times \overrightarrow{\alpha}''(t)\right \|^2}" /></p>

These definitions more or less follow directly. I suggest, if interested, taking some time and doing out the calculations for each part. I shall provide a little bit of input to start the proofs. If we let <img src="http://latex.codecogs.com/gif.latex?\inline&space;\overrightarrow{\alpha}(t)" title="\overrightarrow{\alpha}(t)" /> be a regular curve. Let us have:
<p align="center">
<img src="http://latex.codecogs.com/gif.latex?\frac{ds}{dt}&space;=&space;\left&space;\|&space;\overrightarrow{\alpha}'(t)&space;\right&space;\|&space;=&space;v" title="\frac{ds}{dt} = \left \| \overrightarrow{\alpha}'(t) \right \| = v" />
</p>

Note: If doing out the proofs of the definitions above, be sure to pay close attention when differentiating (ie. be sure to use the chain rule and substitute in our unit speed definitions when you can). After that, the definitions should simply follow.
