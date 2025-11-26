import jpype
import jpype.imports
import os
from jpype.types import *

def start_jvm_if_needed():
    if jpype.isJVMStarted():
        return

    package_dir = os.path.dirname(__file__)
    jar_path = os.path.join(package_dir, "jar", "tamaki_solver.jar")
    jpype.startJVM(classpath=[jar_path])


def tamaki_solver(edge_list):
    """
        edges: list of (u,v) integers, starting at 0.

        returns: width, bag, bag_adj
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
