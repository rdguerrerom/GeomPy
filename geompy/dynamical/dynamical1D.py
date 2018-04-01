"""1-Dimensional Dynamical System

Contains
========

DynamicalSystem1D

"""

from sympy.abc import *
from sympy.core.basic import Basic
from sympy.core import sympify
from sympy.solvers import solveset
from sympy import S
import matplotlib.pyplot as plt

class DynamicalSystem1D(Basic):
    """A 1 Dimensional Dynamical System

    A 1 dimensional dynamical system is constructed by a functions and a parameter value ie. 'x'

    Parameters
    ==========
    
    system : a function
    parameter: symbol, ie. 'x'

    Attributes
    ==========
    
    system
    parameter
    fuxedPoints

    Examples
    ========
    
    >>> from dynamical1D import DynamicalSystem1D
    >>> xDot = DynamicalSystem1D((x**2) - 1, x)
    >>> xDot
    DynamicalSystem1D(x**2 - 1, x)
    >>> yDot = DynamicalSystem1D(y**2, y)
    >>> yDot
    DynamicalSystem1D(y**2, y)
    
    """
    
    def __repr__(self):
        return type(self).__name__ + repr(self.args)
    
    def __str__(self):
        from sympy.printing import sstr
        ret = sstr(self.args)
        return type(self).__name__ + sstr(self.args)
    
    def __new__(cls, *args):
        args = [sympify(a) for a in args]
        return Basic.__new__(cls, *args)

    @property
    def system(self):
        """The system represented by the function

        Returns
        =======
        
        system : a function that represents the system
        
        Examples
        ========
        
        >>> from dynamical1D import DynamicalSystem1D
        >>> xDot = DynamicalSystem1D((x**2) - 1, x)
        >>> xDot.system
        x**2 - 1
        >>> yDot = DynamicalSystem1D(y**2, y)
        >>> yDot.system
        y**2

        """
        return self.args[0]

    @property
    def parameter(self):
        """The system represented by the function

        Returns
        =======
        
        parameter : symbol that represents the parameter of the system
        
        Examples
        ========
        
        >>> from dynamical1D import DynamicalSystem1D
        >>> xDot = DynamicalSystem1D((x**2) - 1, x)
        >>> xDot.parameter
        x
        >>> yDot = DynamicalSystem1D(y**2, y)
        >>> yDot.parameter
        y

        """
        return self.args[1]

    @property
    def fixedPoints(self):
        """The system represented by the function
        
        Examples
        ========
        
        >>> from dynamical1D import DynamicalSystem1D
        >>> xDot = DynamicalSystem1D((x**2) - 1, x)
        >>> xDot.fixedPoints
        [-1, 1]
        >>> yDot = DynamicalSystem1D(y**2, y)
        >>> yDot.fixedPoints
        [0]

        """
        fixedPoints = solveset(self.system,self.parameter,domain=S.Reals)
        (list(fixedPoints)).sort()
        return list(fixedPoints)

    def getEvalPoints(self):
        """The points to look at when evaluating stability
        
        Examples
        ========
        
        >>> from dynamical1D import DynamicalSystem1D
        >>> xDot = DynamicalSystem1D((x**2) - 1, x)
        >>> xDot.getEvalPoints()
        [-2, 0, 2]
        >>> yDot = DynamicalSystem1D(y**2, y)
        >>> yDot.getEvalPoints()
        [-1, 1]

        """
        fixedPoints = self.fixedPoints
        result = []
        for i in range(len(fixedPoints)):
            if len(self.fixedPoints) == 1:
                prev = fixedPoints[0] - 1
                nex = fixedPoints[0] + 1
            elif i == 0:
                prev = fixedPoints[0] - 1
                nex = (fixedPoints[0] + fixedPoints[1]) / 2
            elif (i == (len(self.fixedPoints)-1)):
                prev = (fixedPoints[i-1] + fixedPoints[i]) / 2
                nex = fixedPoints[i] + 1
            else:
                prev = (fixedPoints[i-1] + fixedPoints[i]) / 2
                nex = (fixedPoints[i] + fixedPoints[i+1]) / 2
            result.append(prev)
        result.append(nex)
        return result

    def getEvalPointValues(self):
        """The points to look at when evaluating stability
        
        Examples
        ========
        
        >>> from dynamical1D import DynamicalSystem1D
        >>> xDot = DynamicalSystem1D((x**2) - 1, x)
        >>> xDot.getEvalPointValues()
        [3, -1, 3]
        >>> yDot = DynamicalSystem1D(y**2, y)
        >>> yDot.getEvalPointValues()
        [1, 1]

        """
        result = []
        evalPoints = self.getEvalPoints()
        for evalPoint in evalPoints:
            result.append(self.system.subs(self.parameter, evalPoint))
        return result
                          
    def classify(self):
        """The points to look at when evaluating stability
        
        Examples
        ========
        
        >>> from dynamical1D import DynamicalSystem1D
        >>> xDot = DynamicalSystem1D((x**2) - 1, x)
        >>> xDot.classify()
        [(-1, 'Stable'), (1, 'Unstable')]
        >>> yDot = DynamicalSystem1D(y**2, y)
        >>> yDot.classify()
        [(0, 'Semi-Stable')]

        """
        result = []
        values = self.getEvalPointValues()
        for i in range(len(values)-1):
            if (values[i] > 0 and values[i+1] < 0):
                result.append((self.fixedPoints[i], "Stable"))
            elif (values[i] < 0 and values[i+1] > 0):
                result.append((self.fixedPoints[i], "Unstable"))
            else:
                result.append((self.fixedPoints[i], "Semi-Stable"))
        return result

    def drawPortrait(self):
        """The stability portrait for the 1 D system
        
        To run, simply call self.drawPortrait() and observe the plot.
        The stability portrait will be drawn and will label the
        stable, unstable and semi-stable fixed points for the dynamical
        system. If the plot is not in good scale, just use the zoom feature
        to adjust.

        """
        fixedPoints = self.fixedPoints
        results = self.classify()
        evalPoints = self.getEvalPoints()
        values = self.getEvalPointValues()
        plt.ylim(-.5,.5)
        plt.xlim(float(fixedPoints[0]-1.5), float(fixedPoints[len(fixedPoints)-1]+1.5))
        for fp in results:
            if fp[1] == "Unstable":
                plt.scatter(fp[0],0, color="none", edgecolor="black", label="Unstable Fixed Point")
            elif fp[1] == "Stable":
                plt.scatter(fp[0],0, color="black", edgecolor="black", label="Stable Fixed Point")
            else:
                plt.scatter(fp[0],0, color="yellow", edgecolor="yellow", label="Semi-Stable")
        for i in range(len(evalPoints)):
            if values[i] > 0:
                plt.arrow(evalPoints[i], 0, 0.001, 0, head_width=0.1, head_length=.30, fc="blue")
            if values[i] < 0:
                plt.arrow(evalPoints[i], 0, -0.001, 0, head_width=0.1, head_length=.30, fc="blue" )
        #Tidying up the legend on the plot - no repeats
        handles, labels = plt.gca().get_legend_handles_labels()
        handle_list, label_list = [], []
        for handle, label in zip(handles, labels):
            if label not in label_list:
                handle_list.append(handle)
                label_list.append(label)
        plt.legend(handle_list, label_list)
        plt.show()
