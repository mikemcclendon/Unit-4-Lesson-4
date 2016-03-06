import matplotlib.pyplot as plt
from sklearn import datasets
import numpy as np
import random
import math
import itertools

iris = datasets.load_iris()
#setting the values of interest
X = iris.data[:, :2]
color = iris.target

rand = random.randint(0, len(iris.data))
random_point = X[rand]
dist = []
classy = []

#defining functions to calculate distance and the most common items in a list
def distance(p0, p1):
    return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)

def most_common(L):
  groups = itertools.groupby(sorted(L))
  def _auxfun((item, iterable)):
    return len(list(iterable)), -L.index(item)
  return max(groups, key=_auxfun)[0]

#setting the iris data to a tuple and then iterating through that list of tuples for dist
X = map(lambda x: (x), X)    
it = 0
for tup in X:
	dist.append(distance(random_point, tup))
	classy.append(color[it])
	it= it+1

#zipping distance and class, sorting, breaking them apart, then finding majority	
def knn(k):
	empty = []
	pairs = zip(dist, classy)
	pairs = sorted((pairs), key=lambda tup: tup[0])
	distS, classyS =zip(*pairs)
	for i in range(k):
		empty.append(classyS[i])
	print most_common(empty)
	

knn(15)








