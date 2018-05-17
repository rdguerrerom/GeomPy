# Dynamical Systems
This is a technical overview of the DynamicalSystem1D class
## Dependencies
Curves requires matplotlib and SymPy, so be sure to have those prepared and ready to go.
Once you have that done, you must then import the Curve class:
```python
>>> from dynamical1D import DynamicalSystem1D
```

## Creating a 1 Dimensional Dynamical System
To create an 1D dynamical system, you will need to pass in a parameterized function, as well as the dependent variable:
```python
>>> xDot = DynamicalSystem1D((x**2) - 1, x)
>>> xDot
DynamicalSystem1D(x**2 - 1, x)
```

## Properties of aa 1 Dimensional Dynamical System
| Property        |  Description
| ------------- | -----
| `system`      |  The 1D system represented by the function
| `parameter` | The parameter of the 1D system
| `fixedPoints` | The fixed points of the 1D system
#### system
```python
>>> xDot = DynamicalSystem1D((x**2) - 1, x)
>>> xDot.system
x**2 - 1
```
#### parameter
```python
>>> xDot = DynamicalSystem1D((x**2) - 1, x)
>>> xDot.parameter
x
```
#### fixedPoints
```python
>>> xDot = DynamicalSystem1D((x**2) - 1, x)
>>> xDot.fixedPoints
[-1, 1]
```

## General 1D Dynamical System Functions
| Function        | Input(s)           | Description
| ------------- |-------------| -----
| `getEvalPoints(self)`      | self : DynamicalSystem1D | The points to look at when evaluating stability of the 1D system
| `getEvalPointValues(self)`      | self : DynamicalSystem1D      |   The point values to look at when evaluating stability of the 1D system
| `classify(self)` | self : DynamicalSystem1D      |  The stability classification of the 1D system 
| `potential(self)` | self : DynamicalSystem1D      |  The potential of the 1D dynamical system
| `drawPortrait(self)` | self : DynamicalSystem1D      |   The stability portrait for the 1D system 

Note: We are using the same system for all of the examples below
#### getEvalPoints
```python
>>> xDot = DynamicalSystem1D((x**2) - 1, x)
>>> xDot.getEvalPoints()
[-2, 0, 2]
```
#### getEvalPointValues
```python
>>> xDot = DynamicalSystem1D((x**2) - 1, x)
>>> xDot.getEvalPointValues()
[3, -1, 3]
```
#### classify
```python
>>> xDot = DynamicalSystem1D((x**2) - 1, x)
>>> xDot.classify()
[(-1, 'Stable'), (1, 'Unstable')]
```
#### potential
```python
>>> xDot = DynamicalSystem1D((x**2) - 1, x)
>>> xDot.potential()
-x**3/3 + x
```
#### drawPortrait
```python
>>> xDot = DynamicalSystem1D((x**2) - 1, x)
>>> xDot.drawPortrait()
```
![alt text](https://github.com/AlexKaracaoglu/GeomPy/blob/master/docs/technical/dynamical/dynamical1D/img/drawPortraitExample.png "drawPortrait Example")
