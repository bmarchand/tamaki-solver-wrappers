import jpype
import jpype.imports
import os
from jpype.types import *

def start_jvm_if_needed():
    if jpype.isJVMStarted():
        return

    package_dir = os.path.dirname(__file__)
    jar_path = os.path.join(package_dir, "jar", "tamaki_solver.jar")
    jpype.startJVM("--enable-native-access=ALL-UNNAMED",classpath=[jar_path])


def meiji_solver(edge_list):
    """
        Exact computation of the treewidth of a graph.

        Python-wrapper around the PACE 2017 meiji solver,
        which was originally written in java,
        and whose details are described in
        https://arxiv.org/abs/1704.05286

        Parameters
        ----------
            edge_list: list of tuples of integers 
                list of edges of the graph. Each edge must
                be a tuple of 2 integers (u,v).
                The integers should range from 0 to
                the number of vertices in the graph - 1.

        Returns
        -------
        (treewidth, bags, bag_adj)
            A tuple consisting of three objects.  The first is an integer equal
            to the treewidth.  The second is a python dictionary associating
            integers (bag index) to lists of integers (bag content). The 
            third is also a dictionary, associating integers (bag index)
            to lists of integers (indices of the neighbors of that bag
            in the tree decomposition).
    """
    nnodes = max([max(u,v) for u,v in edge_list])+1

    start_jvm_if_needed()

    from tw.exact import Graph
    from tw.exact import MainDecomposer
    
    g = Graph(nnodes)
    for u,v in edge_list:
        g.addEdge(u,v)

        
    td = MainDecomposer.decompose(g)

    bags = {}
    bag_adj = {}
    for k, bag in enumerate(td.bags):
        if k==0:
            continue
        bags[k] = list(bag)
        bag_adj[k] = list(td.neighbor[k])

    return td.width, bags, bag_adj

if __name__=="__main__":
    td = tamaki_solver([(0,1),(1,2),(2,3)])
    print(td)
