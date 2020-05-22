import pandas as pd
import numpy as np
import random

compounds = pd.read_csv('Enceladus_Compounds_and_Concentrations.csv')
seed_set = []

#Running sum of concentrations
rsums = np.cumsum(compounds['Concentration']).tolist()
print(rsums)

#path to csv file
path = "rseeds_10nw_confidence.dat"
f = open(path, "w")

#VERSION: all seed sets (only one needed)
# seed_set = compounds['Compound'].tolist()
# print(seed_set)
#
# #Final seet set outputting to a file
# for seed in seed_set:
#     f.write(seed + " ")
# f.write("\n")

#create 100 sets of random seed sets
for i in range(1000):
    print(i)
    seed_set = []
    #VERSION: Calculate 10 random numbers weighted average (10w)
    # while len(seed_set) < 10:
    #     r = random.uniform(0, np.sum(compounds['Concentration']))
    #     #print(r)
    #     gc = np.extract(rsums > r, rsums)
    #     element = rsums.index(gc[0])
    #     if (compounds['Compound'][element] not in seed_set):
    #         seed_set.append(compounds['Compound'][element])


    #VERSION: 5 random (with weights) 5w
    # while len(seed_set) < 5:
    #     r = random.uniform(0, np.sum(compounds['Concentration']))
    #     gc = np.extract(rsums > r, rsums)
    #     element = rsums.index(gc[0])
    #     if (compounds['Compound'][element] not in seed_set):
    #         seed_set.append(compounds['Compound'][element])

    #VERSION: 5 random (no weight) 5nw
    # seed_set = random.sample(compounds['Compound'].tolist(), 5)
    # print(seed_set)

    #VERSION: 10 random (no weight) 10nw
    seed_set = random.sample(compounds['Compound'].tolist(), 10)
    print(seed_set)

    #Final seet set outputting to a file
    for seed in seed_set:
        f.write(seed + " ")
    f.write("\n")

f.close()
