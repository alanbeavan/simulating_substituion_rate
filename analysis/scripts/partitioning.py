#!usr/bin/env python3.6
"""Module to help partititoning of datasets."""

import sys

class Settings():
    """Parameters of the gene and rate boundaries etc."""
    def __init__(self):
        """Initialise parameters."""
        self.gene_length = 3000
        self.site_bin_length = 300
        self.alignment_length = 210000
        self.n_taxa = 10

def get_input():
    """Get the input and output files."""
    if len(sys.argv) == 3:
        return sys.argv[1], sys.argv[2]
    else:
        print("Usage: python3 partition_by_rate.py input output")
        exit()

