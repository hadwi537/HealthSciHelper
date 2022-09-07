#!/usr/bin/env python


from dsplot.graph import Graph
from create_tree import get_prereq_list


graph = Graph(
    {0: [1, 4, 5], 1: [3, 4], 2: [1], 3: [2, 4], 4: [], 5: []}, directed=True
)
graph.plot()

# graph.savefig(filename='graph.png')

# this will then send the image to 

def create_tree(paper_code):
    g = Graph(
        get_prereq_list(paper_code), directed=True
    )

    g.plot()

    g.savefig(filename='g.png')

if __name__ == '__main__':
    create_tree('MATH306')
