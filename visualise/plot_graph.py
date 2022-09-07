#!/usr/bin/env python

# import graphviz as gv
# import pylab

from dsplot.graph import Graph
from connect_to_mongo_db import get_prereq_list


graph = Graph(
    {0: [1, 4, 5], 1: [3, 4], 2: [1], 3: [2, 4], 4: [], 5: []}, directed=True
)
graph.plot()

# graph.savefig(filename='graph.png')

# this will then send the image to 

g = Graph(
    get_prereq_list('MATH306'), directed=True
)

g.plot()

g.savefig(filename='g.png')