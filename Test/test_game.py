def load_src(name, fpath):
    import os, imp
    return imp.load_source(name, os.path.join(os.path.dirname(__file__), fpath))
 
load_src("game_of_life", "../game_of_life.py")
import numpy as np
import game_of_life
from game_of_life import generation, survival

def test_generation_dtype():
    """_survial_dtype() should return a np array"""
    new_universe = generation(np.zeros((4,5)))
    assert new_universe.shape == (4,5)

def test_survival_case1():
    """_survial_two()
    Any dead cell with exactly three live neighbours will come to life.
    i.e return 1
    """
    alive = 1
    cell_status = survival(1,1,np.array([0,1,0,0,0,0,1,0,1]).reshape(3,3))
    assert cell_status == alive

def test_survival_case2():
    """_survial_two()
    Any live cell with two or three live neighbours lives,
     unchanged, to the next generation i.t return 1
    """
    alive = 1
    cell_status = survival(1,1,np.array([0,0,0,0,1,0,1,1,1]).reshape(3,3))
    assert cell_status == alive

def test_survival_case3():
    """_survial_two()
    Any live cell with two or three live neighbours lives,
     unchanged, to the next generation i.t return 1
    """
    alive = 1
    cell_status = survival(1,1,np.array([0,0,0,0,1,0,0,1,1]).reshape(3,3))
    assert cell_status == alive

def test_death_case1():
    """_death_case1()
    Any live cell with more than three live neighbours dies (referred to as overpopulation or overcrowding).
    """
    dead = 0
    cell_status = survival(1,1,np.array([0,0,0,0,1,1,1,1,1]).reshape(3,3))
    assert cell_status == dead

def test_death_case2():
    """_death_case1()
    Any live cell with fewer than two live neighbours dies (referred to as underpopulation or exposure[1]).
    """
    dead = 0
    cell_status = survival(1,1,np.array([0,0,0,0,1,0,0,0,1]).reshape(3,3))
    assert cell_status == dead



