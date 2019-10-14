import pylab
import numpy
x = numpy.linspace(-15,15,100)
L=3
R=2
y = numpy.sin(x*L)
T=R/x
Z=y*T
pylab.plot(x,Z)