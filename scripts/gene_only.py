#!/usr/bin/env python3.6
"""Simulate gene mean rates.

Get the mean gene rate from a gamma distribution.
Modify the background tree and append to a file for each tree
"""
import my_module as mod
import variation

def main():
    """Modify the 70 gene trees using simulated rates."""
    base_tree = mod.get_file_data("../timetree.nwk")[0]
    params = variation.Settings()
    i = 0
    while i < 70:
        rate = variation.get_rate(params.gene_alpha, params.gene_beta)
        new_tree = variation.modified_tree(base_tree, rate)
        out = open("treefiles.nwk", "a+")
        out.write(new_tree + "\n")
        out.close()
        i += 1
if __name__ == "__main__":
    main()
