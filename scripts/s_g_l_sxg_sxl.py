#!/usr/bin/env python3.6
"""Simulate conditions for control file.

Conditions:
site + gene + lineage + site by gene + site x lineage.

"""

import variation
import my_module as mod

def main():
    """Simulate gene trees according to gene and lineage variation.
    Modify the site variation by gene by simulating different alpha values.
    also modify the clock for each site partition.
    """
    params = variation.Settings()
    base_tree = variation.relaxed_tree(mod.get_file_data("../timetree.nwk")[0], 1, params.lineage_sigma2)

    i = 0
    trees = []
    alphas = []
    while i < 70:
        relaxed_trees = []
        rate = variation.get_rate(params.gene_alpha, params.gene_beta)
        j = 0
        while j < params.n_bins_per_gene:
            relaxed_trees.append(variation.relaxed_tree(base_tree,
                                                        rate,
                                                        params.lineage_sigma2
                                                        ))
            j += 1
        trees.append(relaxed_trees)

        alphas.append(str(variation.get_rate(params.site_alpha, params.site_alpha)))
        i += 1
    
    out_trees = open("treefiles.nwk", "w")
    for set_of_trees in trees:
        out_trees.write("\t".join(set_of_trees) + "\n")
    out_trees.close()

    out_alpha = open("alphas.txt", "w")
    out_alpha.write("\n".join(alphas))
    out_alpha.close()


if __name__ == "__main__":
    main()
