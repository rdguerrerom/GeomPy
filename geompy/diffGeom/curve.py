# curve.py
# Alex Karacaoglu

# Numpy import
import numpy as np

# SymPy imports
from sympy import integrate, sqrt
from sympy.abc import *
from sympy.core import sympify, diff
from sympy.core.containers import Tuple
from sympy.geometry.entity import GeometryEntity, GeometrySet

class Curve(GeometrySet):
    def __new__(cls, functions, parameter):
        obj = GeometryEntity.__new__(cls, functions,parameter)
        return obj

    @property
    def functions(self):
        return self.args[0]

    @property
    def parameter(self):
        return self.args[1]

    def dot(v1, v2):
        result = np.dot(v1.functions,v2.functions)
        if type(result) is np.int32:
            return result
        return (result).simplify()

    def length(self):
        result = self.dot(self)
        result = sqrt(result)
        if type(result) is np.int32:
            return result
        return (result).simplify()

    ## cos(theta) = angle(v1,v2)
    def angle(v1,v2):
        dots = v1.dot(v2)
        simplifiedLengths = (v1.length() * v2.length())
        result = dots / simplifiedLengths
        if type(result) is np.int32:
            return result
        return (dots / simplifiedLengths).simplify()

    def isPerpendicular(self,C):
        return np.dot(self.functions, C.functions) == 0

    def cross(self, C):
        product = list(np.cross((self.functions),(C.functions)))
        result = []
        for pr in product:
            result.append(pr.simplify())
        return result

    def isParamArc(self):
        d = self.diffV()
        return d.length() == 1

    def uTangent(self):
        return self.diffV()

    def uNormal(self):
        tangentPrime = (self.uTangent()).diffV()
        tPrimeLength = tangentPrime.length()
        if (tPrimeLength != 0):
            tangentPrimeFunctions = list(((np.array(tangentPrime.functions))/ tPrimeLength))

            return Curve(tangentPrimeFunctions, self.parameter)
        else:
            return "undefined"

    def uCurvature(self):
        tangentPrime = self.uTangent().diffV()
        return tangentPrime.length()

    def solveCurve(self, value):
        results = []
        for func in (self.functions):
            results.append(func.subs(self.parameter,value))
        return results

    def uBinormal(self):
        normal = self.uNormal()
        tangent = self.uTangent()
        if type(normal) is str:
            return "undefined"
        else:
            return tangent.cross(normal)

    def uTorsion(self):
        binormalPrime = self.diffV()
        normal = self.uNormal()
        return dot(binormalPrime,normal)

    def diffV(self):
            result = []
            for func in self.functions:
                result.append(diff(func,self.parameter))
            return Curve(result,self.parameter)
