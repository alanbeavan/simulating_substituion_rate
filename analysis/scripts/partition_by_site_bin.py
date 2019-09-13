#!usr/bin/env python3.6
"""Produce a partioned phylip file with each partition correspoding to a site bin.

This will be 10 per gene so 700 clusters - which may be too high.
"""

import partitioning
import my_module as mod

def main():
    """Create the partitoned file"""
    params = partitioning.Settings()
    filename, output = partitioning.get_input()
    seqs = mod.read_phylip_unpartitioned(filename)
    partitioned = open(output, "w")
    for i in range(0, params.alignment_length, params.site_bin_length):
        partitioned.write(str(params.n_taxa) + "  " + str(params.site_bin_length))
        for key, value in seqs.items():
            partitioned.write("\n" + key + "  " + value[i:i+params.site_bin_length])
        partitioned.write("\n\n")
    partitioned.close()

if __name__ == "__main__":
    main()
