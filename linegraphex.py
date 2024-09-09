import numpy
import matplotlib.pyplot as plt

#data set example

x = numpy.arange(1,11)
y = x * 2

plt.plot(x,y)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("simple line graph")
plt.show()
