import json
import random

def main():
    #read in KEGG cpds
    data = json.load(open("containskegg_and_majorspecies.json"))

    #choose random sets of 10 from the main list
    for i in range(1000):
        rseeds = random.sample(data["Contains_KEGGID"], 10)
        for seed in rseeds:
            print(seed, end=" ", file=open("seeds/rseeds_10nw_revised.txt", "a"))
        print("", file=open("seeds/rseeds_10nw_random.txt", "a"))

    #choose random sets, with 5 fixed compounds
    fixed_seeds = data["major_species"]
    seeds = data["Contains_KEGGID"]
    #Remove the fixed seeds from the full seed list
    seeds = list(set(seeds) - set(fixed_seeds))
    for i in range(1000):
        rseeds = random.sample(seeds, 5)
        for seed in fixed_seeds:
            print(seed, end=" ", file=open("seeds/rseeds_10nw_fixed.txt", "a"))
        for seed in rseeds:
            print(seed, end=" ", file=open("seeds/rseeds_10nw_fixed.txt", "a"))
        print("", file=open("seeds/rseeds_10nw_5fixed.txt", "a"))

if __name__ == "__main__":
    main()
