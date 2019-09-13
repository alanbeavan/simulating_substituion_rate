#!usr/bin/env python3.6
"""Write partitioned phylip file of each gene in the alignment."""

import sys
import partitioning
import my_module as mod

def main():
    """Produce partitioned file.
    
    Take user input
    Read in alignment
    Open output
    Print each gene's alignment.
    """
    params = partitioning.Settings()
    filename, output = partitioning.get_input()
    seqs = mod.read_phylip_unpartitioned(filename)
    partitioned = open(output, "w")
    for i in range(0, params.alignment_length, params.gene_length):
        partitioned.write(str(params.n_taxa) + "  " + str(params.gene_length))
        for key, value in seqs.items():
            partitioned.write("\n" + key + "  " + value[i:i+params.gene_length])
        partitioned.write("\n\n")
    partitioned.close()

if __name__ == "__main__":
    main()
