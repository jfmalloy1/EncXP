import json
import random

def main():
    #read in KEGG cpds
    data = json.load(open("containskegg_and_majorspecies.json"))
    all_seeds = data["Contains_KEGGID"]
    useless_seeds = ['C00238','C12244','C12567','C12568','C12569','C12603','C13563','C17390','C18606','C19316','C19572']
    real_seeds = list(set(all_seeds) - set(useless_seeds))

    #choose random sets of 10 from the main list
    for i in range(1000):
        rseeds = random.sample(real_seeds, 10)
        for seed in rseeds:
            print(seed, end=" ", file=open("seeds/rseeds_10nw_random_V2.txt", "a"))
        print("", file=open("seeds/rseeds_10nw_random_V2.txt", "a"))

    #choose random sets, with 5 fixed compounds
    fixed_seeds = data["major_species"]
    #Remove the fixed seeds from the full seed list
    seeds = list(set(real_seeds) - set(fixed_seeds))
    for i in range(1000):
        rseeds = random.sample(seeds, 5)
        for seed in fixed_seeds:
            print(seed, end=" ", file=open("seeds/rseeds_10nw_fixed_V2.txt", "a"))
        for seed in rseeds:
            print(seed, end=" ", file=open("seeds/rseeds_10nw_fixed_V2.txt", "a"))
        print("", file=open("seeds/rseeds_10nw_fixed_V2.txt", "a"))

if __name__ == "__main__":
    main()
