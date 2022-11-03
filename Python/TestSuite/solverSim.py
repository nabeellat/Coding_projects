"""Unit Test for solver"""


import aps
import json
import random
import numpy as np
from numpy.random import default_rng


def random_generate_timings(dim):
    l = []
    rng = default_rng()
    l.append(rng.dirichlet(np.ones(dim+1),size=200))
    return l

def positions(l,room):
    dot_product = 0
    room["base_stations"] = [np.array(b) for b in room["base_stations"]]
    for vecs in l:
        for i in range(len(room['base_stations'])):
            dot_product += vecs*room["base_stations"][i]
    return dot_product

def timegen(p,room):
    delta = 3.0 * random.random()
    times = []
    for vec in p:
        distances = [np.linalg.norm(b - vec) for b in room["base_stations"]]
        times.append([(d / room['speed']) + i * room['tsep'] + delta for i, d in enumerate(distances)]) 
    return times

def simulate(infile,times,pos):
    x_prime = []
    c = aps.APSConfig(infile)
    i = 0
    
    for item in times:
        v = aps.TimeVector(c,*item)
        solverAns = v.solve_eposition()

        if err > .01:
            print("{} {} {} {} passed configurable error tolerance -- FAIL".format(item,pos[i],solverAns,err))
        else:
            print("{} {} {} {} passed".format(item,pos[i],solverAns,err))
        i+=1
    

    


config = "4.57configs.json"
with open(config, "r") as infile:
    room = json.load(infile)
dim = len(room['base_stations'][1])
l = random_generate_timings(dim)
pos = positions(l,room)
times = timegen(pos,room)
simulate(config,times,pos)

