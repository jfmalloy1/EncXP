import pandas as pd
import numpy as np
import random

compounds = pd.read_csv('Enceladus_Compounds_and_Concentrations.csv')
seed_set = []

#Running sum of concentrations
rsums = np.cumsum(compounds['Concentration']).tolist()

#path to csv file
path = "rseeds.dat"
f = open(path, "w")

#create 100 sets of random seed sets, each 10 compounds long
for i in range(100):
    seed_set = []
    #Calculate 10 random numbers, find compound associated with each
    while len(seed_set) < 10:
        r = random.uniform(0, np.sum(compounds['Concentration']))
        gc = np.extract(rsums > r, rsums)
        element = rsums.index(gc[0])
        if (compounds['Compound'][element] not in seed_set):
            seed_set.append(compounds['Compound'][element])

    #Final seet set outputting to a file
    for seed in seed_set:
        f.write(seed + " ")
    f.write("\n")

f.close()
