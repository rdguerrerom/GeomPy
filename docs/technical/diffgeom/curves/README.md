# Curves
This is a technical overview of the Curve class
## Dependencies
Curves requires NumPy and SymPy, so be sure to have those prepared and ready to go.
Once you have that done, you must then import the Curve class:
```python
>>> from curve import Curve
```
When using special functions like `sin` or `cos`, SymPy has a nice implementation of these, so be sure to import them:
```python
>>> from sympy import sin, cos
```

## Creating a Curve
To create an n-dimensional curve, you will need to pass in a parameterized function, as well as the dependent variable:
```python
>>> alpha = Curve((x + 1, x - 2, x**3, sin(x)), x)
>>> alpha
Curve((x + 1, x - 2, x**3, sin(x)), x)
```

## Properties of a Curve
The Curve has three properties which are functions, parameter, dimension:
```python
>>> alpha = Curve((x + 1, x - 2, x**3, sin(x)), x)
>>> alpha.functions
(x + 1, x - 2, x**3, sin(x))
>>> alpha.parameter
x
>>> alpha.dimension
4
```

## General Curve Functions
| Function        | Input(s)           | Description
| ------------- |-------------| -----
| `length(self)`      | self : Curve | The length of the curve 
| `angle(v1, v2)`      | v1, v2 : Curves      |   The cos(angle) created between two curves 
| `isPerpendicular(self, C)` | self, C : Curves      |  If two curves are perpendicular 
| `cross(self, C)` | self, C : Curves      |   The cross product of two curves 
| `isUnitLength(self)` | self: Curve | If the curve is of unit length
| `solveCurve(self, value)` | self : Curve, value : int or float |  The result when substituting the value into the curve's parameter
| `sameUnderRigid(self, beta)` | self, beta: Curves | If two unit speed curves are equivalent under a rigid motion
#### length
```python
>>> alpha = Curve((x + 1, x - 2, x**3, sin(x)), x)
>>> alpha.length()
sqrt(x**6 + 2*x**2 - 2*x + sin(x)**2 + 5)
```
#### angle
```python
## cos(theta) = angle(alpha,beta)
>>> alpha = Curve((-sin(x), cos(x), 1), x)
>>> beta = Curve((0, 0, 1), x)
>>> alpha.angle(beta)
sqrt(2)/2
```
#### isPerpendicular
```python
>>> from curve import Curve
>>> alpha = Curve((0, 0, 1), x)
>>> beta = Curve((0, 1, 0), x)
>>> alpha.isPerpendicular(beta)
True
```
#### cross
```python
>>> alpha = Curve((-sin(x), cos(x), 1), x)
>>> beta = Curve((0, 0, 1), x)
>>> alpha.cross(beta)
Curve((cos(x), sin(x), 0), x)
```
#### isUnitLength
```python
>>> alpha = Curve((-sin(x), cos(x), 0), x)
>>> alpha.isUnitLength()
True
```
#### solveCurve
```python
>>> alpha = Curve((sin(x), cos(x), 0), x)
>>> alpha.solveCurve(5)
[sin(5), cos(5), 0]
```
#### sameUnderRigid
```python
>>> alpha = Curve((sin(x), cos(x), 0), x)
>>> beta = Curve((cos(x), sin(x), 0), x)
 >>> alpha.sameUnderRigid(beta)
True
```

## Frenet Frame Functions
| Function        | Input(s)          | Unit Speed Required | Description
| ------------- | ------------- |:------: | -----
| `uTangent(self)`      | self : Curve | True | The Unit Speed Frenet Frame Tangent Vector (T) 
| `uNormal(self)`      | self : Curve  |  True  |   The Unit Speed Frenet Frame Tangent Vector (N) 
| `uBinormal(self)` | self : Curve   |  True |  The Unit Speed Frenet Frame Binormal Vector (B) 
| `uTorsion(self)` | self : Curve   |  True |   The Torsion of the unit speed curve (tau) 
| `uCurvature(self)` | self : Curve | True | The Curvature of the unit speed curve (kappa)
| `Tangent(self)`      | self : Curve | False | The Frenet Frame Tangent Vector (T) 
| `Normal(self)`      | self : Curve  |  False  |   The Frenet Frame Normal Vector (N) 
| `Binormal(self)` | self : Curve   |  False |  The Frenet Frame Binormal Vector (B) 
| `Torsion(self)` | self : Curve   |  False |   The Torsion of the curve (tau) 
| `Curvature(self)` | self : Curve | False | The Curvature of the curve (kappa)
| `frenetFrame(self)` | self. Curve | False | The Frenet Frame of a parameterized 3-dimensional curve

Note: You can always use the non unit speed functions, even if the imput curve is unit speed
#### Unit Speed Function Examples
##### uTangent
```python
>>> alpha = Curve((sin(x), cos(x), 0), x)
>>> alpha.uTangent()
Curve((cos(x), -sin(x), 0), x)
```
##### uNormal
```python
>>> alpha = Curve((sin(x), cos(x), 0), x)
>>> alpha.uNormal()
Curve((-sin(x), -cos(x), 0), x)
```
##### uBinormal
```python
>>> alpha = Curve((sin(x), cos(x), 0), x)
>>> alpha.uBinormal()
Curve((0, 0, -1), x)
```
##### uTorsion
```python
>>> alpha = Curve((sin(x), cos(x), 0), x)
>>> alpha.uTorsion()
0
```
##### uCurvature
```python
>>> alpha = Curve((sin(x), cos(x), 0), x)
>>> alpha.uCurvature()
1
```
#### Non Unit Speed Function Examples
##### Tangent
```python
>>> alpha = Curve((sin(x), cos(x), 0), x)
>>> alpha.Tangent()
Curve((cos(x), -sin(x), 0), x)
```
##### Normal
```python
>>> alpha = Curve((sin(x), cos(x), 0), x)
>>> alpha.Normal()
Curve((-sin(x), -cos(x), 0), x)
```
##### Binormal
```python
>>> alpha = Curve((sin(x), cos(x), 0), x)
>>> alpha.Binormal()
Curve((0, 0, -1), x)
```
##### Torsion
```python
>>> alpha = Curve((sin(x), cos(x), 0), x)
>>> alpha.Torsion()
0
```
##### Curvature
```python
>>> alpha = Curve((sin(x), cos(x), 0), x)
>>> alpha.Curvature()
1
```
##### frenetFrame
```python
>>> alpha = Curve((sin(x), cos(x), 0), x)
>>> alpha.frenetFrame()
{'Tangent': Curve((cos(x), -sin(x), 0), x), 
'Binormal': Curve((0, 0, -1), x), 
'Normal': Curve((-sin(x), -cos(x), 0), x)}
```
