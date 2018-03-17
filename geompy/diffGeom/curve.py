"""Curves in n-dimensional Euclidean space

Contains
========

Curve

"""


import numpy as np
from sympy import integrate, sqrt
from sympy.abc import *
from sympy.core import sympify, diff
from sympy.core.containers import Tuple
from sympy.geometry.entity import GeometryEntity, GeometrySet

class Curve(GeometrySet):
    """A curve in space n-dimensional space

    A curve is constructed by a parameterized functions and a parameter value ie. 'x'

    Parameters
    ==========

    function : list of functions
    parameter: symbol

    Attributes
    ==========
    functions
    parameter
    dimension

    Examples
    ========

    >>> from curve import Curve
    >>> from sympy import sin
    >>> alpha = Curve((x + 1, x - 2, x**3, sin(x)), x)
    >>> alpha
    Curve((x + 1, x - 2, x**3, sin(x)), x)

    """
    def __new__(cls, functions, parameter):
        obj = GeometryEntity.__new__(cls, functions,parameter)
        return obj

    @property
    def functions(self):
        """The functions that define the curve

        Returns
        =======

        functions : list of parameterized functions

        Examples
        ========

        >>> from curve import Curve
        >>> from sympy import sin
        >>> alpha = Curve((x + 1, x - 2, x**3, sin(x)), x)
        >>> alpha.functions
        (x + 1, x - 2, x**3, sin(x))

        """
        return self.args[0]

    @property
    def parameter(self):
        """The parameter of the curve

        Returns
        =======

        parameter : symbol that represents the parameter of the curve

        Examples
        ========

        >>> from curve import Curve
        >>> from sympy import sin
        >>> alpha = Curve((x + 1, x - 2, x**3, sin(x)), x)
        >>> alpha.parameter
        x

        """
        return self.args[1]

    @property
    def dimension(self):
        """The dimension of the curve

        Examples
        ========

        >>> from curve import Curve
        >>> from sympy import sin
        >>> alpha = Curve((x + 1, x - 2, x**3, sin(x)), x)
        >>> alpha.dimension
        4

        """
        return len(self.args[0])

    def dot(v1, v2):
        """The dot product of two curves

        Examples
        ========

        >>> from curve import Curve
        >>> from sympy import sin
        >>> alpha = Curve((x + 1, x - 2, x**3, sin(x)), x)
        >>> beta = Curve((x, 5, x**2, 2 * x), x)
        >>> alpha.dot(beta)
        x**5 + x**2 + 2*x*sin(x) + 6*x - 10

        """
        result = np.dot(v1.functions,v2.functions)
        if type(result) is np.int32:
            return result
        return (result).simplify()

    def length(self):
        """The length of the curve

        Examples
        ========

        >>> from curve import Curve
        >>> from sympy import sin
        >>> alpha = Curve((x + 1, x - 2, x**3, sin(x)), x)
        >>> alpha.length()
        sqrt(x**6 + 2*x**2 - 2*x + sin(x)**2 + 5)

        """
        result = self.dot(self)
        result = sqrt(result)
        if type(result) is np.int32:
            return result
        return (result).simplify()

    ## cos(theta) = angle(v1,v2)
    def angle(v1,v2):
        """The cos(angle) created between two curves

        Examples
        ========

        >>> from curve import Curve
        >>> from sympy import sin, cos
        >>> alpha = Curve((-sin(x), cos(x), 1), x)
        >>> beta = Curve((0, 0, 1), x)
        >>> alpha.angle(beta)
        sqrt(2)/2

        """
        dots = v1.dot(v2)
        simplifiedLengths = (v1.length() * v2.length())
        result = dots / simplifiedLengths
        if type(result) is np.int32:
            return result
        return (dots / simplifiedLengths).simplify()

    def isPerpendicular(self,C):
        """If two curves are perpendicular

        Examples
        ========

        >>> from curve import Curve
        >>> alpha = Curve((0, 0, 1), x)
        >>> beta = Curve((0, 1, 0), x)
        >>> alpha.isPerpendicular(beta)
        True

        """
        return np.dot(self.functions, C.functions) == 0

    def cross(self, C):
        """The cross product of two curves

        Examples
        ========

        >>> from curve import Curve
        >>> from sympy import sin, cos
        >>> alpha = Curve((-sin(x), cos(x), 1), x)
        >>> beta = Curve((0, 0, 1), x)
        >>> alpha.cross(beta)
        Curve((cos(x), sin(x), 0), x)

        """
        product = list(np.cross((self.functions),(C.functions)))
        result = []
        for pr in product:
            result.append(pr.simplify())
        return Curve(result, self.parameter)

    def isUnitLength(self):
        """If the curve is of unit length

        Examples
        ========

        >>> from curve import Curve
        >>> from sympy import sin, cos
        >>> alpha = Curve((-sin(x), cos(x), 0), x)
        >>> alpha.isUnitLength()
        True

        """
        d = self.diffV()
        return d.length() == 1

    def uTangent(self):
        """The Unit Speed Frenet Frame Tangent Vector (T)

        Raises
        ======

        ValueError
            When the curve is not 3 dimensions
        ValueError
            When the curve is not of unit length

        Examples
        ========

        >>> from curve import Curve
        >>> from sympy import sin, cos
        >>> alpha = Curve((sin(x), cos(x), 0), x)
        >>> alpha.uTangent()
        Curve((cos(x), -sin(x), 0), x)

        """
        if self.dimension != 3:
            raise ValueError("Finding the Tangent curve requires 3 dimensions "
                "but got %s dimensions" % str(self.dimension))
        if not self.isUnitLength():
            raise ValueError("Using uTangent requires a unit speed curve "
                "but input curve is not")
        return self.diffV()

    def uNormal(self):
        """The Unit Speed Frenet Frame Tangent Vector (N)

        Raises
        ======

        ValueError
            When the curve is not 3 dimensions
        ValueError
            When the curve is not of unit length

        Examples
        ========

        >>> from curve import Curve
        >>> from sympy import sin, cos
        >>> alpha = Curve((sin(x), cos(x), 0), x)
        >>> alpha.uNormal()
        Curve((-sin(x), -cos(x), 0), x)

        """
        if self.dimension != 3:
            raise ValueError("Finding the Normal curve requires 3 dimensions "
                "but got %s dimensions" % str(self.dimension))
        if not self.isUnitLength():
            raise ValueError("Using uNormal requires a unit speed curve "
                "but input curve is not")
        tangentPrime = (self.uTangent()).diffV()
        tPrimeLength = tangentPrime.length()
        if (tPrimeLength != 0):
            tangentPrimeFunctions = list(((np.array(tangentPrime.functions))/ tPrimeLength))
            return Curve(tangentPrimeFunctions, self.parameter)
        else:
            return "undefined"

    def uCurvature(self):
        """The curvature of the unit speed curve (kappa)

        Raises
        ======

        ValueError
            When the curve is not 3 dimensions
        ValueError
            When the curve is not of unit speed

        Examples
        ========

        >>> from curve import Curve
        >>> from sympy import sin, cos
        >>> alpha = Curve((sin(x), cos(x), 0), x)
        >>> alpha.uCurvature()
        1

        """
        if self.dimension != 3:
            raise ValueError("Finding the curvature of the curve requires "
                "3 dimensions but got %s dimensions" % str(self.dimension))
        if not self.isUnitLength():
            raise ValueError("Using uCurvature requires a unit speed curve "
                "but input curve is not")
        tangentPrime = self.uTangent().diffV()
        return tangentPrime.length()

    def solveCurve(self, value):
        """The result when substituting the value into the curve's parameter

        Examples
        ========

        >>> from curve import Curve
        >>> from sympy import sin, cos
        >>> alpha = Curve((sin(x), cos(x), 0), x)
        >>> alpha.solveCurve(5)
        [sin(5), cos(5), 0]

        """
        results = []
        for func in (self.functions):
            results.append(func.subs(self.parameter,value))
        return results

    def uBinormal(self):
        """The Unit Speed Frenet Frame Binormal Vector (B)

        Raises
        ======

        ValueError
            When the curve is not 3 dimensions
        ValueError
            When the curve is not of unit speed

        Examples
        ========

        >>> from curve import Curve
        >>> from sympy import sin, cos
        >>> alpha = Curve((sin(x), cos(x), 0), x)
        >>> alpha.uBinormal()
        Curve((0, 0, -1), x)

        """
        if self.dimension != 3:
            raise ValueError("Finding the Binormal curve requires 3 dimensions "
                "but got %s dimensions" % str(self.dimension))
        if not self.isUnitLength():
            raise ValueError("Using uBinormal requires a unit speed curve "
                "but input curve is not")
        normal = self.uNormal()
        tangent = self.uTangent()
        if type(normal) is str:
            return "undefined"
        else:
            return tangent.cross(normal)

    def uTorsion(self):
        """The Torsion of the unit speed curve (tau)

        Raises
        ======

        ValueError
            When the curve is not 3 dimensions
        ValueError
            When the curve is not of unit speed

        Examples
        ========

        >>> from curve import Curve
        >>> from sympy import sin, cos
        >>> alpha = Curve((sin(x), cos(x), 0), x)
        >>> alpha.uTorsion()
        0

        """
        if self.dimension != 3:
            raise ValueError("Finding the curvature of the curve requires "
                "3 dimensions but got %s dimensions" % str(self.dimension))
        if not self.isUnitLength():
            raise ValueError("Using uTorsion requires a unit speed curve "
                "but input curve is not")
        binormalPrime = (self.uBinormal()).diffV()
        normal = self.uNormal()
        return binormalPrime.dot(normal)

    def diffV(self):
        """The derivative of each function in the curve

        Examples
        ========

        >>> from curve import Curve
        >>> from sympy import sin, cos
        >>> alpha = Curve((sin(x), cos(x), 0), x)
        >>> alpha.diffV()
        Curve((cos(x), -sin(x), 0), x)

        """
        result = []
        for func in self.functions:
            result.append(diff(func,self.parameter))
        return Curve(result,self.parameter)

    def divide(self,quantity):
        functions = []
        for func in self.functions:
            functions.append(func / quantity)
        return Curve(functions, self.parameter)

    def Torsion(self):
        """The Torsion of the curve (tau)

        Raises
        ======

        ValueError
            When the curve is not 3 dimensions

        Examples
        ========

        >>> from curve import Curve
        >>> from sympy import sin, cos
        >>> alpha = Curve((sin(x), cos(x), 0), x)
        >>> alpha.Torsion()
        0

        """
        if self.dimension != 3:
            raise ValueError("Finding the torsion of the curve requires "
                "3 dimensions but got %s dimensions" % str(self.dimension))
        alphaPrime = self.diffV()
        alphaDoublePrime = alphaPrime.diffV()
        alphaTriplePrime = alphaDoublePrime.diffV()
        alphaPrimesCross = alphaPrime.cross(alphaDoublePrime)
        numerator = alphaPrimesCross.dot(alphaTriplePrime) * -1
        denominator = (alphaPrimesCross.length())**2
        return numerator / denominator

    def Curvature(self):
        """The Curvature of the curve (kappa)

        Raises
        ======

        ValueError
            When the curve is not 3 dimensions

        Examples
        ========

        >>> from curve import Curve
        >>> from sympy import sin, cos
        >>> alpha = Curve((sin(x), cos(x), 0), x)
        >>> alpha.Curvature()
        1

        """
        if self.dimension != 3:
            raise ValueError("Finding the curvature of the curve requires "
                "3 dimensions but got %s dimensions" % str(self.dimension))
        alphaPrime = self.diffV()
        alphaDoublePrime = alphaPrime.diffV()
        alphaPrimesCross = alphaPrime.cross(alphaDoublePrime)
        numerator = alphaPrimesCross.length()
        denominator = (alphaPrime.length())**3
        return numerator / denominator

    def Tangent(self):
        """The Frenet Frame Tangent Vector (T)

        Raises
        ======

        ValueError
            When the curve is not 3 dimensions

        Examples
        ========

        >>> from curve import Curve
        >>> from sympy import sin, cos
        >>> alpha = Curve((sin(x), cos(x), 0), x)
        >>> alpha.Tangent()
        Curve((cos(x), -sin(x), 0), x)

        """
        if self.dimension != 3:
            raise ValueError("Finding the Tangent of the curve requires "
                "3 dimensions but got %s dimensions" % str(self.dimension))
        alphaPrime = self.diffV()
        lengthAlphaPrime = alphaPrime.length()
        return alphaPrime.divide(lengthAlphaPrime)

    def Normal(self):
        """The Frenet Frame Normal Vector (N)

        Raises
        ======

        ValueError
            When the curve is not 3 dimensions

        Examples
        ========

        >>> from curve import Curve
        >>> from sympy import sin, cos
        >>> alpha = Curve((sin(x), cos(x), 0), x)
        >>> alpha.Normal()
        Curve((-sin(x), -cos(x), 0), x)

        """
        if self.dimension != 3:
            raise ValueError("Finding the Normal of the curve requires "
                "3 dimensions but got %s dimensions" % str(self.dimension))
        return self.Binormal().cross(self.Tangent())

    def Binormal(self):
        """The Frenet Frame Binormal Vector (B)

        Raises
        ======

        ValueError
            When the curve is not 3 dimensions

        Examples
        ========

        >>> from curve import Curve
        >>> from sympy import sin, cos
        >>> alpha = Curve((sin(x), cos(x), 0), x)
        >>> alpha.Binormal()
        Curve((0, 0, -1), x)

        """
        if self.dimension != 3:
            raise ValueError("Finding the Binormal of the curve requires "
                "3 dimensions but got %s dimensions" % str(self.dimension))
        alphaPrime = self.diffV()
        alphaDoublePrime = alphaPrime.diffV()
        alphaPrimesCross = alphaPrime.cross(alphaDoublePrime)
        length = alphaPrimesCross.length()
        return alphaPrimesCross.divide(length)
