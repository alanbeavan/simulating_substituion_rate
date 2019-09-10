#!/usr/bin/env python3.6
"""Generate gene tree with lineage specific variation only.

Requires:
lineage_variation
my_module

"""

import variation
import my_module as mod

def main():
    """Write gene trees to a file."""
    base_tree = mod.get_file_data("../timetree.nwk")[0]
    params = variation.Settings()

    rate = 1
    
    tree = variation.relaxed_tree(base_tree, rate, params.lineage_sigma2)
    out = open("treefiles.nwk", "a+")
    i = 0
    while i < 70:
        out.write(tree + "\n")
        i += 1
    out.close()

if __name__ == "__main__":
    main()
