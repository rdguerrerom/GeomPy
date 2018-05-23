# Dynamical Systems
This is a technical overview of the DynamicalSystem1D class
## Dependencies
DynamicalSystem1D requires matplotlib, NumPy, SciPy, and SymPy, so be sure to have those prepared and ready to go.
Once you have that done, you must then import the DynamicalSystem1D class:
```python
>>> from dynamical1D import DynamicalSystem1D
```

## Creating a 1 Dimensional Dynamical System
To create an 1D dynamical system, you will need to pass in a parameterized function, as well as the parameter variable:
```python
>>> from sympy.abc import z
>>> zDot = DynamicalSystem1D((z+1)*(z-1)*(z**2), z)
>>> zDot
DynamicalSystem1D(z**2*(z - 1)*(z + 1), z)
```

## Properties of aa 1 Dimensional Dynamical System
| Property        |  Description
| ------------- | -----
| `system`      |  The 1D system represented by the function
| `parameter` | The parameter of the 1D system
| `fixedPoints` | The fixed points of the 1D system
#### system
```python
>>> from sympy.abc import z
>>> zDot = DynamicalSystem1D((z+1)*(z-1)*(z**2), z)
>>> zDot.system
z**2*(z - 1)*(z + 1)
```
#### parameter
```python
>>> from sympy.abc import z
>>> zDot = DynamicalSystem1D((z+1)*(z-1)*(z**2), z)
>>> zDot.parameter
z
```
#### fixedPoints
```python
>>> from sympy.abc import z
>>> zDot = DynamicalSystem1D((z+1)*(z-1)*(z**2), z)
>>> zDot.fixedPoints
[-1, 0, 1]
```

## General 1D Dynamical System Functions
| Function        | Input(s)           | Description
| ------------- |-------------| -----
| `getEvalPoints(self)`      | self : DynamicalSystem1D | The points to look at when evaluating stability of the 1D system
| `getEvalPointValues(self)`      | self : DynamicalSystem1D      |   The point values to look at when evaluating stability of the 1D system
| `classify(self)` | self : DynamicalSystem1D      |  The stability classification of the 1D system 
| `potential(self)` | self : DynamicalSystem1D      |  The potential of the 1D dynamical system
| `drawPortrait(self)` | self : DynamicalSystem1D      |   The stability portrait for the 1D system 
| `solveSystem(self, value)` | self : DynamicalSystem1D, value: some value | The result when substituting the value into the system's parameter

Note: We are using the same system for all of the examples below
#### getEvalPoints
```python
>>> from sympy.abc import z
>>> zDot = DynamicalSystem1D((z+1)*(z-1)*(z**2), z)
>>> zDot.getEvalPoints()
[-2, -1/2, 1/2, 2]
```
#### getEvalPointValues
```python
>>> from sympy.abc import z
>>> zDot = DynamicalSystem1D((z+1)*(z-1)*(z**2), z)
>>> zDot.getEvalPointValues()
[12, -3/16, -3/16, 12]
```
#### classify
```python
>>> from sympy.abc import z
>>> zDot = DynamicalSystem1D((z+1)*(z-1)*(z**2), z)
>>> zDot.classify()
[(-1, 'Stable'), (0, 'Semi-Stable'), (1, 'Unstable')]
```
#### potential
```python
>>> from sympy.abc import z
>>> zDot = DynamicalSystem1D((z+1)*(z-1)*(z**2), z)
>>> zDot.potential()
-z**5/5 + z**3/3
```
#### solveSystem
```python
>>> from sympy.abc import z
>>> zDot = DynamicalSystem1D((z+1)*(z-1)*(z**2), z)
>>> zDot.solveSystem(5)
600
```
#### drawPortrait
```python
>>> from sympy.abc import z
>>> zDot = DynamicalSystem1D((z+1)*(z-1)*(z**2), z)
>>> zDot.drawPortrait()
```
![alt text](https://github.com/AlexKaracaoglu/GeomPy/blob/master/docs/technical/dynamical/dynamical1D/img/drawPortraitExample.png "drawPortrait Example")
