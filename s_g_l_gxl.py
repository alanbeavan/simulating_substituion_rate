#!/usr/bin/env python3.6
"""Simulate gene trees with, site, gene, lineage and gene x lineage rate variation."""

import variation
import variation
import my_module as mod

def main():
    """Generate gene trees and write to a file."""
    base_tree = mod.get_file_data("../timetree.nwk")[0]
    params = variation.Settings()
    rate = 1


    tree = variation.relaxed_tree(base_tree, rate, params.lineage_sigma2)
    out = open("treefiles.nwk", "a+")
    i = 0
    while i < 70:
        rate = variation.get_rate(params.gene_alpha, params.gene_beta)
        new_tree = variation.relaxed_tree(tree, rate, params.lineage_sigma2)
        out.write(new_tree + "\n")
        i += 1
    out.close()


if __name__ == "__main__":
    main()
