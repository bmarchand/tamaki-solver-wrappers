from pymeiji import meiji_solver

def test_meiji_solver_call():
    tw, bag, bag_adj = meiji_solver([(0,1),(1,2),(2,3)])
    assert(tw==1)

def test_meiji_one_edge():
    tw, bag, bag_adj = meiji_solver([(0,1)])
    assert(tw==1)
