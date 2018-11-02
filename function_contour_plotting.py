import matplotlib.pyplot as plt
import numpy as np
from numpy import sin, cos

# ABCD are arbitrary real constants
A= 3.
B= 4.
C= 5.
D= 6.
# a, b are strictly positive real numbers
a= 1.
b= 1.
# n1, n2, n3 and m are real positive numbers
n1 = 3.
n2 = 3.
n3 = 2.

m = 6. 

# define the limite of the plot
lim = 5

# h is a factor which can be 1 or, more generally, 
#a function expressed as a Fourier series of sines and cosines whose arguments are multiples of the angle f.
def h(x):
	res = 1
	return res

def cosg(x):
	#res = h(x)* cos(x)
	res = ( h(x) * cos(x) )/( abs((1/a) * cos((m*x)/4))**n2 + abs((1/b) * sin((m*x)/4))**n3 )**(n1)
	return res
def sing(x):
	res = ( h(x) * sin(x) )/( abs((1/a) * cos((m*x)/4))**n2 + abs((1/b) * sin((m*x)/4))**n3 )**(n1)
	return res

# the main mathematical function
def f(x,y):
	return A * cosg( C * cosg(x) + D * sing(y)) + B * sing( C* cosg(x) + D * sing(y))

# Create the mesh grid
u = np.linspace(-lim,lim, 100)
v = np.linspace(-lim-1.5,lim-1.5, 100)
x,y = np.meshgrid(u,v)


# define the run function
def run():
	z = f(x,y)
	#print cosg(x)
	fig = plt.figure()
	ax = fig.add_subplot(111)
	c = ('#ff0000', '#ffff00', '#0000FF')#, '0.6', 'c', 'm','b')
	ax.contourf(x,y,z, colors=c)
	plt.savefig('contour_plot_a_{}_b_{}_n1_{}_n2_{}_n3_{}_m_{}_A_{}_B_{}_C_{}_D_{}_lim_{}.png'.format(a,b,n1,n2,n3,m,A,B,C,D,lim))
	plt.show()


if __name__ == '__main__':
	run()
