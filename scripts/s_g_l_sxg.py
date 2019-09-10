#!/usr/bin/env python3.6
"""Simulate conditions for control file.

Conditions:
site + gene + lineage + site by gene interactions.

"""

import variation
import my_module as mod

def main():
    """Simulate gene trees according to gene and lineage variation.
    Modify the site variation by gene by simulating different alpha values.
    """
    params = variation.Settings()
    base_tree = variation.relaxed_tree(mod.get_file_data("../timetree.nwk")[0], 1, params.lineage_sigma2)

    i = 0
    trees = []
    alphas = []
    while i < 70:
        rate = variation.get_rate(params.gene_alpha, params.gene_beta)
        trees.append(variation.modified_tree(base_tree, rate))
        alphas.append(str(variation.get_rate(params.site_alpha, params.site_alpha)))
        i += 1

    out_trees = open("treefiles.nwk", "w")
    out_trees.write("\n".join(trees))
    out_trees.close()

    out_alpha = open("alphas.txt", "w")
    out_alpha.write("\n".join(alphas))
    out_alpha.close()


if __name__ == "__main__":
    main()
