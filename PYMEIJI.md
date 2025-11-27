## Installation instructions
```
pip install pymeiji
```
## Usage
```python
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
```

```
    tw, bag, bag_adj = meiji_solver([(0,1),(1,2),(2,3)])
```
