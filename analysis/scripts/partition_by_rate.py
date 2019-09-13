#!usr/bin/env python3.6
"""Produce a partitioned alignment with partitions based on the rate at the site.

Get the number of clusers from the user (or estimate)
Generate KDE for rates
if estiming the number of clusters
    take clusters between local minima
else:
    Use Jenks natural breaks optimization somehow
Write paritioned phylip
"""

import re
import sys
import scipy.stats
import numpy as np
import my_module as mod

def get_args():
    """Get the seq file and rates file from the user input."""
    if len(sys.argv) == 5:
        return sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    else:
        print("Usage: python3 partition_by_rate.py seq_file rates_file"\
              "output_file partition_dictionary_file")
        exit()

def get_rates(rates_file):
    """Get rates as dictionary from a paml output file."""
    lines = mod.get_file_data(rates_file)
    rates = {}
    pattern = re.compile("^\s+[0-9]+\s+[0-9]+\s+\S+\s+\S+\s+[0-9]+")
    for line in lines:
        if re.match(pattern, line):
            fields = line.split()
            rates[fields[0]] = fields[3]
    return rates

def estimate_kde(values):
    """Estimate kde for a list of values."""
    values = list(map(float, values))
    kde = scipy.stats.gaussian_kde(values)
    return kde

def get_minima(kde, values):
    """Find the local mimima of the density function."""
    values = np.array(list(map(float, values)))
    my_range = np.amax(values) - np.amin(values)
    step = my_range / 200
    low = np.amin(values)
    high = np.amax(values)

    x_values = list(np.arange(low, high, step))
    y_values = kde.evaluate(np.array(x_values))

    minima = []
    for i in range(1, len(x_values)-1):
        if y_values[i] < y_values[i-1] and y_values[i] <= y_values[i+1]:
            minima.append(x_values[i])
    return minima

def add_to_partition(partition, seqs, site):
    """Add the states for each species to a sequence dictionary."""
    for key, value in seqs.items():
        partition[key] += value[int(site) - 1]
    return partition

def partition_sites(seqs, rate_dict, bin_boundaries):
    """Split sites up into partitions based on rate."""
    empty_dict = {}
    ####Make general purpose####
    for sp in ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]:
        empty_dict[sp] = ""
    ###########end##############
    partitions = []
    for i in range(0, len(bin_boundaries)+1):
        partitions.append(empty_dict.copy())
    
    destinations = {}
    for site, rate in rate_dict.items():
        if float(rate) > bin_boundaries[len(bin_boundaries)-1]:
            partitions[-1] = add_to_partition(partitions[-1], seqs, site)
            destinations[site] = len(bin_boundaries)
        else:
            for i in range(0, len(bin_boundaries)):
                if float(rate) <= bin_boundaries[i]:
                    partitions[i] = add_to_partition(partitions[i], seqs, site)
                    destinations[site] = i
                    break
        
    return partitions, destinations

def write_phylip(alignments, filename):
    """Write alignments in a partitioned phylip file."""
    out = open(filename, "w")
    for alignment in alignments:
        out.write(str(len(alignment)) + "\t" + str(len(list(alignment.values())[0])) + "\n")
        for key, value in alignment.items():
            out.write("\n" + key + "  " + value)
        out.write("\n\n\n")
    out.close()

def write_sorting(sorting, filename):
    """Write the partition that each site went to to a file."""
    out = open(filename, "w")
    for key, value in sorting.items():
        out.write(str(key) + "\t" + str(value+1) + "\n")
    out.close()

def main():
    """Estimate partitions and write them to a file."""
    seqs_file, rates_file, out_file, sorting_file = get_args()
    seqs = mod.read_phylip_unpartitioned(seqs_file)
    rates = get_rates(rates_file)
    kde = estimate_kde(list(rates.values()))
    boundaries = get_minima(kde, list(rates.values()))
    alignments, sorting = partition_sites(seqs, rates, boundaries)
    write_phylip(alignments, out_file)
    write_sorting(sorting, sorting_file)

if __name__ == "__main__":
    main()
