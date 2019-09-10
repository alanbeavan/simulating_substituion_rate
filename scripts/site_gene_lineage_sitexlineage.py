#!/usr/bin/env python3.6
"""Simulate trees under site + lineage + site x lineage variation."""

import variation
import my_module as mod

def main():
    """Simulate gene trees for genes with site and lineage variation

    This will involve a base tree for each bin per gene
    each gene will have these trees for each partition multiplied by
    the gene rate"""

    base_tree = mod.get_file_data("timetree.nwk")[0]
    params = variation.Settings()

    relaxed_trees = []
    i = 0
    while i < params.n_bins_per_gene:
        relaxed_trees.append(variation.relaxed_tree(base_tree, 
                                                    1, 
                                                    params.lineage_sigma2
                                                    ))
    out = open("treefiles.nwk", "w")
    i = 0
    while i < 70:
        trees_to_write = []
        for tree in relaxed_trees:
            rate = variation.get_rate(params.gene_alpha, params.gene_beta)
            trees_to_write.append(tree, rate)
        out.write("\t".join(trees_to_write) +"\n")


if __name__ == "__main__":
    main()
