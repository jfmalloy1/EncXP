import re
import json

def remove_apparate_rxns(rxns, input, output):
    with open(input) as f:
        data = json.load(f)
        for r in rxns:
            if r in data['products']:
                del data['products'][r]
            if r in data['substrates']:
                del data['substrates'][r]

        with open(output, "w") as f2:
            json.dump(data, f2)

def get_rxns(filename):
    rxns = []
    with open(filename) as f:
        for line in f:
            l = line.split()
            rxns.append(re.sub('[\W_]', '', l[0]))
    return rxns

def main():
    rxns = get_rxns("apparate_rxns.txt")
    remove_apparate_rxns(rxns, "links/reaction_edges.json", "links/reaction_edges_curated2.json")

if __name__ == "__main__":
    main()
