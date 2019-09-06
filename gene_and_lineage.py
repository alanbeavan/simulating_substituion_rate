#!/usr/bin/env python3.6
"""Simulate gene trees with gene and lineage rate variation."""

import variation
import variation
import my_module as mod

def main():
    """Generate gene trees and write to a file."""
    base_tree = mod.get_file_data("../timetree.nwk")[0]
    sigma2 = 0.25
    rate = 1


    tree = variation.relaxed_tree(base_tree, rate, sigma2)
    out = open("treefiles.nwk", "a+")
    i = 0
    while i < 70:
        rate = variation.get_rate(10, 10)
        new_tree = variation.modified_tree(tree, rate)
        out.write(new_tree + "\n")
        i += 1
    out.close()


if __name__ == "__main__":
    main()
