#!/usr/bin/env python3.6
"""Simulate trees under site + gene + lineage + site x lineage variation."""

import variation
import my_module as mod

def main():
    """Simulate gene trees for genes with gene + lineage + sitexlineage variation.

    This will involve a base tree for each bin per gene
    each gene will have these trees for each partition multiplied by
    the gene rate"""

    base_tree = mod.get_file_data("../timetree.nwk")[0]
    params = variation.Settings()

    out = open("treefiles.nwk", "w")
    relaxed_trees = []
    i = 0
    while i < 70:
        j = 0
        rate = variation.get_rate(params.gene_alpha, params.gene_beta)
        while j < params.n_bins_per_gene:
            relaxed_trees.append(variation.relaxed_tree(base_tree, 
                                                        rate,
                                                        params.lineage_sigma2
                                                        ))
            j += 1
        out.write("\t".join(relaxed_trees) +"\n")
        i += 1
    out.close()

if __name__ == "__main__":
    main()
